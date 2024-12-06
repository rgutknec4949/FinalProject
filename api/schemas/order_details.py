from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class OrderDetailBase(BaseModel):
    item_name: str
    price: float
    quantity: int



class OrderDetailCreate(OrderDetailBase):
    order_id: int

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    item_name: Optional[str] = None

class OrderDetail(OrderDetailBase):
    id: int
    order_id: int

    class ConfigDict:
        from_attributes = True