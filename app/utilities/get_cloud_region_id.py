__author__ = "Supratik Majumdar"
__status__ = "Development"

import sqlalchemy
from ..models import CloudRegion as CloudRegionSchema


def get_cloud_region_id(session, cloud_region: str):
    try:
        record = (
            session.query(CloudRegionSchema)
            .filter(CloudRegionSchema.cloud_region == cloud_region)
            .one()
        )
        return record.id

    except sqlalchemy.orm.exc.NoResultFound:
        return None
