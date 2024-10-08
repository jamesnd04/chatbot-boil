# external
from pydantic import BaseModel

# interal
from enum import Enum


class Role(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"


class Message(BaseModel):
    role: Role
    content: str
