__author__ = "Supratik Majumdar"
__status__ = "Development"

from app.models import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint


class Status(Base):
    __tablename__ = "MAPPING_STATUS"

    id = Column(
        name="ID", type_=Integer, primary_key=True, autoincrement=True, nullable=False
    )
    status = Column(name="STATUS", type_=String(255), nullable=False)

    __table_args__ = (UniqueConstraint("STATUS", name="STATUS_UNIQUE_KEY"),)
