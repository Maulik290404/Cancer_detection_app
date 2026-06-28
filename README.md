🔬 Skin Cancer Detection Web App


A deep-learning web application that classifies skin-lesion images as benign or malignant using a CNN, served through a Flask backend with a clean, animated web interface.

Overview

Upload an image of a skin lesion and the app runs it through a trained Convolutional Neural Network to predict whether it appears benign or malignant, returning the result in real time. If the result is malignant, the UI surfaces a prompt to seek medical assistance immediately.

Built by a team of 4 as a full-stack ML project — covering model training, a REST prediction API, a responsive frontend, and cloud deployment.


⚠️ Medical disclaimer: This project is for educational and research purposes only. It is not a medical device and must not be used for actual diagnosis. Always consult a qualified healthcare professional.




✨ Features


Image-based classification — binary benign vs. malignant prediction from a skin-lesion photo.
REST prediction API — a /predict endpoint that accepts an image and returns a JSON result.
Responsive web UI — drag-and-drop style upload, live image preview, and animated feedback (animate.css).
Real-time inference — preprocessing (resize to 512×512, normalize) and prediction happen on upload.
Cloud-ready — configured for deployment to Azure App Service.



🧠 How It Works

Browser (upload image)
        │  POST /predict  (multipart form-data)
        ▼
Flask app  ─►  preprocess (resize 512×512, normalize 0–1)
        │
        ▼
Keras CNN (built_model.keras)  ─►  sigmoid output
        │
        ▼
prediction > 0.5 ?  →  1 = Malignant  /  0 = Benign
        │
        ▼
JSON response  ─►  rendered in the UI


📁 Project Structure

Cancer_detection_app/
├── app.py                 # Flask server + /predict API + model inference
├── built_model.keras      # Trained CNN model
├── requirements.txt
├── templates/
│   └── index.html         # Frontend page (upload form + result area)
├── static/
│   ├── script.js          # Handles upload, preview, fetch to /predict
│   └── styles.css         # Styling
└── .deployment            # Azure build configuration


🚀 Getting Started

Prerequisites


Python 3.10+
pip


Installation

bash# 1. Clone the repository
git clone https://github.com/Maulik290404/Cancer_detection_app.git
cd Cancer_detection_app

# 2. (Recommended) create a virtual environment
python -m venv venv
# Windows:
.\venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py

Then open http://localhost:5000 in your browser, upload a skin-lesion image, and click Detect Cancer.


🔌 API Reference

POST /predict

FieldTypeDescriptionimagefile (form-data)The skin-lesion image to classify

Success response

json{ "prediction": 1 }   // 1 = malignant, 0 = benign

Error response

json{ "error": "No file uploaded" }


🛠️ Tech Stack

Backend: Flask · Flask-CORS · TensorFlow / Keras · Pillow · NumPy
Frontend: HTML · CSS · JavaScript · animate.css
Deployment: Azure App Service


👥 Team & Credits

Built by a team of 4 — covering CNN model development, the Flask API, the web frontend, and cloud deployment.
