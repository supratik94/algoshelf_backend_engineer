__author__ = "Supratik Majumdar"
__status__ = "Development"

from .Resource import API_Resource_v0
from ...models import InstanceType as InstanceTypeSchema


class InstanceType(API_Resource_v0):
    def get(self):
        instance_types = list()
        results = self.session.query(InstanceTypeSchema).all()
        for result in results:
            instance_types.append(result.instance_type)

        return instance_types
