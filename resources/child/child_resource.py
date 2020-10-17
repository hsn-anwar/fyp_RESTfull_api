import secrets
import string

from flask_restful import Resource, reqparse

from models.child_model import ChildModel


# noinspection PyMethodMayBeStatic
class ChildResource(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument('email', type=str, required=True, help='Employee email not found'
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Vaccine name not found')
    parser.add_argument('id', type=int, required=True, help='Child ID not found')

    def get(self, id):
        #  TODO: ENCRYPT THIS SHIT
        child = ChildModel.find_by_id(id)
        return child.json()


# noinspection PyMethodMayBeStatic
class ChildList(Resource):

    def get(self, fid):
        return {'Children': [child.json() for child in ChildModel.query.filter_by(parent_id=fid).all()]}


# noinspection PyMethodMayBeStatic
class ChildParentResource(Resource):

    def get(self, pid):
        parentInfo = ChildModel.find_parents(pid=pid)
        json = \
            {
                'father': parentInfo.father_first_name + ' ' + parentInfo.father_last_name,
                'mother': parentInfo.mother_first_name + ' ' + parentInfo.mother_last_name
            }
        return json


# noinspection PyMethodMayBeStatic
class ChildToken(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('token', type=str)
    parser.add_argument('id', type=int)

    def put(self):
        data = self.parser.parse_args()
        child_id = data['id']
        token = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        print(token)
        child = ChildModel.find_by_id(child_id)

        if child:
            child.Token = token
            child.save_to_db()
            return {"Token": child.Token}

    def post(self):
        data = self.parser.parse_args()
        token = data['token']
        # return cls.query.filter_by(child_id=id).first()
        child = ChildModel.query.filter_by(Token=token).first()
        if child:
            child.Token = None
            child.update_db()
            print(child.json())
            return child.json()
        else:
            return {"Message": "Token not found"}, 400
