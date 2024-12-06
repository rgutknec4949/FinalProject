from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ResourceBase(BaseModel):
    ingredient: str
    amount: int


class ResourceCreate(ResourceBase):
    ingredient: str
    amount: Optional[int] = None


class ResourceUpdate(BaseModel):
    ingredient: Optional[str] = None
    amount: Optional[int] = None


class Resource(ResourceBase):
    id: int
    ingredient: str
    amount: int

    class ConfigDict:
        from_attributes = True