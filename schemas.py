from typing import Optional
from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    Description: Optional[str] = None

class STask(STaskAdd):
    id: int

tasks = []