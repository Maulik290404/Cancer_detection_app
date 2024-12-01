document.getElementById("uploadForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const imageInput = document.getElementById("imageInput");
    const resultDiv = document.getElementById("result");
    const previewDiv = document.getElementById("preview");

    resultDiv.className = "result";
    resultDiv.textContent = "";
    previewDiv.innerHTML = "";

    if (imageInput.files.length === 0) {
        resultDiv.textContent = "Please upload an image.";
        resultDiv.className = "result animate__animated animate__shakeX";
        return;
    }

    const file = imageInput.files[0];
    const reader = new FileReader();
    reader.onload = function (e) {
        const img = document.createElement("img");
        img.src = e.target.result;
        img.alt = "Uploaded Image Preview";
        img.className = "preview-image";
        previewDiv.appendChild(img);
    };
    reader.readAsDataURL(file);

    const formData = new FormData();
    formData.append("image", file);

    resultDiv.textContent = "Processing...";
    resultDiv.className = "result animate__animated animate__flash";

    try {
        const backendURL = window.location.origin + "/predict";

        const response = await fetch(backendURL, {
            method: "POST",
            body: formData,
        });

        if (!response.ok) {
            const errorMessage = await response.text();
            throw new Error(`Server Error: ${errorMessage || response.statusText}`);
        }

        const data = await response.json();
        const isMalignant = data.prediction === 1;
        const prediction = isMalignant ? "Malignant (Cancer Detected)" : "Benign (No Cancer Detected)";
        resultDiv.textContent = `Result: ${prediction}`;
        resultDiv.className = "result animate__animated animate__fadeIn";

        if (isMalignant) {
            const assistanceMessage = document.createElement("div");
            assistanceMessage.textContent = "Get assistance immediately!";
            assistanceMessage.className = "assistance-message animate__animated animate__flash";
            resultDiv.appendChild(assistanceMessage);
        }
    } catch (error) {
        resultDiv.textContent = `Error: ${error.message}`;
        resultDiv.className = "result animate__animated animate__shakeX";
    }
});
