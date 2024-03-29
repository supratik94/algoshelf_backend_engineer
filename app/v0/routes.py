__author__ = "Supratik Majumdar"
__status__ = "Development"

from flask import Blueprint
from flask_restful import Api

from .resources import CloudRegion, Status, InstanceType

v0_blueprint = Blueprint(name="v0", import_name=__name__)
v0_api = Api(app=v0_blueprint, prefix="/v0")

v0_api.add_resource(CloudRegion, "/cloud_regions/")
v0_api.add_resource(Status, "/statuses/")
v0_api.add_resource(InstanceType, "/instance_types/")
