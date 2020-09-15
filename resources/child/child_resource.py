from flask_restful import Resource, reqparse

from models.child_model import ChildModel


# noinspection PyMethodMayBeStatic
class ChildResource(Resource):

    # parser = reqparse.RequestParser()
    # parser.add_argument('email', type=str, required=True, help='Employee email not found')

    def get(self, id):
        #  TODO: ENCRYPT THIS SHIT
        child = ChildModel.find_by_id(id)
        return child.json()


# noinspection PyMethodMayBeStatic
class ChildList(Resource):

    def get(self, fid):
        return {'Children': [child.json() for child in ChildModel.query.filter_by(parent_id=fid).all()]}
