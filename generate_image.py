from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float32
)

prompt =   """
Lord Krishna sitting under a large tree beside a river,
playing flute,
beautiful peacock nearby,
golden sunset lighting,
spiritual atmosphere,
Indian devotional art,
facebook motivational poster,
left side dark empty space for quote text,
right side Krishna portrait,
cinematic lighting,
ultra detailed,
high quality,
1080x1080 social media poster,
professional composition,
warm golden glow,
masterpiece
"""

image = pipe(prompt).images[0]

image.save("images/generated.png")

print("Image Saved!")