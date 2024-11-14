from typing import Optional
from pydantic import BaseModel

# Rating Schemas
class RatingBase(BaseModel):
    rev_text: Optional[str] = None
    rev_score: int
    cust_id: int


class RatingCreate(RatingBase):
    pass


class RatingUpdate(BaseModel):
    rev_text: Optional[str] = None
    rev_score: Optional[int] = None


class Rating(RatingBase):
    rev_id: int

    class ConfigDict:
        from_attributes = True