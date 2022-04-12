from optparse import Option
from pydantic import BaseModel
from typing import Optional
import datetime as dt

from app.schemas.address import Address


class RecordBase(BaseModel):
    name: Optional[str] = None
    address_id: Optional[int] = None
    company: Optional[str] = None
    transaction_id: Optional[int] = None


class RecordCreate(RecordBase):
    name: str
    address_id: int
    transaction_id: int


class RecordUpdate(RecordBase):
    pass


class RecordInDB(BaseModel):
    id: int
    name: str
    address: Address
    company: Optional[str]
    transaction_id: int
    created_datetime: dt.datetime
    updated_datetime: dt.datetime

    class Config:
        orm_mode = True


class Record(RecordInDB):
    pass
