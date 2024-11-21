from datetime import date
from typing import Optional
from pydantic import BaseModel

class PromotionBase(BaseModel):
    code_name: str
    expiration_date: date

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    code_name: Optional[str] = None
    expiration_date: Optional[date] = None

class Promotion(PromotionBase):
    id: int

    class ConfigDict:
        from_attributes = True
