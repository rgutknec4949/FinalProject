from typing import Optional
from pydantic import BaseModel, Field, validator

class PaymentBase(BaseModel):
    order_id: int
    payment_type: str
    card_number: Optional[str] = None
    cash_amount: Optional[float] = None

    @validator('payment_type')
    def validate_payment_type(cls, v):
        if v not in ['Cash', 'Card']:
            raise ValueError('Payment type must be Cash or Card')
        return v

    @validator('card_number')
    def validate_card_number(cls, v, values):
        if values.get('payment_type') == 'Card' and not v:
            raise ValueError('Card number is required for Card payment')
        return v

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int

    class ConfigDict:
        from_attributes = True