import requests

prompt = """
Bhagavad Gita se ek motivational quote likho.

Hindi language.

Maximum 4 lines.

Simple language.

End me:
जय श्रीकृष्ण 🙏
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "gemma3:4b",
        "prompt": prompt,
        "stream": False
    }
)

quote = response.json()["response"]

with open("posts/quote.txt", "w", encoding="utf-8") as f:
    f.write(quote)

print(quote)