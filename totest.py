from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Load the model
model = load_model("C:/Users/Maulik/Cancer_detection_app/Cancer_detection_app/cancer.keras")

# Function to test the model with an input image
def test_model(image_path):
    # Load and preprocess the image (resize to 224x224)
    img = Image.open(r"D:ML/archive/melanoma_cancer_dataset/train/malignant/melanoma_5019.jpg").resize((224, 224))  # Resize to match the model's input size
    img_array = np.array(img) / 255.0  # Normalize pixel values to [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Predict using the model
    prediction = model.predict(img_array)
    return "Cancer Detected" if prediction[0][0] > 0.5 else "No Cancer"

# Example usage
print(test_model(""))

