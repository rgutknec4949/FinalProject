from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import payment as controller
from ..schemas import payment as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Payments'],
    prefix="/payments"
)

@router.post("/", response_model=schema.Payment)
def create(request: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/order/{order_id}", response_model=schema.Payment)
def read_by_order(order_id: int, db: Session = Depends(get_db)):
    return controller.read_by_order(db, order_id=order_id)

@router.get("/{item_id}", response_model=schema.Payment)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)