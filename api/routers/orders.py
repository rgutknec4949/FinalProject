from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import engine, get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..controllers import orders as order_controller
from datetime import datetime
from typing import List
from ..schemas import orders as order_schema

router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)


@router.post("/", response_model=schema.Order)
def create(request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Order])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/revenue", response_model=int)
def get_total_revenue(db: Session = Depends(get_db)):
    return controller.get_total_revenue(db)

@router.get("/{item_id}", response_model=schema.Order)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.Order)
def update(item_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)

@router.get("/tracking/{tracking_number}", response_model=schema.Order)
def read_by_track(tracking_number: str, db: Session = Depends(get_db)):
    return controller.read_by_track(db, tracking_number=tracking_number)

@router.get("/orders/date-range", response_model=List[order_schema.Order])
def get_orders_by_date_range(start_date: datetime, end_date: datetime, db: Session = Depends(get_db)):
    return order_controller.read_orders_by_date_range(db, start_date, end_date)

