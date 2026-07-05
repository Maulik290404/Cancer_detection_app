# Use the official Python 3.12 image
FROM python:3.12-slim

# Ensure Python output is unbuffered and no .pyc files clutter the image
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=5000

WORKDIR /app

# Install dependencies first so the layer caches across code edits
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app

# Drop root
RUN useradd --create-home --uid 1000 appuser \
    && chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

# Serve via waitress (production WSGI) instead of the Flask dev server
CMD ["waitress-serve", "--host=0.0.0.0", "--port=5000", "app:app"]
