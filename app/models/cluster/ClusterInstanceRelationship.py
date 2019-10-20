__author__ = "Supratik Majumdar"
__status__ = "Development"

from app.models import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey


class ClusterInstanceRelationship(Base):
    __tablename__ = "CLUSTER_INSTANCE_RELATIONSHIP"

    id = Column(
        name="ID", type_=Integer, primary_key=True, autoincrement=True, nullable=False
    )
    cluster_id = Column(name="CLUSTER_ID", type_=Integer, nullable=False)
    instance_id = Column(name="INSTANCE_ID", type_=Integer, nullable=False)

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
