from typing import Optional, List
from pydantic import BaseModel




# Payment Schemas
class CustomerBase(BaseModel):
    cust_id: int
    cust_name: str
    cust_email: str
    cust_phone: int
    cust_address: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    cust_name: Optional[str] = None
    cust_email: Optional[str] = None
    cust_address: Optional[str] = None
    cust_phone: Optional[int] = None
    cust_id: Optional[int] = None


class Customer(CustomerBase):
    cust_id: int

    class ConfigDict:
        from_attributes = True