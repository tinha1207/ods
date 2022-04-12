from sqlalchemy import (
    Column,
    String,
    Integer,
    Boolean,
    UniqueConstraint,
    DateTime,
    text,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.db import Base


class Address(Base):
    __tablename__ = "address"
    __table_args__ = (
        UniqueConstraint("address1", "city", "state", "zip", name="uix_address"),
    )

    id = Column(Integer, primary_key=True)
    address1 = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(2), nullable=False)
    zip = Column(String(10), nullable=False)
    is_household = Column(Boolean, nullable=False)
    created_datetime = Column(DateTime(timezone=True), server_default=func.now())
    updated_datetime = Column(
        DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )
