from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import orders as order_model, order_details as detail_model
from ..schemas import orders as order_schema
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request: order_schema.OrderCreate):
    # Create the Order
    new_order = order_model.Order(
        customer_name=request.customer_name,
        description=request.description,
        promo_id=request.promo_id,
        payment=request.payment
    )
    try:
        db.add(new_order)
        db.commit()
        db.refresh(new_order)

        # Automatically create a corresponding OrderDetail
        new_detail = detail_model.OrderDetail(
            order_id=new_order.id,  # Use the ID of the created order
            item_name="Default Item",  # Default values, can be updated later
            quantity=1,
            price=0
        )
        db.add(new_detail)
        db.commit()

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_order
