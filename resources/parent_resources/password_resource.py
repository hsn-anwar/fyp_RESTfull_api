from flask_restful import Resource, reqparse

from models.parent_account_model import ParentAccountModel
from models.parent_model import ParentModel


# noinspection PyMethodMayBeStatic
class PasswordResource(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('password', type=str, help='Password not found')
    parser.add_argument('new', type=str)

    def post(self, email):
        data = self.parser.parse_args()
        if ParentAccountModel.find_by_f_email(email):
            acc = ParentAccountModel.find_by_f_email(email)
            if data['password'] == acc.f_password:
                acc.f_password = data['new']
                acc.update_to_db()
                return {'password': acc.f_password, 'flag': True}
            else:
                return {'Message': 'Incorrect password', 'flag': False}

        elif ParentAccountModel.find_by_m_email(email):
            acc = ParentAccountModel.find_by_m_email(email)
            if data['password'] == acc.m_password:
                acc.m_password = data['new']
                acc.update_to_db()
                return {'password': acc.m_password, 'flag': True}
            else:
                return {'Message': 'Incorrect password', 'flag': False}

        else:
            return {'Message': 'Account not found'}

