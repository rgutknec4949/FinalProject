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
    payment = Column(String(100), unique=False)  # Add the payment attribute
    tracking_number = Column(String(50), nullable=True, unique=True)

    order_details = relationship("OrderDetail", back_populates="order")

    promo = relationship("Promotion")