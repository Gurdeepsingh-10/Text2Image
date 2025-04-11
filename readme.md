🖼️ Text-to-Image Generator (Stable Diffusion + Flask)
Turn your words into stunning AI-generated visuals! This project is a lightweight Flask web app that uses 🤗 Hugging Face's Stable Diffusion models to generate images from text prompts — optimized for GPU use (e.g., NVIDIA RTX 3050) and styled with a retro-themed UI.

🚀 Features
🧠 Text prompt → AI-generated image

⚡ GPU-accelerated (torch + FP16 inference)

🎨 Retro-style web interface

🪶 Lightweight, responsive, and easy to use

🔌 Powered by diffusers and Hugging Face Hub

🖥️ Tech Stack
Python 3.10+

Flask

Diffusers (runwayml/stable-diffusion-v1-5)

Torch (CUDA + FP16 enabled)

HTML/CSS (Retro UI)

📦 Installation
bash
Copy
Edit
git clone https://github.com/your-username/text2image-flask.git
cd text2image-flask
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
🧪 Run Locally
bash
Copy
Edit
python app.py
Visit http://localhost:5000 in your browser and start generating!

📁 Project Structure
csharp
Copy
Edit
text2image-flask/
├── app.py             # Flask server
├── generate.py        # Stable Diffusion pipeline
├── templates/
│   └── index.html     # Web interface
├── static/
│   └── style.css      # Retro UI styling
├── static/generated.png  # Output image (auto-overwritten)
└── requirements.txt
📸 Demo
Add screenshot here if you want

🧠 Prompt Example
arduino
Copy
Edit
"A futuristic cyberpunk city with neon lights and flying cars"
💡 Future Ideas
🗂️ Save past generations

⬇️ Download button for images

📦 Deploy on Hugging Face Spaces or Render

🧩 Add API endpoint support

🛡️ License
MIT License © YourName