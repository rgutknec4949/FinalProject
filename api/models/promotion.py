from sqlalchemy import Column, Integer, String, Date
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code_name = Column(String(16), nullable=False, unique=True)
    expiration_date = Column(Date, nullable=False)

