from sqlalchemy.orm import Session
from app.schemas.address import AddressCreate, AddressUpdate
from fastapi import HTTPException, status
from app.models.address import Address as AddressModel


def create(address: AddressCreate, db: Session):
    new_address = AddressModel(**address.dict())
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address


def update(id: int, updated_address: AddressUpdate, db: Session):
    address = db.query(AddressModel).filter(AddressModel.id == id)
    if not address.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    address.update(updated_address.dict(), synchronize_session=False)
    db.commit()
    return address.first()


def get(id: int, db: Session):
    address = db.query(AddressModel).filter(AddressModel.id == id).first()
    if not address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return address


def get_all(db: Session):
    return db.query(AddressModel).all()


def delete(id: int, db: Session):
    address = db.query(AddressModel).filter(AddressModel.id == id)
    if not address.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.delete(address.first())
    db.commit()
