import requests

prompt = """
Bhagavad Gita motivational Facebook post ke liye
ek detailed AI image prompt likho.

Image:
- Lord Krishna
- Kurukshetra battlefield
- Divine light
- Realistic
- 4K
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "gemma3:4b",
        "prompt": prompt,
        "stream": False
    }
)

image_prompt = response.json()["response"]

with open("posts/image_prompt.txt", "w", encoding="utf-8") as f:
    f.write(image_prompt)

print(image_prompt)