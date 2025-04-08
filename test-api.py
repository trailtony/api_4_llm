import requests
from dotenv import load_dotenv
import os

load_dotenv()

url: str = "http://localhost:8000/generate?prompt=Tell me about Python"
headers: dict = {
    "x-api-key": os.getenv("API_KEY"),
    "Content-Type": "application/json",
}

response = requests.post(url=url, headers=headers)
print(response.json())
