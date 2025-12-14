import re
from src.math_pipeline import solve_math
from src.llm_client import call_llm

MATH_PATTERN = re.compile(r"\\d+\\s*[+\\-*/]")

def route(question: str) -> str:
# simple heuristic routing
    if MATH_PATTERN.search(question):
        return solve_math(question)

    messages = [{"role": "user", "content": question}]
    result = call_llm(messages, model="small")
    return result["choices"][0]["message"]["content"]