# Skin Cancer Detection

A Flask + TensorFlow web app that classifies skin-lesion images as **benign** or
**malignant** using a Keras CNN. Users upload a photo through a simple web UI
and receive a class label plus the model's confidence.

> **Disclaimer — not a medical device.** This project is for educational and
> research purposes only. Predictions can be wrong. Always consult a licensed
> dermatologist for concerns about a skin lesion.

## Features

- Web UI with image preview and confidence display
- REST endpoint (`POST /predict`) returning JSON
- Health check (`GET /health`) for container orchestration
- Robust input handling — accepts JPEG / PNG / RGBA / grayscale
- Upload size limit (default 10 MB), configurable via env var
- Runs as a non-root user under `waitress` in the Docker image

## Project layout

```
.
├── app.py                # Flask app — routes and inference pipeline
├── built_model.keras     # Trained Keras model (input 512x512x3, sigmoid output)
├── requirements.txt      # Pinned Python dependencies
├── Dockerfile            # Production container (waitress WSGI)
├── .dockerignore
├── templates/
│   └── index.html        # Upload UI
└── static/
    ├── Designer.jpeg     # Header illustration
    ├── script.js         # Upload + result rendering
    └── styles.css
```

## Quick start

### Local (venv)

```bash
python -m venv .venv
.venv/Scripts/activate         # Windows
# source .venv/bin/activate    # macOS / Linux
pip install -r requirements.txt
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

Then open <http://127.0.0.1:5000>.

## API

### `GET /`
Renders the upload UI.

### `GET /health`
Liveness probe.

```json
{ "status": "ok" }
```

### `POST /predict`
Multipart form upload.

**Request**
- `image` — image file (JPEG / PNG). Any color mode is converted to RGB.

**Response — 200**
```json
{
  "prediction": 1,
  "probability": 0.9873,
  "threshold": 0.5
}
```

- `prediction` — `1` if `probability > threshold` (malignant), else `0`.
- `probability` — raw sigmoid output from the model in `[0, 1]`.
- `threshold` — decision threshold used (default `0.5`).

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

## Configuration

All settings are environment variables — sensible defaults are baked in.

| Variable | Default | Purpose |
|---|---|---|
| `MODEL_PATH` | `./built_model.keras` | Path to the Keras model file |
| `MAX_UPLOAD_MB` | `10` | Reject uploads larger than this |
| `ALLOWED_ORIGINS` | `*` | CORS `Access-Control-Allow-Origin` for `/predict` |
| `DECISION_THRESHOLD` | `0.5` | Probability cutoff for the "malignant" class |
| `PORT` | `5000` | Port for the dev server (`python app.py`) |
| `FLASK_DEBUG` | *unset* | Set to `1` to enable the Werkzeug debugger (dev only) |

## Model

- Input: RGB image, resized to **512×512**, pixel values scaled to `[0, 1]`.
- Output: single sigmoid neuron — probability of the malignant class.
- File: `built_model.keras` (~54 MB) is tracked in git. For future iterations
  prefer Git LFS or an external artifact store — `*.keras` is already excluded
  by `.gitignore` so new checkpoints will not be committed by accident.

## Tech stack

- Python 3.12
- Flask 3, Flask-CORS
- TensorFlow / Keras 2.16
- Pillow for image loading
- Waitress for production serving
- Vanilla HTML / CSS / JS on the frontend (no build step)

## License

No license specified — treat this as source-available research code and do
not use it for clinical decisions.
