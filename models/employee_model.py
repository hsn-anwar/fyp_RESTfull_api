from db import db
from models.office_locations import OfficeLocationModel
from models.model import ModelTemplate


# noinspection PyMethodMayBeStatic
class EmployeeModel(db.Model, ModelTemplate):
    __tablename__ = 'Employee'

    employee_ID = db.Column(db.INTEGER, primary_key=True)
    employee_CNIC = db.Column(db.String(15))
    first_name = db.Column(db.String(35))
    last_name = db.Column(db.String(35))
    email = db.Column(db.String(50))
    passcode = db.Column(db.String(20))
    contact_number = db.Column(db.String(11))
    office_ID = db.Column(db.INTEGER, db.ForeignKey('OfficeLocation.office_ID'))

    atten = db.relationship('AttendanceModel', backref='employee_time')
    loc = db.relationship('LocationsModel', backref='loc_ref')

    def __init__(self, employee_CNIC, first_name, last_name, email, passcode, contact_number, office_ID):
        # self.employee_ID = _id
        self.employee_CNIC = employee_CNIC
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.passcode = passcode
        self.contact_number = contact_number
        self.office_ID = office_ID

    def json(self):
        return \
            {
                'id': self.employee_ID,
                'cnic': self.employee_CNIC,
                'name': self.first_name + ' ' + self.last_name,
                'email': self.email,
                'password': self.passcode,
                'number': self.contact_number,
                'office_id': self.office_ID,
                'flag': True
            }

    def __str__(self):
        return f'Employee ID: {self.employee_ID}\nEmployee CNIC: {self.employee_CNIC}\nFirst Name: {self.first_name}' \
               f'\nLast Name: {self.last_name}\ne_mail: {self.email}\n{self.passcode}Password: {self.visit_location}' \
               f'\nVisit Location: {self.visit_location}\nOffice Location:{self.office_location}\n'

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(employee_ID=_id).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    # @classmethod
    # def get_user_password(cls, email):
    #     return cls.query.filter_by(email=email).first

    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()
    #
    # def delete_from_db(self):
    #     db.session.delete(self)
    #     db.session.commit()
