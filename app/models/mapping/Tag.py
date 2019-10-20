__author__ = "Supratik Majumdar"
__status__ = "Development"

from app.models import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint


class Tag(Base):
    __tablename__ = "MAPPING_TAG"

    id = Column(
        name="ID", type_=Integer, primary_key=True, autoincrement=True, nullable=False
    )
    cloud_region = Column(name="TAG", type_=String(255), nullable=False)

    __table_args__ = (UniqueConstraint("TAG", name="TAG_UNIQUE_KEY"),)
