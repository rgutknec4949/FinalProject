from typing import Optional, List
from pydantic import BaseModel


# Payment Schemas
class PaymentBase(BaseModel):
    pay_info: str
    pay_status: str
    pay_type: str
    cust_id: int
    order_id: int


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    pay_info: Optional[str] = None
    pay_status: Optional[str] = None
    pay_type: Optional[str] = None


class Payment(PaymentBase):
    pay_id: int

    class ConfigDict:
        from_attributes = True