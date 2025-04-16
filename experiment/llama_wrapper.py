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
        count = 0
        prompt_tokens = 0
        completion_tokens = 0
        for item in wrapped_prompt:
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
            response = outputs[0]["generated_text"]
            print(response)
            with open("./test.jsonl", "a") as file:
                file.write(json.dumps(response) + "\n")


            prompt_tokens += response.usage.prompt_tokens
            completion_tokens += response.usage.completion_tokens

        parsed_response = json.loads(responses[-1])
        if not parsed_response.get("decision"):
            raise Exception("No decision in response")

        decision = DecisionOption(parsed_response["decision"])

        return Response(
            wrapped_prompt=wrapped_prompt,
            decision=decision,
            llm_identifier=MODEL_NAME,
            unparsed_messages=[LlmMessage.from_dict(item) for item in messages],
            parsed_response=parsed_response,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
        )
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    file_path = "data/prompts/wrapped_prompts_v1.6.json"
    prompts = load_prompts_from_json(file_path)

    query(wrapped_prompt=prompts, MODEL_NAME="meta-llama/Llama-3.2-1B-Instruct")
