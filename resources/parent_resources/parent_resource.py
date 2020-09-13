from flask_restful import Resource, reqparse

from models.parent_model import ParentModel


# noinspection PyMethodMayBeStatic
class ParentResource(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('cnic', type=str, help='CNIC not found')

    def get(self):
        data = self.parser.parse_args()
        cnic = data['cnic']
        father = ParentModel.find_by_father_cnic(cnic)
        mother = ParentModel.find_by_mother_cnic(cnic)

        if father:
            return father.json()
        elif mother:
            return mother.json()
        return {'Message': 'Parent not found'}
