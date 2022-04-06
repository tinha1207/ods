from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db

from app.schemas.address import AddressBase, AddressCreate, Address, AddressUpdate
from app.services.address import create, update, get, get_all, delete

router = APIRouter(tags=["Address"], prefix="/address")


@router.get("/", response_model=List[Address])
def get_all_addreses(db: Session = Depends(get_db)):
    """Returns a list of all addreses."""
    return get_all(db)


@router.get("/{id}", response_model=Address)
def get_address(id: int, db: Session = Depends(get_db)):
    """Returns 1 address based on id."""
    return get(id, db)


@router.post("/", response_model=Address)
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    """Creates 1 Address"""
    return create(db=db, address=address)


@router.put("/{id}", response_model=Address)
def update_address(
    id: int, updated_address: AddressUpdate, db: Session = Depends(get_db)
):
    """Upadtes 1 address."""
    return update(id, updated_address, db)


@router.delete("/{id}")
def delete_address(id: int, db: Session = Depends(get_db)):
    """Deletes an address based on id"""
    return delete(id, db)
