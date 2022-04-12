from pydantic import BaseModel
from typing import List, Optional
import datetime as dt


class AddressBase(BaseModel):
    address1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    is_household: Optional[bool] = None


class AddressCreate(AddressBase):
    address1: str
    city: str
    state: str
    zip: str
    is_household: bool = False


class AddressUpdate(AddressBase):
    pass


class AddressInDB(BaseModel):
    id: int
    address1: str
    city: str
    state: str
    zip: str
    is_household: bool

    class Config:
        orm_mode = True


class Address(AddressInDB):
    created_datetime: dt.datetime
    updated_datetime: Optional[dt.datetime]
