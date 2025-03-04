import os

from library.prompt_factory import get_all_possible_prompts, base_prompts
from library.prompt_wrapper import PromptWrapper
from library.prompts_json import generate_prompt_json
from library.version import VERSION


prompts_folder_path = os.path.join(os.path.dirname(__file__), "../data/prompts")

if __name__ == '__main__':
    # Generation forwrapped prompts - v1.6
    prompts_file_path = os.path.join(prompts_folder_path, f"wrapped_prompts_v{VERSION}.json")
    prompts = get_all_possible_prompts()
    # We found the base_prompt not to have a significant impact, so we willonly use base_prompt_1
    selected_base_prompt = next(iter(base_prompts))
    print(f"selected base prompt: {selected_base_prompt}")
    prompts: list[PromptWrapper] = [x for x in prompts if x.base_prompt_identifier == selected_base_prompt]
    prompts: list[PromptWrapper] = [x for x in prompts if x.dilemma.context_identifier in [
        "child_abuse_prevention",
        "public_health",
    ]]
    # Our current dilemmas do not include the LLM as a subject, thus the egoism framework is not applicable
    # TODO add later if cost allows it
    prompts: list[PromptWrapper] = [x for x in prompts if not x.framework_identifier == "ethical_egoism"]
    generate_prompt_json(prompts, prompts_file_path)
    print(f"generated {len(prompts)} prompts and saved them to {prompts_file_path}")
