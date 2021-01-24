from flask_restful import Resource, reqparse

from models.parent_account_model import ParentAccountModel

z
# noinspection PyMethodMayBeStatic
class MotherAcccountResource(Resource):
    parser = reqparse.RequestParser()

    def get(self, email):
        # acc = MotherAccountModel.find_by_username(email)
        acc = ParentAccountModel.find_by_m_email(username=email)

        if acc:
            return acc.json()
        else:
            return {'Message': 'Account not found'}
