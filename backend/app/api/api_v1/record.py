from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db

from app.schemas.record import Record, RecordCreate, RecordUpdate
from app.services.record import create, get_all, get_one, update, delete


router = APIRouter(tags=["Record"], prefix="/record")


@router.post("/", response_model=Record)
def create_record(record: RecordCreate, db: Session = Depends(get_db)):
    return create(record, db)


@router.get("/", response_model=List[Record])
def get_all_records(db: Session = Depends(get_db)):
    return get_all(db)


@router.get("/{id}", response_model=Record)
def get_record(id: int, db: Session = Depends(get_db)):
    return get_one(id, db)


@router.put("/{id}", response_model=Record)
def update_record(id: int, updated_record: RecordUpdate, db: Session = Depends(get_db)):
    return update(id, updated_record, db)


@router.delete("/{id}")
def delete_record(id, db: Session = Depends(get_db)):
    return delete(id, db)
