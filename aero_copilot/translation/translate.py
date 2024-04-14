from loguru import logger

from aero_copilot.llm import get_completion_model
from aero_copilot.llm.prompt import get_prompt
from aero_copilot.schemas.message import (
    ROLE_USER,
    ROLE_SYSTEM,
    ROLE_ASSISTANT,
    Message,
)


class LLMTranslate:

    def __init__(
        self,
        provider: str,
        model: str,
        from_language: str = "english",
        target_language: str = "chinese",
        prompt_name: str = "translate_v1",
        prompt: str = None,
    ) -> None:
        self.provider = provider
        self.model = model
        self.target_language = target_language
        self.llm = get_completion_model(provider, model)
        self.prompt = prompt
        self.prompt_name = prompt_name
        self.from_language = from_language

    def translate(self, text: str, max_tokens: int = 4096) -> str:
        if self.prompt is None and self.prompt_name is not None:
            prompt = get_prompt(
                self.prompt_name,
                variables={
                    "language": self.target_language,
                    "from_language": self.from_language,
                },
            )
        else:
            raise ValueError("prompt or prompt_name must be provided")
        if self.llm.generate_type == "chat":
            messages = [
                Message(role=ROLE_USER, content=prompt),
                Message(role=ROLE_SYSTEM, content=text),
            ]
            response = self.llm.generate(messages, max_tokens=max_tokens)
        elif self.llm.generate_type == "completion":
            prompt = f"{prompt}\n{text}"
            response = self.llm.generate(prompt, max_tokens=max_tokens)
        else:
            raise NotImplementedError(
                f"Generate type {self.llm.generate_type} is not supported"
            )
        translated_text = response.choices[0].text
        usage = response.usage
        logger.info(
            "Translated text len {translated_text} usage {usage}",
            translated_text=len(translated_text),
            usage=usage,
        )
        return translated_text
