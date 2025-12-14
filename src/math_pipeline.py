from src.llm_client import call_llm

def solve_math(question: str) -> str:
    messages = [
        {"role": "system", "content": "Bạn là trợ lý giải toán chính xác."},
        {"role": "user", "content": question},
]

    result = call_llm(messages, model="large")
    return result["choices"][0]["message"]["content"]