from sqlalchemy import Column, Integer, String, Float, Text, JSON
from sqlalchemy.dialects.postgresql import ARRAY  # Use for storing lists
from ..dependencies.database import Base

class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    calorie = Column(Integer, nullable=True)
    ingredients = Column(JSON, nullable=False)