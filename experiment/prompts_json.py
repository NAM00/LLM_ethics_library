import json

from experiment.prompt_wrapper import PromptWrapper, Response, OutputStructure
from version import VERSION
from typing import List


def generate_prompt_json(prompts: List[PromptWrapper], path: str):
    prompt_dicts = [prompt.to_dict() for prompt in prompts]
    with open(path, 'w') as f:
        json.dump(prompt_dicts, f, indent=4)

    print(f"{len(prompts)} rompts successfully written to {path}")


def load_prompts_from_json(path: str):
    """
    Load a List of PromptWrapper objects from a JSON file.
    """
    obj = []

    with open(path, 'r') as f:
        data = json.load(f)

    for item in data:
        print(item)
        res = PromptWrapper(prompts=item["prompts"],
                            dilemma_identifier=item["dilemma_identifier"],
                            ethical_framework_identifier=item["ethical_framework_identifier"],
                            base_prompt_identifier=item["base_prompt_identifier"],
                            prompt_has_output_structure_description=item["prompt_has_output_structure_description"],
                            prompt_has_output_structure_json_schema=item["prompt_has_output_structure_json_schema"],
                            output_structure=OutputStructure.from_dict(
                                item["output_structure"]),
                            version=item["version"],
                            )
        obj.append(res)


    # Convert each dictionary back into a PromptWrapper object
    return obj


def generate_response_json(responses: List[Response], path: str, logging: bool = True):
    response_dicts = [response.to_dict() for response in responses]
    with open(path, 'w') as f:
        json.dump(response_dicts, f, indent=4)

    if logging:
        print(f"Responses successfully written to {path}")


def load_responses_from_json(path: str):
    with open(path, 'r') as f:
        data = json.load(f)

    # Convert each dictionary back into a Response object
    res = [Response.from_dict(item) for item in data]

    if not res[0].wrapped_prompt.version == VERSION:
        print("Warning: The version of the loaded responses does not match the current library version.")
    return res
