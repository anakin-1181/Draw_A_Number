---
title: Draw A Number
emoji: 🎨
colorFrom: purple
colorTo: pink
sdk: docker
app_file: Dockerfile
pinned: false
---

# Draw A Number (MNIST CNN Demo)

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/anakin-1181/Draw_A_Number)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-CNN-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)


This Hugging Face Space lets you draw a digit (0–9) on a canvas and the app predicts the number using a PyTorch CNN trained on MNIST.

**Model Training**: The CNN model was trained in the [machine-learning-notebook](https://github.com/anakin-1181/machine-learning-notebook) repository.

**Live Demo**: Try it out at [https://huggingface.co/spaces/anakin-1181/Draw_A_Number](https://huggingface.co/spaces/anakin-1181/Draw_A_Number)

The model weights are loaded from Hugging Face Hub using `hf_hub_download()` at runtime.

## Tech Stack
- Flask backend
- HTML/JS frontend canvas
- PyTorch CNN for digit classification
- Hugging Face Hub for model storage
- Docker for deployment on Spaces

## How it works
1. Draw a digit on the canvas  
2. The browser sends the PNG to the Flask backend  
3. The image is preprocessed (crop → center → resize 28×28)  
4. CNN predicts digit  
5. Result is shown instantly

Enjoy playing with your handwritten digit model!

