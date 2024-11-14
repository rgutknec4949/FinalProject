from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = 'payment'
    pay_id = Column(Integer, primary_key=True)
    pay_info = Column(String(32), nullable=False)
    pay_status = Column(String(32), nullable=False)
    pay_type = Column(String(32), nullable=False)

    # Foreign Keys
    cust_id = Column(Integer, ForeignKey('customer.cust_id'))
    order_id = Column(Integer, ForeignKey('orders.order_id'))

    # Relationships
    customer = relationship('Customer', back_populates='payments')
    order = relationship('Order', back_populates='payment')