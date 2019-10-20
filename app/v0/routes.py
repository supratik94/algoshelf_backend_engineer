__author__ = "Supratik Majumdar"
__status__ = "Development"

from flask import Blueprint
from flask_restful import Api

v0_blueprint = Blueprint(name="v0", import_name=__name__)
v0_api = Api(app=v0_blueprint, prefix="/v0")
