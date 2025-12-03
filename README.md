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

This Hugging Face Space lets you draw a digit (0–9) on a canvas and the app predicts the number using a PyTorch CNN trained on MNIST. The model was trained in the machine-learning-notebook repository; this Space demonstrates a demo use case of that trained model.

The model weights are stored separately in a model repository and loaded with `hf_hub_download()` at runtime. Note: this Space is a demo that uses the model and training artifacts from the machine-learning-notebook repository.

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
