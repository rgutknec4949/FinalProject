from email.policy import default

from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))
    promo_id = Column(String(16), ForeignKey("promotions.code_name"), nullable=True)
    payment = Column(String(100), unique=False)
    tracking_number = Column(Integer, nullable=False, unique=True)
    delivery_option = Column(String(50), nullable=True)
    menu_id = Column(Integer, ForeignKey("menu.id"), nullable=True)
    revenue = Column(Integer, nullable=False, default=0)

    promo = relationship("Promotion")
