from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

# Rating model
class Rating(Base):
    __tablename__ = 'rating'
    rev_id = Column(Integer, primary_key=True)
    rev_text = Column(String, nullable=True)
    rev_score = Column(Integer, nullable=False)

    # Foreign Key
    cust_id = Column(Integer, ForeignKey('customer.cust_id'))

    # Relationships
    customer = relationship('Customer', back_populates='ratings')