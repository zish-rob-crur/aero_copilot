import uuid

import ollama
import dateparser
from loguru import logger
from openai.types.completion import Completion
from openai.types.completion_usage import CompletionUsage
from openai.types.completion_choice import CompletionChoice

from aero_copilot.core.settings import settings
from aero_copilot.llm.completion.base import BaseLLMCompletionGenerator


class OllamaCompletionGenerator(BaseLLMCompletionGenerator):
    def __init__(self, model: str, provider: str) -> None:
        super().__init__(model)
        self.setting = settings.ollama
        self.host = "{}://{}:{}".format(
            self.setting.base_url.scheme,
            self.setting.base_url.host,
            self.setting.base_url.port,
        )
        logger.info(f"Connecting to Ollama at {self.host}")
        self.client = ollama.Client(
            host=self.host,
        )

    def generate(self, prompt: str, max_tokens: int = 4096, temperature: float = 1.0):
        response = self.client.generate(
            model=self.model,
            prompt=prompt,
            options={
                "temperature": temperature,
            },
        )
        logger.debug(
            "Generated completion for model: {model} prompt: {prompt} response: {response}",
            model=self.model,
            prompt=prompt,
            response=response,
        )
        model = response["model"]
        content = response["response"]
        return Completion(
            id=str(uuid.uuid4().hex),
            model=model,
            choices=[CompletionChoice(text=content, index=0, finish_reason="stop")],
            created=int(dateparser.parse(response["created_at"]).timestamp()),
            object="text_completion",
        )
