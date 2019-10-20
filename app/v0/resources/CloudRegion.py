__author__ = "Supratik Majumdar"
__status__ = "Development"

from .Resource import API_Resource_v0
from ...models import CloudRegion as CloudRegionSchema


class CloudRegion(API_Resource_v0):
    def get(self):
        cloud_regions = list()
        results = self.session.query(CloudRegionSchema).all()
        for result in results:
            cloud_regions.append(result.cloud_region)

        return cloud_regions
