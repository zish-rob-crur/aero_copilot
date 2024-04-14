from openai.types.completion import Completion


class BaseLLMCompletionGenerator:
    def __init__(self, model: str) -> None:
        self.model = model
        self.generate_type = "completion"

    def generate(
        self, prompt: str, max_tokens: int = 4096, temperature: float = 1.0
    ) -> Completion:
        raise NotImplementedError