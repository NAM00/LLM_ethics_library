import json
from library.prompt_wrapper import PromptWrapper


def generate_prompt_json(prompts: list[PromptWrapper], path: str):
    prompt_dicts = [prompt.to_dict() for prompt in prompts]
    with open(path, 'w') as f:
        json.dump(prompt_dicts, f, indent=4)

    print("Prompts successfully written to 'wrapped_prompts.json'")


def load_prompts_from_json(path: str):
    """
    Load a list of PromptWrapper objects from a JSON file.
    """
    with open(path, 'r') as f:
        data = json.load(f)

    # Convert each dictionary back into a PromptWrapper object
    return [PromptWrapper.from_dict(item) for item in data]
