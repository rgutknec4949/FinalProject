from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .resources import Resource
from .resources import ResourceCreate


class RecipeBase(BaseModel):
    ingredient: str
    recipe_name: str


class RecipeCreate(BaseModel):
    recipe_name: str
    ingredients: Optional[List[str]] = None

class RecipeUpdate(BaseModel):
    recipe_name: Optional[str] = None
    ingredient: Optional[List[str]] = None

class Recipe(BaseModel):
    recipe_name: str
    ingredients: List[str]

    class ConfigDict:
        from_attributes = True