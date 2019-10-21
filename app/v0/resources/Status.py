__author__ = "Supratik Majumdar"
__status__ = "Development"

from .Resource import API_Resource_v0
from ...models import Status as StatusSchema


class Status(API_Resource_v0):
    def get(self):
        statuses = list()
        results = self.session.query(StatusSchema).all()
        for result in results:
            statuses.append(result.status)

        return statuses
