from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .resources import Resource


class RecipeBase(BaseModel):
    amount: int


class RecipeCreate(RecipeBase):
    resource_id: int

class RecipeUpdate(BaseModel):
    resource_id: Optional[int] = None
    amount: Optional[int] = None

class Recipe(RecipeBase):
    id: int
    resource: Resource = None

    class ConfigDict:
        from_attributes = True