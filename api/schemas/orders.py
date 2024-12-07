from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel


class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None
    promo_id: Optional[str] = None
    payment: str
    tracking_number: int
    delivery_option: Optional[str] = None
    order_date: datetime
    menu_id: Optional[int] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: str
    description: Optional[str] = None
    promo_id: Optional[str] = None
    payment: str
    tracking_number: int
    delivery_option: Optional[str] = None
    order_date: datetime
    menu_id: Optional[int] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None

    class ConfigDict:
        from_attributes = True