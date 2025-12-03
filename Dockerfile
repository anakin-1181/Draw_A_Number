FROM python:3.10-slim

# System deps for numpy/pillow
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy project
COPY . /app

# Install normal Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Install PyTorch CPU wheels explicitly from the official index
RUN pip install --no-cache-dir \
    torch==2.2.2 \
    torchvision==0.17.2 \
    --index-url https://download.pytorch.org/whl/cpu

# HF Spaces expects port 7860
ENV PORT=7860
ENV PYTHONUNBUFFERED=1

EXPOSE 7860

# app.py must define `app = Flask(__name__)`
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]
