__author__ = "Supratik Majumdar"
__status__ = "Development"

from app.models import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey

from ..mapping import Status, InstanceType


class Instance(Base):
    __tablename__ = "INSTANCE"

    id = Column(
        name="ID", type_=Integer, primary_key=True, autoincrement=True, nullable=False
    )
    name = Column(name="NAME", type_=String(255), nullable=False)
    ip_address = Column(name="IP_ADDRESS", type_=String(255), nullable=False)
    instance_type_id = Column(
        ForeignKey(
            Status.id,
            name="INSTANCE_TYPE_ID_FOREIGN_KEY",
            onupdate="CASCADE",
            ondelete="RESTRICT",
        ),
        name="INSTANCE_TYPE_ID",
        type_=Integer,
        nullable=False,
    )
    instance_status_id = Column(
        ForeignKey(
            InstanceType.id,
            name="INSTANCE_STATUS_ID_FOREIGN_KEY",
            onupdate="CASCADE",
            ondelete="RESTRICT",
        ),
        name="INSTANCE_STATUS_ID",
        type_=Integer,
    )

    __table_args__ = (
        UniqueConstraint("IP_ADDRESS", name="INSTANCE_IP_ADDRESS_UNIQUE_KEY"),
    )
