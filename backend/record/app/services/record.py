from sqlalchemy.orm import Session
from app.schemas.record import RecordCreate, RecordUpdate
from fastapi import HTTPException, status
from app.models.record import Record as RecordModel


def create(record: RecordCreate, db: Session):
    new_record = RecordModel(**record.dict())
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record


def get_all(db: Session):
    return db.query(RecordModel).all()


def get_one(id: int, db: Session):
    record = db.query(RecordModel).filter(RecordModel.id == id).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return record


def update(id: int, updated_record: RecordUpdate, db: Session):
    record = db.query(RecordModel).filter(RecordModel.id == id)
    if not record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    record.update(updated_record.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return record.first()


def delete(id: int, db: Session):
    record = db.query(RecordModel).filter(RecordModel.id == id).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.delete(record)
    db.commit()


def get_count_of_transactions_by_transaction_id(transaction_id: int, db: Session):
    records = (
        db.query(RecordModel)
        .filter(RecordModel.transaction_id == transaction_id)
        .count()
    )
    return records
