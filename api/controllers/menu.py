from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import menu as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_item = model.MenuItem(
        menu_id=request.menu_id,
        menu_dishes=request.menu_dishes,
        menu_ingredients=request.menu_ingredients,
        menu_price=request.menu_price,
        menu_carolie=0,
        menu_category="default"
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item

def read_all(db: Session):
    try:
        result = db.query(model.MenuItem).all()

        menu_text = """
        Welcome to Discord Diner:
        Choose your Menu Options:
        1. Ham Sandwich
        2. Turkey Sandwich
        3. Cheese Sandwich
        """

        return {
            "menu": menu_text,
            "orders": result
        }
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def read_one(db: Session, item_id: int):
    try:
        item = db.query(MenuItem).filter(MenuItem.menu_id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item

def update(db: Session, item_id: int, request):
    try:
        item = db.query(MenuItem).filter(MenuItem.menu_id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")

        update_data = request.dict(exclude_unset=True)  # Ensure data is correctly parsed from Pydantic model
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()

def delete(db: Session, item_id: int):
    try:
        item = db.query(MenuItem).filter(MenuItem.menu_id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return {"detail": "Item deleted successfully"}
