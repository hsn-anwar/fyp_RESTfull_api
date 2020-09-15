from flask_restful import Resource, reqparse

from models.parent_account_model import ParentAccountModel
from models.parent_model import ParentModel


# noinspection PyMethodMayBeStatic
class ParentAcccountResource(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('password', type=str, help='Password not found')
    parser.add_argument('email', type=str, help='email not found')
    parser.add_argument('f_username', type=str)
    parser.add_argument('f_password', type=str)
    parser.add_argument('m_username', type=str)
    parser.add_argument('m_password', type=str)
    parser.add_argument('parent_id', type=int)

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
                        'cnic': parents_info[0]['father_CNIC'],
                        'number': parents_info[0]['father_mobile'],
                        'address': parents_info[0]['father_address'],
                        'flag': True
                    }
                return json
            else:
                return {'Message': 'Incorrect password', 'flag': False}
        elif ParentAccountModel.find_by_m_email(email):
            acc = ParentAccountModel.find_by_m_email(email)
            if data['password'] == acc.m_password:
                parents = ParentModel.find_by_id(acc.parent_id)
                parents_info = parents.json()
                json = \
                    {
                        'id': parents_info[0]['id'],
                        'name': parents_info[0]['mother_first_name'] + ' ' + parents_info[0]['mother_last_name'],
                        'email': email,
                        'cnic': parents_info[0]['mother_CNIC'],
                        'number': parents_info[0]['mother_mobile'],
                        'address': parents_info[0]['mother_address'],
                        'flag': True
                    }
                return json
            else:
                return {'Message': 'Incorrect password', 'flag': False}

        else:
            return {'Message': 'Account not found'}

    def put(self, email):
        data = self.parser.parse_args()

        if ParentAccountModel.find_by_f_email(email):
            acc = ParentAccountModel.find_by_f_email(email)

            if data['email'] and data['email'] != 'null':
                acc.f_username = data['email']
                acc.update_to_db()

            if data['password'] and data['password'] != 'null':
                acc.f_password = data['password']
                acc.update_to_db()

            return {'Message': "Username and/or passoword sucessfully updated", "email": acc.f_username}

        elif ParentAccountModel.find_by_m_email(email):
            acc = ParentAccountModel.find_by_m_email(email)

            if data['email'] and data['email'] != 'null':
                acc.m_username = data['email']
                acc.update_to_db()

            if data['password'] and data['password'] != 'null':
                acc.m_password = data['password']
                acc.update_to_db()

            return {'Message': "Username and/or passoword sucessfully updated", "email": acc.m_username}

        else:
            return {'Message': "Username not found"}
