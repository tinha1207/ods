from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from ..deps import get_db
from ...schemas.transaction import TransactionCreate, Transaction
from ...services.transaction import create, get_transaction_time

router = APIRouter(tags=["Transaction"], prefix="/transaction")


@router.post("/", response_model=Transaction)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return create(transaction, db)


@router.get("/{id}")
def get_transaction_time_by_id(id: int, db: Session = Depends(get_db)):
    return get_transaction_time(id, db)
