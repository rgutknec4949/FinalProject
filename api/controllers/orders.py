from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..schemas import orders as order_schema
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from ..models import orders as model
from ..models import orders as order_model, menu as menu_model



def create(db: Session, request: order_schema.OrderCreate):
    promo_id = request.promo_id if request.promo_id != "" else None

    menu_item = db.query(menu_model.Menu).filter(menu_model.Menu.id == request.menu_id).first()
    if not menu_item:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Menu item not found")

    # Increment the price of the menu item
    order_model.Order.revenue += menu_item.price

    new_order = model.Order(
        customer_name=request.customer_name,
        description=request.description,
        promo_id=promo_id,
        payment=request.payment,
        tracking_number=request.tracking_number,
        delivery_option=request.delivery_option,
        order_date=request.order_date,
        menu_id=request.menu_id,
        revenue=menu_item.price
    )

    try:
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return new_order

def read_all(db: Session):
    try:
        result = db.query(model.Order).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return result

def read_one(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return item

def update(db: Session, item_id, request):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return item.first()

def delete(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def read_by_track(db: Session, tracking_number):
    try:
        item = db.query(model.Order).filter(model.Order.tracking_number == tracking_number).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tracking number not found!")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return item

def read_orders_by_date_range(db: Session, start_date: datetime, end_date: datetime):
    try:
        orders = db.query(model.Order).filter(
            model.Order.order_date >= start_date,
            model.Order.order_date <= end_date
        ).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return orders

def get_total_revenue(db: Session):
    try:
        total_revenue = db.query(func.sum(model.Order.revenue)).scalar()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return total_revenue
