from src.llm_client import call_llm

if __name__ == "__main__":
    print(
        call_llm(
            [{"role": "user", "content": "Việt Nam có bao nhiêu tỉnh thành?"}],
            model="small",
        )
    )