from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load the ML model
MODEL_PATH = "D:/Cancer_detection_app/built_model.keras"  # Ensure the model is in the same directory
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file '{MODEL_PATH}' not found!")
model = load_model(MODEL_PATH)

# Route to serve the frontend
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")  # Renders the main HTML page

# Route for prediction API
@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    # Get the uploaded image
    img_file = request.files["image"]

    try:
        # Preprocess the image
        img = Image.open(img_file).resize((512, 512))  # Adjust input size as per model
        img_array = np.array(img) / 255.0  # Normalize pixel values
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Make a prediction
        prediction = model.predict(img_array)
        result = {"prediction": int(prediction[0][0] > 0.5)}  # Binary output: 1 (malignant), 0 (benign)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
