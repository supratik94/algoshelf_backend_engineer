__author__ = "Supratik Majumdar"
__status__ = "Development"

from app.models import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint


class InstanceType(Base):
    __tablename__ = "MAPPING_INSTANCE_TYPE"

    id = Column(
        name="ID", type_=Integer, primary_key=True, autoincrement=True, nullable=False
    )
    instance_type = Column(name="INSTANCE_TYPE", type_=String(255), nullable=False)

    __table_args__ = (
        UniqueConstraint("INSTANCE_TYPE", name="INSTANCE_TYPE_UNIQUE_KEY"),
    )
