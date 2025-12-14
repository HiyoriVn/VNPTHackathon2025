import os

VNPT_BASE = "https://api.idg.vnpt.vn"

ENDPOINTS = {
"small": f"{VNPT_BASE}/data-service/v1/chat/completions/vnptai-hackathon-small",
"large": f"{VNPT_BASE}/data-service/v1/chat/completions/vnptai-hackathon-large",
"embedding": f"{VNPT_BASE}/data-service/vnptai-hackathon-embedding",
}

# Read from ENV for security
ACCESS_TOKEN = os.getenv("VNPT_ACCESS_TOKEN")
TOKEN_ID = os.getenv("VNPT_TOKEN_ID")
TOKEN_KEY = os.getenv("VNPT_TOKEN_KEY")

def build_headers():
    if not all([ACCESS_TOKEN, TOKEN_ID, TOKEN_KEY]):
        raise RuntimeError("Missing VNPT credentials in environment variables")

    return {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Token-id": TOKEN_ID,
        "Token-key": TOKEN_KEY,
        "Content-Type": "application/json",
    }