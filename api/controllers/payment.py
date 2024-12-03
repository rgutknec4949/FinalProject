from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import payments as model, orders as order_model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    # Check if the order exists and doesn't already have a payment
    order = db.query(order_model.Order).filter(order_model.Order.id == request.order_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found!")

    if db.query(model.Payment).filter(model.Payment.order_id == request.order_id).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Payment already exists for this order!")

    new_payment = model.Payment(
        order_id=request.order_id,
        payment_type=request.payment_type,
        card_number=request.card_number,
        cash_amount=request.cash_amount
    )

    try:
        # Update order's payment method
        order.payment_method = request.payment_type

        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_payment


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Payment).filter(model.Payment.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def read_by_order(db: Session, order_id):
    try:
        payment = db.query(model.Payment).filter(model.Payment.order_id == order_id).first()
        if not payment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No payment found for this order!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return payment