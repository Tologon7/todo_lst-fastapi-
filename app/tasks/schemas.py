from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from fastapi import Query
from datetime import date


class STasksCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    description: Optional[str]
    complexity: int = Field(ge=1, le=5)
    deadline: Optional[date]
    is_active: bool


class STasksShowAll(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    done: Optional[bool]


class STasksDetailShow(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: Optional[str]
    complexity: int
    data_create: date
    deadline: Optional[date]
    done: Optional[bool]
    is_active: bool

