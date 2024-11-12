from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

# Menu Item Model
class MenuItem(Base):
    __tablename__ = "menu_item"
    menu_id = Column(Integer, primary_key=True, nullable=False)
    menu_dishes = Column(String, nullable=False)
    menu_ingredients = Column(String, nullable=False)
    menu_price = Column(Float, nullable=False)
    menu_carolie = Column(Integer, nullable=False)
    menu_category = Column(String, nullable=False)

    orders = relationship("Order", secondary="order_menu_item", back_populates="menu_items")
