__author__ = "Supratik Majumdar"
__status__ = "Development"

from app.models import Base
from sqlalchemy import Column, Integer, UniqueConstraint, ForeignKey

from .Cluster import Cluster
from ..instance import Instance


class ClusterInstanceRelationship(Base):
    __tablename__ = "CLUSTER_INSTANCE_RELATIONSHIP"

    id = Column(
        name="ID", type_=Integer, primary_key=True, autoincrement=True, nullable=False
    )
    cluster_id = Column(
        ForeignKey(
            Cluster.id,
            name="CLUSTER_ID_FOREIGN_KEY",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        name="CLUSTER_ID",
        type_=Integer,
        nullable=False,
    )
    instance_id = Column(
        ForeignKey(
            Instance.id,
            name="CLUSTER_INSTANCE_RELATIONSHIP_INSTANCE_ID_FOREIGN_KEY",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        name="INSTANCE_ID",
        type_=Integer,
        nullable=False,
    )

    __table_args__ = (
        UniqueConstraint(
            "INSTANCE_ID", name="INSTANCE_ID_CLUSTER_INSTANCE_RELATIONSHIP_UNIQUE_KEY"
        ),
        UniqueConstraint(
            "CLUSTER_ID",
            "INSTANCE_ID",
            name="CLUSTER_ID_INSTANCE_ID_CLUSTER_INSTANCE_RELATIONSHIP_UNIQUE_KEY",
        ),
    )
