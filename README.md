# 🔬 Skin Cancer Detection Web App

A deep-learning web application that classifies skin-lesion images as **benign**
or **malignant** using a CNN, served through a Flask backend with a clean,
animated web interface.

## Overview

Upload an image of a skin lesion and the app runs it through a trained
Convolutional Neural Network to predict whether it appears benign or malignant,
returning the result — with the model's confidence — in real time.

Built by a team of 4 as a full-stack ML project — covering model training, a
REST prediction API, a responsive frontend, and cloud deployment.

> ⚠️ **Medical disclaimer:** This project is for educational and research
> purposes only. It is **not** a medical device and must not be used for
> actual diagnosis. Always consult a qualified healthcare professional.

## ✨ Features

- **Image-based classification** — binary benign vs. malignant prediction from a skin-lesion photo.
- **Confidence score** — the API returns the raw sigmoid probability, not just a class label.
- **REST prediction API** — `/predict` endpoint accepting an image, plus a `/health` liveness probe.
- **Robust input handling** — JPEG, PNG, RGBA and grayscale images are all normalized to RGB.
- **Upload size limit** — 10 MB by default (configurable) with a clean `413` response.
- **Responsive web UI** — image preview, animated feedback (animate.css), disabled state during inference.
- **Production container** — Docker image runs under `waitress` as a non-root user.
- **Cloud-ready** — pre-configured for deployment to Azure App Service.

## 🧠 How It Works

```
Browser (upload image)
        │  POST /predict  (multipart form-data)
        ▼
Flask app  ─►  preprocess (convert RGB, resize 512×512, normalize 0–1)
        │
        ▼
Keras CNN (built_model.keras)  ─►  sigmoid output (probability)
        │
        ▼
probability > threshold ?  →  1 = Malignant  /  0 = Benign
        │
        ▼
JSON response { prediction, probability, threshold }  ─►  rendered in the UI
```

## 📁 Project Structure

```
Cancer_detection_app/
├── app.py                 # Flask server + /predict API + model inference
├── built_model.keras      # Trained CNN model (input 512×512×3, sigmoid output)
├── requirements.txt       # Pinned Python dependencies
├── Dockerfile             # Production container (waitress WSGI)
├── .dockerignore
├── templates/
│   └── index.html         # Frontend page (upload form + result area)
├── static/
│   ├── Designer.jpeg      # Header illustration
│   ├── script.js          # Handles upload, preview, fetch to /predict
│   └── styles.css         # Styling
└── .deployment            # Azure build configuration
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12
- pip

### Local (venv)

```bash
# 1. Clone the repository
git clone https://github.com/Maulik290404/Cancer_detection_app.git
cd Cancer_detection_app

# 2. (Recommended) create a virtual environment
python -m venv .venv
# Windows:
.\.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py                  # dev server on http://127.0.0.1:5000
```

For a production-like run without Docker:

```bash
waitress-serve --host=127.0.0.1 --port=5000 app:app
```

### Docker

```bash
docker build -t skin-cancer-app .
docker run --rm -p 5000:5000 skin-cancer-app
```

Then open <http://127.0.0.1:5000>, upload a skin-lesion image, and click **Analyze Image**.

## 🔌 API Reference

### `GET /`
Renders the upload UI.

### `GET /health`
Liveness probe.

```json
{ "status": "ok" }
```

### `POST /predict`

Multipart form upload.

| Field | Type | Description |
|---|---|---|
| `image` | file (form-data) | The skin-lesion image to classify (any color mode — converted to RGB) |

**Success response — `200`**

```json
{
  "prediction": 1,
  "probability": 0.9873,
  "threshold": 0.5
}
```

- `prediction` — `1` if `probability > threshold` (malignant), else `0`.
- `probability` — raw sigmoid output in `[0, 1]`.
- `threshold` — the decision cutoff used (default `0.5`).

**Error responses**

| Status | Body |
|---|---|
| `400` | `{"error": "No file uploaded"}` |
| `400` | `{"error": "Empty file"}` |
| `400` | `{"error": "Uploaded file is not a valid image"}` |
| `413` | `{"error": "File exceeds 10 MB limit"}` |
| `500` | `{"error": "Inference failed"}` |

### Example

```bash
curl -X POST -F "image=@lesion.jpg" http://127.0.0.1:5000/predict
```

## ⚙️ Configuration

All settings are environment variables — sensible defaults are baked in.

| Variable | Default | Purpose |
|---|---|---|
| `MODEL_PATH` | `./built_model.keras` | Path to the Keras model file |
| `MAX_UPLOAD_MB` | `10` | Reject uploads larger than this |
| `ALLOWED_ORIGINS` | `*` | CORS `Access-Control-Allow-Origin` for `/predict` |
| `DECISION_THRESHOLD` | `0.5` | Probability cutoff for the "malignant" class |
| `PORT` | `5000` | Port for the dev server (`python app.py`) |
| `FLASK_DEBUG` | *unset* | Set to `1` to enable the Werkzeug debugger (dev only) |

## 🧪 Model

- **Input:** RGB image, resized to **512×512**, pixel values scaled to `[0, 1]`.
- **Output:** single sigmoid neuron — probability of the malignant class.
- **File:** `built_model.keras` (~54 MB) is tracked in git. For future
  iterations prefer Git LFS or an external artifact store — `*.keras` is
  already excluded by `.gitignore` so new checkpoints will not be committed
  by accident.

## 🛠️ Tech Stack

- **Backend:** Flask · Flask-CORS · TensorFlow / Keras · Pillow · NumPy · Waitress
- **Frontend:** HTML · CSS · JavaScript · animate.css
- **Deployment:** Docker · Azure App Service

## 👥 Team & Credits

Built by a team of 4 — covering CNN model development, the Flask API, the web
frontend, and cloud deployment.
