from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

# Customer model
class Customer(Base):
    __tablename__ = 'customer'
    cust_id = Column(Integer, primary_key=True)
    cust_name = Column(String, nullable=False)
    cust_email = Column(String, unique=True, nullable=False)
    cust_phone = Column(String, nullable=False)
    cust_address = Column(String, nullable=False)

    # Relationships
    orders = relationship('Order', back_populates='customer')
    ratings = relationship('Rating', back_populates='customer')
    payments = relationship('Payment', back_populates='customer')