from pydantic import BaseModel, HttpUrl
from typing import Literal

class GenerateRequest(BaseModel):
    url: HttpUrl
    instruction: str
