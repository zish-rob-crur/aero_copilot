from typing import Any, Dict, List

from openai.types.chat.chat_completion import ChatCompletion

from aero_copilot.core.settings import settings


class BaseLLMChatGenerator:

    def __init__(self, model: str) -> None:
        self.model = model
        self.generate_type = "chat"

    def models(self) -> List[str]:
        raise NotImplementedError

    def generate(self, messages: List[Dict[str, Any]]) -> ChatCompletion:
        raise NotImplementedError
