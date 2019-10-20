__author__ = "Supratik Majumdar"
__status__ = "Development"

from app.models import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint


class InstanceType(Base):
    __tablename__ = "MAPPING_INSTANCE_TYPE"

    id = Column(
        name="ID", type_=Integer, primary_key=True, autoincrement=True, nullable=False
    )
    cloud_region = Column(name="CLOUD_REGION", type_=String(255), nullable=False)

    __table_args__ = (UniqueConstraint("CLOUD_REGION", name="CLOUD_REGION_UNIQUE_KEY"),)
