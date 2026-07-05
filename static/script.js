const form = document.getElementById("uploadForm");
const imageInput = document.getElementById("imageInput");
const resultDiv = document.getElementById("result");
const previewDiv = document.getElementById("preview");
const submitBtn = form.querySelector("button[type=submit]");

imageInput.addEventListener("change", () => {
    previewDiv.innerHTML = "";
    resultDiv.textContent = "";
    resultDiv.className = "result";

    const file = imageInput.files[0];
    if (!file) return;

    const img = document.createElement("img");
    img.src = URL.createObjectURL(file);
    img.alt = "Uploaded image preview";
    img.className = "preview-image";
    img.onload = () => URL.revokeObjectURL(img.src);
    previewDiv.appendChild(img);
});

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    resultDiv.className = "result";
    resultDiv.textContent = "";

    if (!imageInput.files.length) {
        resultDiv.textContent = "Please select an image first.";
        resultDiv.className = "result animate__animated animate__shakeX";
        return;
    }

    const formData = new FormData();
    formData.append("image", imageInput.files[0]);

    submitBtn.disabled = true;
    resultDiv.textContent = "Analyzing…";
    resultDiv.className = "result";

    try {
        const response = await fetch(window.location.origin + "/predict", {
            method: "POST",
            body: formData,
        });

        const data = await response.json().catch(() => ({}));

        if (!response.ok) {
            throw new Error(data.error || response.statusText || "Request failed");
        }

        renderResult(data);
    } catch (error) {
        resultDiv.textContent = `Error: ${error.message}`;
        resultDiv.className = "result animate__animated animate__shakeX";
    } finally {
        submitBtn.disabled = false;
    }
});

function renderResult(data) {
    const isMalignant = data.prediction === 1;
    const probability = typeof data.probability === "number" ? data.probability : null;
    const shownProb = isMalignant ? probability : (probability !== null ? 1 - probability : null);

    resultDiv.innerHTML = "";
    resultDiv.className = "result animate__animated animate__fadeIn";

    const label = document.createElement("div");
    label.className = "result-label";
    label.textContent = isMalignant
        ? "Higher-risk features detected"
        : "No higher-risk features detected";
    resultDiv.appendChild(label);

    if (shownProb !== null) {
        const conf = document.createElement("div");
        conf.className = "confidence-rate";
        conf.textContent = `Model confidence: ${(shownProb * 100).toFixed(1)}%`;
        resultDiv.appendChild(conf);
    }

    if (isMalignant) {
        const advice = document.createElement("div");
        advice.className = "assistance-message";
        advice.textContent =
            "This screening suggests you should consult a dermatologist. This is not a diagnosis.";
        resultDiv.appendChild(advice);
    }
}
