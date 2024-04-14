from loguru import logger
from openai import OpenAI
from openai.types.completion import Completion

from aero_copilot.core.settings import settings
from aero_copilot.llm.completion.base import BaseLLMCompletionGenerator


class OpenAICompletionGenerator(BaseLLMCompletionGenerator):

    def __init__(self, model: str, provider: str) -> None:
        super().__init__(model)
        if provider == "openai":
            self.setting = settings.openai
        elif provider == "ollama":
            raise NotImplementedError("Provider ollama is not supported.")
        else:
            raise NotImplementedError(f"Provider {provider} is not supported.")

        self.openai = OpenAI(
            api_key=self.setting.api_key,
            base_url=self.setting.base_url,
            timeout=self.setting.timeout,
        )

    def generate(
        self, prompt: str, max_tokens: int = 4096, temperature: float = 1.0
    ) -> Completion:
        logger.info(
            "Generating completion for model: {model} prompt: {prompt}",
            model=self.model,
            prompt=prompt,
        )
        return self.openai.completions.create(
            model=self.model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
        )
