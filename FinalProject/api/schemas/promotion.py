from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

# Promotion Schemas
class PromotionBase(BaseModel):
    promo_code: str
    promo_exp: datetime

class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    promo_code: Optional[str] = None
    promo_exp: Optional[datetime] = None


class Promotion(PromotionBase):
    promo_id: int
    orders: List["Order"] = []

    class ConfigDict:
        from_attributes = True