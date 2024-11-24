document.getElementById("uploadForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const imageInput = document.getElementById("imageInput");
    const resultDiv = document.getElementById("result");

    if (imageInput.files.length === 0) {
        resultDiv.textContent = "Please upload an image.";
        return;
    }

    const formData = new FormData();
    formData.append("image", imageInput.files[0]);

    resultDiv.textContent = "Processing...";

    try {
        const response = await fetch("https://<your-backend-endpoint>/predict", {
            method: "POST",
            body: formData,
        });

        if (!response.ok) {
            throw new Error("Failed to get prediction");
        }

        const data = await response.json();
        const prediction = data.prediction === 1 ? "Cancer Detected" : "No Cancer Detected";
        resultDiv.textContent = `Result: ${prediction}`;
    } catch (error) {
        resultDiv.textContent = `Error: ${error.message}`;
    }
});
