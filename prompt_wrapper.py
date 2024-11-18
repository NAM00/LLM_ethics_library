from enum import Enum
import json


class DecisionOption(Enum):
    YES = "YES"
    NO = "NO"
    UNDECIDED = "UNDECIDED"


ALL_DECISION_OPTIONS = [DecisionOption.YES,
                        DecisionOption.NO, DecisionOption.UNDECIDED]


class OutputComponentType(Enum):
    DECISION = "DECISION"
    FRAMEWORK_EXPLANATION = "FRAMEWORK_EXPLANATION"
    DECISION_REASON = "DECISION_REASON"


class OutputStructure:
    def __init__(self, sorted_output_components: list[OutputComponentType], sorted_decision_options: list[DecisionOption], first_unstructred_output: bool):
        self.sorted_output_components = sorted_output_components
        self.sorted_decision_options = sorted_decision_options
        self.first_unstructred_output = first_unstructred_output

    def to_dict(self):
        return {
            "sorted_output_components": [component.value for component in self.sorted_output_components],
            "sorted_decision_options": [option.value for option in self.sorted_decision_options],
            "first_unstructred_output": self.first_unstructred_output,
        }


class PromptWrapper:
    def __init__(
        self,
        prompts: list[str],
        dilemma_identifier: str,
        framework_identifier: str,
        output_structure: OutputStructure,
        version: str,
    ):
        self.prompts = prompts
        self.dilemma_identifier = dilemma_identifier
        self.framework_identifier = framework_identifier
        self.output_structure = output_structure
        self.version = version

    def __str__(self):
        str = "--------PromptWrapper--------"
        for prompt in self.prompts:
            str += f"\nprompt:\n{prompt}"
        str += "-----------------------------"
        return str

    def to_dict(self):
        return {
            "prompts": self.prompts,
            "dilemma_identifier": self.dilemma_identifier,
            "framework_identifier": self.framework_identifier,
            "output_structure": self.output_structure.to_dict(),
            "version": self.version,
        }


class Response:
    def __init__(self, prompt: PromptWrapper, decision: DecisionOption):
        self.prompt = prompt
        self.decision = decision

    def to_dict(self):
        return {
            "prompt": self.prompt.to_dict(),
            "decision": self.decision.value,
        }
