__author__ = "Supratik Majumdar"
__status__ = "Development"

from app.models import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey

from ..mapping import Status, CloudRegion


class Cluster(Base):
    __tablename__ = "CLUSTER"

    id = Column(
        name="ID", type_=Integer, primary_key=True, autoincrement=True, nullable=False
    )
    name = Column(name="NAME", type_=String(255), nullable=False)
    cloud_region_id = Column(
        ForeignKey(
            CloudRegion.id,
            name="CLOUD_REGION_ID_FOREIGN_KEY",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        name="CLOUD_REGION_ID",
        type_=Integer,
        nullable=False,
    )
    cluster_status_id = Column(
        ForeignKey(
            Status.id,
            name="CLUSTER_STATUS_ID_FOREIGN_KEY",
            onupdate="CASCADE",
            ondelete="RESTRICT",
        ),
        name="CLUSTER_STATUS_ID",
        nullable=False,
        default=1,
    )

    __table_args__ = (UniqueConstraint("NAME", name="CLUSTER_NAME_UNIQUE_KEY"),)
