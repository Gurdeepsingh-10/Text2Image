# 🖼️ Text-to-Image Generator (Stable Diffusion + Flask)

Turn your words into stunning AI-generated visuals. A lightweight Flask app using Hugging Face’s Stable Diffusion, optimized for GPU (e.g. RTX 3050) and styled with a retro UI.

## 🚀 Features

- Text prompt to image generation  
- GPU-accelerated with FP16 inference  
- Retro-style frontend  
- Simple Flask backend  
- Powered by `diffusers` + Hugging Face  

## 🖥️ Tech Stack

- Python 3.10+  
- Flask  
- Diffusers (`runwayml/stable-diffusion-v1-5`)  
- Torch (CUDA enabled)  
- HTML/CSS  

## 📦 Installation

```bash
git clone https://github.com/your-username/text2image-flask.git
cd text2image-flask
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## 🧪 Run Locally

```bash
python app.py
```

Open `http://localhost:5000` in your browser.

## 📁 Project Structure

```
text2image-flask/
├── app.py
├── generate.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── generated.png
└── requirements.txt
```
