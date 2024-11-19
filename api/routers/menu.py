from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import menu as controller  # Adjusted import path for 'controllers'
from ..schemas import menu as schema  # Adjusted import path for 'schemas'
from ..dependencies.database import get_db  # Adjusted import path for 'database'
from typing import List

router = APIRouter(
    tags=["Menu"],
    prefix="/menu"
)

@router.post("/", response_model=schema.Menu)
def create(request: schema.MenuCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=List[schema.Menu])  # Fixed: Ensure List is imported from typing
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.Menu)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.Menu)
def update(item_id: int, request: schema.MenuCreate, db: Session = Depends(get_db)):  # Fixed: Used `MenuCreate`
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
