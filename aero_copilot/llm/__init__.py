from aero_copilot.llm.chat.base import BaseLLMChatGenerator
from aero_copilot.llm.completion.base import BaseLLMCompletionGenerator
from aero_copilot.llm.chat.openai_chat import OpenAIChatGenerator
from aero_copilot.llm.completion.ollama_completion import (
    OllamaCompletionGenerator,
)
from aero_copilot.llm.completion.openai_completion import (
    OpenAICompletionGenerator,
)

CHAT_MODELS = {
    "openai": OpenAIChatGenerator,
    "ollama": OpenAIChatGenerator,
}

COMPLETION_MODELS = {
    "openai": OpenAICompletionGenerator,
    "ollama": OllamaCompletionGenerator,
}


def get_chat_model(provider: str, model: str) -> BaseLLMChatGenerator:
    if provider not in CHAT_MODELS:
        raise NotImplementedError(f"Provider {provider} is not supported.")
    return CHAT_MODELS[provider](model=model, provider=provider)


def get_completion_model(provider: str, model: str) -> BaseLLMCompletionGenerator:
    if provider not in COMPLETION_MODELS:
        raise NotImplementedError(f"Provider {provider} is not supported.")
    return COMPLETION_MODELS[provider](model=model, provider=provider)
