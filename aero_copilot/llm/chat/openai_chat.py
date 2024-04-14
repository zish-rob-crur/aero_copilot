from typing import Any, Dict, List

from loguru import logger
from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion

from aero_copilot.core.settings import settings
from aero_copilot.llm.chat.base import BaseLLMChatGenerator
from aero_copilot.schemas.message import Message


class OpenAIChatGenerator(BaseLLMChatGenerator):
    def __init__(
        self,
        model: str,
        provider: str,
    ) -> None:
        super().__init__(model=model)
        if provider == "openai":
            self.setting = settings.openai
        elif provider == "ollama":
            self.setting = settings.ollama
        else:
            raise NotImplementedError(f"Provider {provider} is not supported.")

        self.openai = OpenAI(
            api_key=self.setting.api_key,
            base_url=self.setting.base_url,
            timeout=self.setting.timeout,
        )

    def models(self):
        return self.openai.models.list()

    def generate(
        self,
        messages: List[Message],
        max_tokens: int = 4096,
        temperature: float = 1.0,
    ) -> ChatCompletion:
        logger.info(
            "Generating completion for model: {model} messages: \n{messages}",
            messages="\n".join([f"{m.role}: {m.content}" for m in messages]),
            model=self.model,
        )
        return self.openai.chat.completions.create(
            messages=[m.model_dump() for m in messages],
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
        )
