__author__ = "Supratik Majumdar"
__status__ = "Development"

from app.models import Base
from sqlalchemy import Column, Integer, UniqueConstraint, ForeignKey

from .Instance import Instance
from ..mapping import Tag


class InstanceTagRelationship(Base):
    __tablename__ = "INSTANCE_TAG_RELATIONSHIP"

    id = Column(
        name="ID", type_=Integer, primary_key=True, autoincrement=True, nullable=False
    )
    instance_id = Column(
        ForeignKey(
            Instance.id,
            name="INSTANCE_TAG_RELATIONSHIP_INSTANCE_ID_FOREIGN_KEY",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        name="INSTANCE_ID",
        type_=Integer,
        nullable=False,
    )
    tag_id = Column(
        ForeignKey(
            Tag.id, name="TAG_ID_FOREIGN_KEY", onupdate="CASCADE", ondelete="CASCADE"
        ),
        name="TAG_ID",
        type_=Integer,
        nullable=False,
    )

    __table_args__ = (
        UniqueConstraint(
            "INSTANCE_ID",
            "TAG_ID",
            name="INSTANCE_ID_TAG_ID_CLUSTER_INSTANCE_TAG_RELATIONSHIP_UNIQUE_KEY",
        ),
    )
