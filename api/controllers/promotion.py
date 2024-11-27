from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import promotion as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_promotion = model.Promotion(
        code_name=request.code_name,
        expiration_date=request.expiration_date
    )
    try:
        db.add(new_promotion)
        db.commit()
        db.refresh(new_promotion)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_promotion

def read_all(db: Session):
    try:
        result = db.query(model.Promotion).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_one(db: Session, promo_id):
    try:
        promo = db.query(model.Promotion).filter(model.Promotion.id == promo_id).first()
        if not promo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return promo

def update(db: Session, promo_id, request):
    try:
        promo = db.query(model.Promotion).filter(model.Promotion.id == promo_id)
        if not promo.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found!")
        update_data = request.dict(exclude_unset=True)
        promo.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return promo.first()

def delete(db: Session, promo_id):
    try:
        promo = db.query(model.Promotion).filter(model.Promotion.id == promo_id)
        if not promo.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found!")
        promo.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)