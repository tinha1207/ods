from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database.db import Base


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True)
    file_name = Column(String(255))
    upload_date = Column(DateTime(timezone=True), server_default=func.now())

    records = relationship("Record", back_populates="transaction")
