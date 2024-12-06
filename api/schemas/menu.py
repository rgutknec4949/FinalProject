from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

class MenuBase(BaseModel):
    name: str
    category: str
    price: float
    calorie: Optional[int] = None
    ingredients: List[str]

class MenuCreate(MenuBase):
    pass

class MenuUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    calorie: Optional[int] = None
    ingredients: Optional[List[str]] = None

class Menu(MenuBase):
    id: int

    class ConfigDict:
        from_attributes = True
