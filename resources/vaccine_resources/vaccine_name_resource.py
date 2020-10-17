from flask_restful import Resource, reqparse

from models.vaccine_name_model import VaccineNameModel


# noinspection PyMethodMayBeStatic
class VaccineNameList(Resource):

    def get(self):
        return {'names': [vacc.json() for vacc in VaccineNameModel.query.all()]}
