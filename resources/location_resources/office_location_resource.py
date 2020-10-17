from flask_restful import Resource, reqparse

from models.office_locations import OfficeLocationModel


# noinspection PyMethodMayBeStatic
class OfficeLocationsResource(Resource):

    def get(self, fid):

        if OfficeLocationModel.find_by_id(fid):
            return OfficeLocationModel.find_by_id(fid).json()
        else:
            return {'Message': 'Not Found'}
