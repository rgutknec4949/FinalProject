from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import reviews as controller
from ..schemas import reviews as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Reviews'],
    prefix="/reviews"
)

@router.post("/", response_model=schema.Review)
def create(request: schema.ReviewCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Review])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/order/{order_id}", response_model=list[schema.Review])
def read_by_order(order_id: int, db: Session = Depends(get_db)):
    return controller.read_by_order(db, order_id=order_id)

@router.get("/{item_id}", response_model=schema.Review)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)