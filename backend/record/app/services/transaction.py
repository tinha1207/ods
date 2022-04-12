from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..models.transaction import Transaction as TransactionModel
from ..schemas.transaction import TransactionCreate


def create(transaction: TransactionCreate, db: Session):
    new_transaction = TransactionModel(**transaction.dict())
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction


def get_transaction_time(id: int, db: Session):
    transaction = db.query(TransactionModel).filter(TransactionModel.id == id).first()
    if transaction is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return transaction
