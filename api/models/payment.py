from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), unique=True, nullable=False)
    payment_type = Column(String(10), nullable=False)  # 'Cash' or 'Card'
    card_number = Column(String(16), nullable=True)
    cash_amount = Column(DECIMAL(10, 2), nullable=True)

    order = relationship("Order", back_populates="payment")