from pydantic import BaseModel
from typing import List, Optional
import datetime as dt


class AddressBase(BaseModel):
    address1: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip: Optional[str]


class AddressCreate(AddressBase):
    address1: str
    city: str
    state: str
    zip: str


class AddressUpdate(AddressBase):
    pass


class AddressInDB(BaseModel):
    id: int
    address1: str
    city: str
    state: str
    zip: str

    class Config:
        orm_mode = True


class Address(AddressInDB):
    created_datetime: dt.datetime
    updated_datetime: Optional[dt.datetime]
