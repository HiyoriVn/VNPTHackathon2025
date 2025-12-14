import requests
from src.config import ENDPOINTS, build_headers

def embed(text: str):
    payload = {
        "model": "vnptai_hackathon_embedding",
        "input": text,
        "encoding_format": "float",
    }

    resp = requests.post(
        ENDPOINTS["embedding"],
        headers=build_headers(),
        json=payload,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["data"][0]["embedding"]