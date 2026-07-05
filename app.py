import logging
import os

import numpy as np
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from PIL import Image, UnidentifiedImageError
from tensorflow.keras.models import load_model
from werkzeug.exceptions import RequestEntityTooLarge

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MODEL_PATH = os.environ.get("MODEL_PATH", "./built_model.keras")
MAX_UPLOAD_MB = int(os.environ.get("MAX_UPLOAD_MB", "10"))
ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS", "*")
IMAGE_SIZE = (512, 512)
DECISION_THRESHOLD = float(os.environ.get("DECISION_THRESHOLD", "0.5"))

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = MAX_UPLOAD_MB * 1024 * 1024
CORS(app, resources={r"/predict": {"origins": ALLOWED_ORIGINS}})

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file '{MODEL_PATH}' not found!")
model = load_model(MODEL_PATH)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    img_file = request.files["image"]
    if not img_file.filename:
        return jsonify({"error": "Empty file"}), 400

    try:
        img = Image.open(img_file).convert("RGB").resize(IMAGE_SIZE)
    except UnidentifiedImageError:
        return jsonify({"error": "Uploaded file is not a valid image"}), 400

    img_array = np.expand_dims(np.array(img, dtype=np.float32) / 255.0, axis=0)

    try:
        probability = float(model.predict(img_array, verbose=0)[0][0])
    except Exception:
        logger.exception("Model inference failed")
        return jsonify({"error": "Inference failed"}), 500

    return jsonify(
        {
            "prediction": int(probability > DECISION_THRESHOLD),
            "probability": probability,
            "threshold": DECISION_THRESHOLD,
        }
    )


@app.errorhandler(RequestEntityTooLarge)
def handle_too_large(_):
    return jsonify({"error": f"File exceeds {MAX_UPLOAD_MB} MB limit"}), 413


if __name__ == "__main__":
    app.run(
        debug=os.environ.get("FLASK_DEBUG") == "1",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "5000")),
    )
