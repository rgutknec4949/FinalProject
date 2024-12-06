from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base



class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    recipe_name = Column(String(100), index=True, nullable=False)
    ingredients = Column(JSON, nullable=False)

