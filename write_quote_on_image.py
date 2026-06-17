from PIL import Image, ImageDraw, ImageFont
import textwrap

# Open image
img = Image.open("images/generated.png")

# Draw object
draw = ImageDraw.Draw(img)

# Read quote
with open("posts/post.txt", "r", encoding="utf-8") as f:
    quote = f.read()

# Hindi Font
font = ImageFont.truetype(
    "fonts/NotoSansDevanagari-VariableFont_wdth,wght.ttf",
    32
)

# Branding Font
brand_font = ImageFont.truetype(
    "fonts/NotoSansDevanagari-VariableFont_wdth,wght.ttf",
    22
)

# Image size
width, height = img.size

# Quote ko wrap karo
quote = "\n".join(
    textwrap.wrap(
        quote[:180],
        width=22
    )
)

# Bottom black box
overlay_height = 180

draw.rectangle(
    [(0, height-overlay_height), (width, height)],
    fill=(0, 0, 0)
)

# Quote text
draw.text(
    (20, height-overlay_height+15),
    quote,
    fill="white",
    font=font
)

# Branding
draw.text(
    (20, height-35),
    "Sanatan Vani",
    fill="gold",
    font=brand_font
)

# Save image
img.save("images/final_post.png")

print("Final image saved!")