from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

# Resource Management model
class ResourceManagement(Base):
    __tablename__ = 'resource_management'
    resource_id = Column(Integer, primary_key=True)
    resource_name = Column(String, nullable=False)
    resource_amount = Column(Float, nullable=False)
