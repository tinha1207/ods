from sqlalchemy import text, Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func, null


from app.database.db import Base


class Record(Base):
    __tablename__ = "record"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    address_id = Column(Integer, ForeignKey("address.id", ondelete="CASCADE"))
    company = Column(String(150), nullable=True, default=null)
    is_household = Column(Boolean, default=False)
    created_datetime = Column(DateTime(timezone=True), server_default=func.now())
    updated_datetime = Column(
        DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )

    address = relationship("Address")
