
from flask_restful import Resource, reqparse

from models.attendance_model import AttendanceModel


# noinspection PyMethodMayBeStatic
class AttendanceResource(Resource):

    def get(self, _id):
        atten = AttendanceModel.find_by_id(_id=_id)
        if atten: 
            return atten.json(), 200
        else:
            return {'Message': 'ID not found'}, 400

    def post(self, _id):
        if AttendanceModel.find_by_fid(_id):
            atten = AttendanceModel(employee_ID=_id)
            atten.date_time()
            atten.save_to_db()
            return {'Message': 'Attendance marked'.format(_id)}, 200
        return {'Message': 'Employee with ID {} does not exist'.format(_id)}, 400


# noinspection PyMethodMayBeStatic
class AttendanceList(Resource):

    def get(self):
        return {'Attendance List: ': [atten.json() for atten in AttendanceModel.query.all()]}

    def delete(self):
        [atten.delete_from_db() for atten in AttendanceModel.query.all()]
