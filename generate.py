# generate.py

from diffusers import StableDiffusionPipeline
import torch

# Load the model from Hugging Face
model_id = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    use_safetensors=True,
    low_cpu_mem_usage=True
)

# Optimize GPU memory usage
pipe.enable_model_cpu_offload()
pipe.enable_attention_slicing()

def generate_image(prompt, output_path=r"text2image/generate.png", steps=50, scale=9.0, seed=42):
    
    """
    Generates an image from a text prompt and saves it.

    Args:
        prompt (str): The text description of the image.
        output_path (str): Where to save the generated image.
        steps (int): Number of inference steps (more = better quality).
        scale (float): Classifier-free guidance scale (higher = more prompt-focused).
        seed (int): Random seed for reproducibility.

    Returns:
        str: Path to the saved image.
    """
    generator = torch.Generator("cuda").manual_seed(seed)

    image = pipe(
        prompt,
        num_inference_steps=steps,
        guidance_scale=scale,
        generator=generator
    ).images[0]

    image.save(output_path)

    # Free GPU memory
    torch.cuda.empty_cache()

    return output_path
