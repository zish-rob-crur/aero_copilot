from typing import Dict, Optional
from pathlib import Path

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

from aero_copilot.core import color_print


class LogSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="LOG_",
    )
    level: str = "INFO"
    path: Path = Path(
        Path(__file__).parent.parent,
        "logs",
        "aero_copilot.log",
    )
    rotation: str = "1 week"
    serialize: bool = True


class CelerySettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="CELERY_",
    )
    broker_url: str = "redis://localhost:6379/0"
    result_backend: str = "redis://localhost:6379/0"


class LlMSettings(BaseSettings):
    model_config = SettingsConfigDict()
    provider: str = "ollama"
    model: str = "mistral:7b"
    base_url: AnyHttpUrl = "http://localhost:8000"
    api_key: Optional[str] = None
    timeout: int = 300


class OpenAISettings(LlMSettings):
    model_config = SettingsConfigDict(
        env_prefix="OPENAI_",
    )


class OLlamaSettings(LlMSettings):
    model_config = SettingsConfigDict(
        env_prefix="OLLAMA_",
    )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
    )
    celery: CelerySettings = CelerySettings()
    openai: OpenAISettings = OpenAISettings()
    ollama: OLlamaSettings = OLlamaSettings()
    log: LogSettings = LogSettings()


settings = Settings()
color_print("APP SETTINGS:")
color_print(
    settings.model_dump_json(
        indent=2,
    )
)
