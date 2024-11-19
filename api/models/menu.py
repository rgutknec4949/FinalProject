from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from ..dependencies.database import Base  # Adjusted import path for your database dependency


# MenuItem Model
class MenuItem(Base):
    __tablename__ = "menu_items"

    menu_id = Column(Integer, primary_key=True, index=True, nullable=False)
    menu_dishes = Column(String(100), nullable=False)  # Increased string length for more flexibility
    menu_ingredients = Column(String(255), nullable=True)
    menu_price = Column(Float, nullable=False)
    menu_carolie = Column(Integer, nullable=True)
    menu_category = Column(String(50), nullable=False)

    # Adjust the relationship to match the actual relationships in your database
    orders = relationship("Order", secondary="order_menu_item", back_populates="menu_items")
