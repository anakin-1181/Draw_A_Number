# --- Base image ---
# Python-slim is lightweight but still supports PyTorch CPU wheels.
FROM python:3.10-slim

# --- System dependencies ---
# These are needed for numpy, pillow and general scientific libs.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# --- Working directory ---
WORKDIR /app

# --- Copy project files ---
COPY . /app

# --- Install Python dependencies ---
# Requirements must exist in the repo.
RUN pip install --no-cache-dir -r requirements.txt

# --- Set environment variables ---
# Hugging Face Spaces expect apps to listen on 7860.
ENV PORT=7860
ENV PYTHONUNBUFFERED=1

# --- Expose port ---
EXPOSE 7860

# --- Launch server ---
# Use gunicorn in production. "app:app" = app.py contains Flask instance "app"
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]
