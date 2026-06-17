import requests
from dotenv import load_dotenv
import os

load_dotenv()

PAGE_ID = os.getenv("PAGE_ID")
TOKEN = os.getenv("PAGE_ACCESS_TOKEN")

with open("posts/post.txt", "r", encoding="utf-8") as f:
    message = f.read()

url = f"https://graph.facebook.com/{PAGE_ID}/feed"

data = {
    "message": message,
    "access_token": TOKEN
}

response = requests.post(url, data=data)

print(response.text)