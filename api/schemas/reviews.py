from typing import Optional
from pydantic import BaseModel, Field

class ReviewBase(BaseModel):
    order_id: int
    feedback: Optional[str] = None
    rating: float = Field(..., ge=0, le=5, description="Rating must be between 0 and 5")

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int

    class ConfigDict:
        from_attributes = True