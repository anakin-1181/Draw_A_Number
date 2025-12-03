from flask import Flask, request, jsonify, render_template
from PIL import Image, ImageOps
import io
import torch
import torchvision.transforms as transforms
import numpy as np
from model_def import clsModel   
from huggingface_hub import hf_hub_download


app = Flask(__name__)

device = torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")

# Load model
model = clsModel().to(device)

# Download the model file from your HF model repo
model_path = hf_hub_download(
    repo_id="anakin-1181/draw-a-number-cnn",  
    filename="mnist_cnn.pt"
)

state_dict = torch.load(model_path, map_location=device)
model.load_state_dict(state_dict)
model.eval()



def preprocess_canvas_image(pil_img):
    img = pil_img.convert("L")
    img = img.resize((28, 28), Image.BILINEAR)

    arr = np.array(img)
    thresh = 10 # crop the image to where the digit locates
    ys, xs = np.where(arr > thresh)

    if len(xs) == 0:  
        return transforms.ToTensor()(img)

    x_min, x_max = xs.min(), xs.max()
    y_min, y_max = ys.min(), ys.max()

    cropped = img.crop((x_min, y_min, x_max + 1, y_max + 1))
    cropped = cropped.resize((20, 20), Image.BILINEAR)
    
    canvas = Image.new("L", (28, 28), color=0)  
    upper_left = (4, 4)  
    canvas.paste(cropped, upper_left)
    
    tensor = transforms.ToTensor()(canvas)
    return tensor


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "no file"}), 400

    file = request.files["file"]

    pil_img = Image.open(file)

    # preprocess_canvas_image returns a tensor (1, 28, 28) in [0,1]
    img_tensor = preprocess_canvas_image(pil_img)   # (1, 28, 28)
    img_tensor = img_tensor.unsqueeze(0).to(device) # (1, 1, 28, 28)

    with torch.no_grad():
        logits = model(img_tensor)
        pred = logits.argmax(dim=1).item()

    return jsonify({"prediction": int(pred)})


if __name__ == "__main__":
    app.run(debug=True)
