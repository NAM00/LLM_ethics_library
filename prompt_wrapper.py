from typing import Dict, Type
from pydantic import BaseModel, create_model

from enum import Enum


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


def create_response_class(fields: Dict[str, Type]):
    return create_model('DynamicResponse', **{score: (score_type, ...) for score, score_type in fields.items()})


class OutputStructure:
    def __init__(self, sorted_output_components: list[OutputComponentType], sorted_decision_options: list[DecisionOption], first_unstructred_output: bool):
        self.sorted_output_components = sorted_output_components
        self.sorted_decision_options = sorted_decision_options
        self.first_unstructred_output = first_unstructred_output

    def get_json_schema(self) -> object:
        """
        Get the OpenAI structured output schema for the current OutputStructure object.
        """

        sorted_output_components_schema = {}
        for output_component in self.sorted_output_components:
            if output_component == OutputComponentType.DECISION:
                output_component_schema = {
                    "type": "string",
                    "description": "The decision options",
                    "enum": [item.value for item in self.sorted_decision_options]
                }

            else:
                output_component_schema = {
                    "type": "string",
                    "description": f"The {output_component.value.lower()} content"
                }
            sorted_output_components_schema[output_component.value.lower(
            )] = output_component_schema

        json_schema = {
            "type": "object",
            "properties": sorted_output_components_schema,
            "additionalProperties": False,
            "required": [component.value.lower() for component in self.sorted_output_components],
        }
        return json_schema

    def to_dict(self):
        return {
            "sorted_output_components": [component.value for component in self.sorted_output_components],
            "sorted_decision_options": [option.value for option in self.sorted_decision_options],
            "first_unstructred_output": self.first_unstructred_output,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Create an OutputStructure object from a dictionary.
        """
        return cls(
            sorted_output_components=[OutputComponentType(
                component) for component in data["sorted_output_components"]],
            sorted_decision_options=[DecisionOption(
                option) for option in data["sorted_decision_options"]],
            first_unstructred_output=data["first_unstructred_output"],
        )


class PromptWrapper:
    def add_id(self, id: int):
        self.id = id

    def __init__(
        self,
        prompts: list[str],
        dilemma_identifier: str,
        framework_identifier: str,
        base_prompt_identifier: str,
        output_structure: OutputStructure,
        version: str,
    ):
        self.id = None
        self.prompts = prompts
        self.dilemma_identifier = dilemma_identifier
        self.framework_identifier = framework_identifier
        self.base_prompt_identifier = base_prompt_identifier
        self.output_structure = output_structure
        self.version = version

    def __str__(self):
        str = "--------PromptWrapper--------"
        for prompt in self.prompts:
            str += f"\nprompt:\n{prompt}"
        str += "-----------------------------"
        return str

    def to_dict(self):
        if self.id is None:
            raise Exception("PromptWrapper ID is None")
        return {
            "id": self.id,
            "prompts": self.prompts,
            "dilemma_identifier": self.dilemma_identifier,
            "framework_identifier": self.framework_identifier,
            "base_prompt_identifier": self.base_prompt_identifier,
            "output_structure": self.output_structure.to_dict(),
            "version": self.version,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Create a PromptWrapper object from a dictionary.
        """
        res = cls(
            prompts=data["prompts"],
            dilemma_identifier=data["dilemma_identifier"],
            framework_identifier=data["framework_identifier"],
            base_prompt_identifier=data["base_prompt_identifier"],
            output_structure=OutputStructure.from_dict(
                data["output_structure"]),
            version=data["version"],
        )

        res.add_id(data["id"])
        return res


class Model(Enum):
    GPT4O = "gpt-4o"


class GPTMessageRole(Enum):
    SYSTEM = "system"
    ASSISSANT = "assistant"


class GPTMessage:
    def __init__(self, role: GPTMessageRole, content: str):
        self.role = role
        self.content = content

    def to_dict(self):
        return {
            "role": self.role.value,
            "content": self.content,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            role=GPTMessageRole(data["role"]),
            content=data["content"],
        )


class Response:
    def __init__(self, wrapped_prompt: PromptWrapper, decision: DecisionOption, llm_identifier: Model, unparsed_messages: list[GPTMessage], parsed_response: dict):
        self.wrapped_prompt = wrapped_prompt
        self.decision = decision
        self.llm_identifier = llm_identifier
        self.unparsed_messages = unparsed_messages
        self.parsed_response = parsed_response

    def to_dict(self):
        return {
            "wrapped_prompt": self.wrapped_prompt.to_dict(),
            "decision": self.decision.value,
            "llm_identifier": self.llm_identifier.value,
            "unparsed_messages": [message.to_dict() for message in self.unparsed_messages],
            "parsed_response": self.parsed_response,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            wrapped_prompt=PromptWrapper.from_dict(data["wrapped_prompt"]),
            decision=DecisionOption(data["decision"]),
            llm_identifier=Model(data["llm_identifier"]),
            unparsed_messages=[GPTMessage.from_dict(item) for item in data["unparsed_messages"]],
            parsed_response=data["parsed_response"],
        )

    def get_messages_by_role(self, role: GPTMessageRole) -> list[GPTMessage]:
        return [message for message in self.unparsed_messages if message.role == role]

    @property
    def input_tokens_len(self) -> int:
        sum = 0
        for i in range(0, len(self.unparsed_messages) - 1):
            for j in range(0, i + 1):
                sum += len(self.unparsed_messages[j].content)
        return sum
    
    @property
    def output_tokens_len(self) -> int:
        sum = 0
        assistant_messages = self.get_messages_by_role(GPTMessageRole.ASSISSANT)
        for message in assistant_messages:
            sum += len(message.content)
        return sum