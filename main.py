from typing import Any
from fastapi import FastAPI, Depends, HTTPException, Header
import ollama
import os
from dotenv import load_dotenv

load_dotenv()

API_KEYS_CREDITS: dict[str | None, int] = {
    os.getenv(key="API_KEY"): 5
}  # number of credits for each API key

app = FastAPI()


def verify_api_key(x_api_key: str = Header(default=None)):
    credits: int = API_KEYS_CREDITS.get(x_api_key, 0)
    if credits <= 0:
        raise HTTPException(
            status_code=401, detail="Invalid API key, or no credits left"
        )

    return x_api_key


@app.post(path="/generate")
def generate(prompt: str, x_api_key: str = Depends(dependency=verify_api_key)) -> dict[str, Any]:
    API_KEYS_CREDITS[x_api_key] -= 1
    response: ollama.ChatResponse = ollama.chat(
        model="mistral", messages=[{"role": "user", "content": prompt}]
    )
    return {"response": response["message"]["content"]}
