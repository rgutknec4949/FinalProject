from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import menu as controller
from ..schemas import menu as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Menu'],
    prefix="/menu"
)

@router.post("/", response_model=schema.Menu)
def create(request: schema.MenuCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Menu])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.Menu)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.Menu)
def update(item_id: int, request: schema.MenuUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
