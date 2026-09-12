from pydantic import BaseModel, ConfigDict
from typing import Optional
from fastapi import Query
from datetime import date


class STasksCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    description: Optional[str]
    complexity: int = Query(None, ge=1, le=5)
    deadline: Optional[date]
    is_active: bool
