prompt = """
Sanatan Vani Facebook Page ke liye post likho.

Topic: Bhagavad Gita

Rules:
- Hindi language
- 80-120 words
- Motivational tone
- Sanskrit shlok include karo
- 8 viral hashtags do
- Emoji use karo
- Facebook audience ke liye engaging banao
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "gemma3:4b",
        "prompt": prompt,
        "stream": False
    }
)

post_text = response.json()["response"]

with open("posts/post.txt", "w", encoding="utf-8") as f:
    f.write(post_text)

print(post_text)
