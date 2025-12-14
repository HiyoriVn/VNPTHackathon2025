import requests
from src.config import ENDPOINTS, build_headers

def call_llm(messages, model="small", **params):
    """
    model: 'small' | 'large'
    messages: [{role, content}]
    """
    if model not in ("small", "large"):
        raise ValueError("model must be 'small' or 'large'")

    payload = {
        "model": f"vnptai_hackathon_{model}",
        "messages": messages,
        "temperature": params.get("temperature", 1.0),
        "top_p": params.get("top_p", 1.0),
        "top_k": params.get("top_k", 20),
        "n": params.get("n", 1),
        "max_completion_tokens": params.get("max_completion_tokens", 256),
    }


    resp = requests.post(
        ENDPOINTS[model],
        headers=build_headers(),
        json=payload,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()