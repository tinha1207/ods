from pydantic import BaseModel
from typing import Optional


class TransactionBase(BaseModel):
    file_name: Optional[str] = None


class TransactionCreate(TransactionBase):
    file_name: str


class TransactionBaseDB(BaseModel):
    id: int
    file_name: Optional[str]

    class Config:
        orm_mode = True


class Transaction(TransactionBaseDB):
    pass
