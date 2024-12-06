from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ingredient = Column(String(100), unique=True, nullable=False, default="unknown")
    amount = Column(Integer, index=True, nullable=False, server_default='0.0')

