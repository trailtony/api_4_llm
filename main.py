from typing import Any
from fastapi import FastAPI, Depends, HTTPException, Header
import ollama
import os
from dotenv import load_dotenv

load_dotenv()

API_KEYS = {os.getenv("API_KEY"): 5}

app = FastAPI()


@app.post(path="/generate")
def generate(prompt: str) -> dict[str, Any]:
    response: ollama.ChatResponse = ollama.chat(
        model="mistral", messages=[{"role": "user", "content": prompt}]
    )
    return {"response": response["message"]}
