from typing import Optional, List
from pydantic import BaseModel


class Menu(BaseModel):
    menu_id: int
    menu_dishes: str
    menu_ingredients: Optional[str] = None
    menu_price: float

    class Config:
        orm_mode = True

class MenuCreate(Menu):
    pass


class MenuResponse(BaseModel):
    menu: str
    orders: List[Menu]

