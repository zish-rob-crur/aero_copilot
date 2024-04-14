from typing import Literal

from pydantic import BaseModel

ROLE_SYSTEM = "system"
ROLE_USER = "user"
ROLE_ASSISTANT = "assistant"

class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str
