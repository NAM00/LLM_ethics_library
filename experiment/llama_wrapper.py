import os
import json
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer
import os
from prompt_wrapper import *
from prompts_json import *
from prompt_wrapper import PromptWrapper

from typing import List

def query(wrapped_prompt, MODEL_NAME) -> Response:
    messages = []
    responses = []
    try:
        safeguard = 5  # We never have more than 5 prompts
        count = 384
        prompt_tokens = 0
        completion_tokens = 0
        for item in wrapped_prompt[383:]:
            prompt = item.get_prompts()
            messages.append({"role": "system", "content": prompt})
            kwargs = {}
            # We add the the response_format either directly or in the second prompt where its asked to parse its ouput.

            pipeline = transformers.pipeline(
                "text-generation",
                model=MODEL_NAME,
                device_map="cuda"
            )
            outputs = pipeline(
                messages,
                max_new_tokens=1024,
            )
            response = outputs[0]["generated_text"][-1]["content"]
            print(response)
            print("row ------" + str(count))
            count = count + 1
            responses.append(response)
            with open("./test.jsonl", "a") as file:
                file.write(json.dumps(response) + "\n")

        with open("responses_2_from_383.json", "w", encoding="utf-8") as f:
            json.dump(responses, f, indent=2)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    file_path = "data/prompts/wrapped_prompts_v1.6.json"
    prompts = load_prompts_from_json(file_path)

    query(wrapped_prompt=prompts, MODEL_NAME="meta-llama/Llama-3.2-1B-Instruct")
