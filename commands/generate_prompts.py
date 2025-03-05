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

    # Selected dilemmas
    prompts: list[PromptWrapper] = [x for x in prompts if x.dilemma.context_identifier in [
        "child_abuse_prevention",
        "public_health",
    ]]

    # We found the base_prompt not to have a significant impact, so we will only use base_prompt_1
    selected_base_prompt = next(iter(base_prompts))
    prompts: list[PromptWrapper] = [x for x in prompts if x.base_prompt_identifier == selected_base_prompt]

    # Our current dilemmas do not include the LLM as a subject, thus the egoism theory might not applicable
    # prompts: list[PromptWrapper] = [x for x in prompts if not x.normative_ethical_theory == "ethical_egoism"]

    # This is a newly added variable we do not yet want to test
    # Previously the prompt always containted the output structure json and description
    prompts: list[PromptWrapper] = [x for x in prompts if not x.prompt_has_output_structure_description is True]
    prompts: list[PromptWrapper] = [x for x in prompts if not x.prompt_has_output_structure_json_schema is True]
    generate_prompt_json(prompts, prompts_file_path)
    print(f"generated {len(prompts)} prompts and saved them to {prompts_file_path}")
