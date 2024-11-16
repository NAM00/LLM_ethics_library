import openai
import os

def test_openai_api(api_key: str):
    openai.api_key = api_key
    try:
        response = openai.chat.completions.create(
            model = "gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Hello World"}
            ],
            max_tokens=5
        )
        return response
    except Exception as e:
        return f"An error occurred: {e}"
