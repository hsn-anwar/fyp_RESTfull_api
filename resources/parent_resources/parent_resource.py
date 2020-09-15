from flask_restful import Resource, reqparse

from models.parent_model import ParentModel


# noinspection PyMethodMayBeStatic
class ParentResource(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('cnic', type=str, help='CNIC not found')
    parser.add_argument('mobile', type=int, help='mobile not found')
    parser.add_argument('address', type=str, help='address not found')


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

    def put(self):

        data = self.parser.parse_args()
        cnic = data['cnic']
        if ParentModel.find_by_father_cnic(cnic):
            acc = ParentModel.find_by_father_cnic(cnic)

            if data['mobile'] != 'null':
                acc.father_mobile = data['mobile']
                acc.update_db()

            if data['address'] != 'null':
                acc.father_address = data['address']
                acc.update_db()

            return {'Message': "ContactInfo and/or address sucessfully updated", 'mobile': acc.father_mobile, "address": acc.father_address}

        elif ParentModel.find_by_mother_cnic(cnic):
            acc = ParentModel.find_by_mother_cnic(cnic)
            print(acc)
            if data['mobile'] != 'null':
                mobile = data['mobile']
                acc.mother_mobile = int(mobile)
                acc.update_db()

            if data['address'] != 'null':
                acc.mother_address = data['address']
                acc.update_db()

            return {'Message': "ContactInfo and/or address sucessfully updated", "mobile": acc.mother_mobile, "address": acc.mother_address}

        else:
            return {'Message': "ERROR"}

