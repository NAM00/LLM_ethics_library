import os
import openai
from library.prompt_wrapper import *



def test_openai_api(api_key: str):
    openai.api_key = api_key
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Hello World"}
            ],
            max_tokens=5
        )
        print("WORKED")
        return response
    except Exception as e:
        return f"An error occurred: {e}"


def query_openai_api(api_key: str, wrapped_prompt: PromptWrapper) -> Response:
    openai.api_key = api_key

    messages = []
    responses = []
    safeguard = 5 # We never have more than 5 prompts
    count = 0
    for prompt in wrapped_prompt.prompts:
        if count >= safeguard:
            break
        count += 1

        messages.append({"role": "system", "content": prompt})
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                max_tokens=100
            )

            if len(response.choices) == 0:
                raise Exception("No response from OpenAI API")
            response_str = response.choices[0].message.content
            messages.append(
                {"role": "assistant", "content": response_str})
            responses.append(response_str)
        except Exception as e:
            print(f"An error occurred: {e}")
            raise e

    return responses


if __name__ == '__main__':
    api_key = os.getenv("ETHICS_OPENAI_API_KEY")
    response = test_openai_api(api_key)
