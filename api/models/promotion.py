from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


# Promotion model
class Promotion(Base):
    __tablename__ = 'promotion'
    promo_id = Column(Integer, primary_key=True)
    promo_code = Column(String, unique=True, nullable=False)
    promo_exp = Column(DATETIME, nullable=False)

    # Relationships
    orders = relationship('Order', back_populates='promotion')