from pydantic import BaseModel


class SRoleAdd(BaseModel):
    name: str
