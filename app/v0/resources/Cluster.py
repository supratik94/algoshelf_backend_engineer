__author__ = "Supratik Majumdar"
__status__ = "Development"

import sqlalchemy
from flask_restful import reqparse
from .Resource import API_Resource_v0
from ...models import Cluster as ClusterSchema

from ...utilities import get_cloud_region_id


class Cluster(API_Resource_v0):
    def get(self):
        pass

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "name",
            help="name of the cluster to be created",
            required=True,
            type=str,
            location="json",
        )
        parser.add_argument(
            "cloud_region",
            help="cloud_region for cluster to be created in",
            required=True,
            type=str,
            location="json",
        )
        data = parser.parse_args()

        cloud_region_id = get_cloud_region_id(
            session=self.session, cloud_region=data["cloud_region"]
        )

        if cloud_region_id is None:
            return {"message": "cloud_region does not exist"}, 400

        else:
            return self.create_cluster(
                cloud_region_id=cloud_region_id, cluster_name=data["name"]
            )

    def create_cluster(self, cloud_region_id: int, cluster_name: str):

        cluster = ClusterSchema(name=cluster_name, cloud_region_id=cloud_region_id)

        try:
            self.session.add(cluster)
            self.session.commit()

            print("Created cluster")
            return {"message": "{} cluster created".format(cluster_name)}

        except sqlalchemy.exc.IntegrityError as e:
            self.session.rollback()
            error_message = e.args[0]
            if "CLUSTER_NAME_UNIQUE_KEY" in error_message:
                return {"message": "cluster name already in use"}, 400
