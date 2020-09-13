from flask_restful import Resource, reqparse

from models.parent_account_model import ParentAccountModel
from models.parent_model import ParentModel


# noinspection PyMethodMayBeStatic
class ParentAcccountResource(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('password', type=str, help='Password not found')

    def post(self, email):
        data = self.parser.parse_args()

        if ParentAccountModel.find_by_f_email(email):
            acc = ParentAccountModel.find_by_f_email(email)
            if data['password'] == acc.f_password:
                parents = ParentModel.find_by_id(acc.parent_id)
                parents_info = parents.json()
                json = \
                    {
                        'id': parents_info[0]['id'],
                        'name': parents_info[0]['father_first_name'] + ' ' + parents_info[0]['father_last_name'],
                        'email': email,
                        'cnic': parents_info[0]['father_CNIC']
                    }
                return json
            else:
                return {'Message': 'Incorrect password'}
        elif ParentAccountModel.find_by_m_email(email):
            acc = ParentAccountModel.find_by_m_email(email)
        else:
            return {'Message': 'Account not found'}
