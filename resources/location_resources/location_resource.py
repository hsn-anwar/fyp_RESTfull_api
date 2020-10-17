from flask_restful import Resource, reqparse

from models.employee_model import EmployeeModel
from models.locations import LocationsModel


# noinspection PyMethodMayBeStatic
class LocationsResource(Resource):

    def get(self, fid):
        return {'locs': [loc.json() for loc in LocationsModel.query.filter_by(employee_ID=fid).all()]}
