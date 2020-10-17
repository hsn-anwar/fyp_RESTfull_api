from flask_restful import Resource, reqparse

from models.employee_model import EmployeeModel


# noinspection PyMethodMayBeStatic
class EmployeeResource(Resource):
    parser = reqparse.RequestParser()

    # Add Parser Arguments
    # parser.add_argument('key', type=data_tyoe, required=True/False, help='Help message'
    # parser.add_argument('employee_ID', type=str, required=True, help='Employee ID not found')
    # parser.add_argument('employee_CNIC', type=str, help='Employee CNIC not found')
    # parser.add_argument('first_name', type=str, help='Employee first name not found')
    # parser.add_argument('last_name', type=str, help='Employee last name not found')
    parser.add_argument('email', type=str, help='Employee email not found')
    parser.add_argument('passcode', type=str, help='Employee password not found')
    parser.add_argument('new', type=str, help='Employee new password not found')
    parser.add_argument('phone', type=str, help='Phone not found')

    # parser.add_argument('visit_location', type=str, help='Employee visit location not found')
    # parser.add_argument('office_location', type=str, help='Employee office location not found')

    def get(self, _id):
        emp = EmployeeModel.find_by_id(_id=_id)
        if emp:
            return emp.json()
        else:
            return {'Message': 'Employee not found'}

    # def post(self, _id):
    #     if not EmployeeModel.find_by_id(_id=_id):
    #         data = self.parser.parse_args()
    #         emp = EmployeeModel(**data)
    #         emp.save_to_db()
    #         return {'Message': 'Employee created'}, 200
    #     return {'Message': 'Employee already exists'}, 400

    def post(self, _id):
        if EmployeeModel.find_by_id(_id=_id):
            emp = EmployeeModel.find_by_id(_id=_id)
            data = self.parser.parse_args()

            if data['passcode'] == emp.passcode:
                emp.passcode = data['new']
                emp.update_db()
                return {"flag": True}, 200
            else:
                return {"flag": False}


    def put(self, _id):
        if EmployeeModel.find_by_id(_id=_id):
            emp = EmployeeModel.find_by_id(_id=_id)
            data = self.parser.parse_args()

            if data['email'] != 'null':
                emp.email = data['email']
                emp.update_db()
            if data['phone'] != 'null':
                emp.contact_number = data['phone']
                emp.update_db()

            return {'Message': "ContactInfo and/or email sucessfully updated", 'email': emp.email,
                    "phone": emp.contact_number}

        else:
            return {'Message': "ERROR"}

    def delete(self):
        pass
