from sqlalchemy import Column, ForeignKey, Integer, String, Float, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


# Order model
class Order(Base):
    __tablename__ = 'order'
    order_id = Column(Integer, primary_key=True)
    order_date = Column(DATETIME, nullable=False)
    order_track = Column(String, unique=True, nullable=True)
    order_status = Column(String, nullable=False)
    order_total = Column(Float, nullable=False)

    # Foreign Keys
    cust_id = Column(Integer, ForeignKey('customer.cust_id'))
    promo_id = Column(Integer, ForeignKey('promotion.promo_id'))

    # Relationships
    customer = relationship('Customer', back_populates='orders')
    promotion = relationship('Promotion', back_populates='orders')
    payment = relationship('Payment', back_populates='order')
    menu_items = relationship('MenuItem', secondary='order_menu_item', back_populates='orders')