import requests
from dotenv import load_dotenv
import os

load_dotenv()

PAGE_ID = os.getenv("PAGE_ID")
TOKEN = os.getenv("PAGE_ACCESS_TOKEN")

with open("images/final_post.png", "rb"):
    caption = f.read()

url = f"https://graph.facebook.com/{PAGE_ID}/photos"

files = {
    "source": open("images/krishna.jpg", "rb")
}

data = {
    "caption": caption,
    "access_token": TOKEN
}

response = requests.post(url, files=files, data=data)

print(response.text)