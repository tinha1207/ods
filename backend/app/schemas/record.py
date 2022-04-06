from optparse import Option
from pydantic import BaseModel
from typing import Optional
import datetime as dt

from app.schemas.address import Address


class RecordBase(BaseModel):
    name: Optional[str]
    address_id: Optional[int]
    company: Optional[str]

    class Config:
        arbitrary_types_allowed = True


class RecordCreate(RecordBase):
    name: str
    address_id: int


class RecordUpdate(RecordBase):
    pass


class RecordInDB(BaseModel):
    id: int
    name: str
    address: Address
    company: Optional[str]
    is_household: bool
    created_datetime: dt.datetime
    updated_datetime: dt.datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class Record(RecordInDB):
    pass
