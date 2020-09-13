from flask_restful import Resource, reqparse

from models.employee_model import EmployeeModel


# noinspection PyMethodMayBeStatic
class EmployeeAccountResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help='Employee email not found')
    parser.add_argument('passcode', type=str, required=True, help='Employee password not found')
    parser.add_argument('new_password', type=str)

    def post(self, email):
        employee = EmployeeModel.find_by_email(email=email)
        if not employee:
            return {"Message": "User with email '{}' does not exist".format(email)}, 400
        else:
            data = self.parser.parse_args()
            if data['passcode'] == employee.passcode:
                return {'EmployeeID': employee.employee_ID}
            else:
                return {'Message': 'Incorrect password'}

    def put(self, email):
        employee = EmployeeModel.find_by_email(email=email)
        if not employee:
            return {"Message": "User with email '{}' does not exist".format(email)}, 400
        else:
            data = self.parser.parse_args()
            if data['passcode'] == employee.passcode:
                employee.passcode = data['new_password']
                employee.save_to_db()
                return employee.json()
            else:
                return {"Message": "Incorrect password"}, 400
