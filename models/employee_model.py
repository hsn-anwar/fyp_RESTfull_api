from db import db


# noinspection PyMethodMayBeStatic
class EmployeeModel(db.Model):
    __tablename__ = 'Employee'

    employee_ID = db.Column(db.INTEGER, primary_key=True)
    employee_CNIC = db.Column(db.String(15))
    first_name = db.Column(db.String(35))
    last_name = db.Column(db.String(35))
    email = db.Column(db.String(50))
    passcode = db.Column(db.String(20))
    visit_location = db.Column(db.String(50))
    office_location = db.Column(db.String(50))
    atten = db.relationship('AttendanceModel', backref='employee_time')

    def __init__(self, employee_CNIC, first_name, last_name, email, passcode, visit_location, office_location):
        # self.employee_ID = _id
        self.employee_CNIC = employee_CNIC
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.passcode = passcode
        self.visit_location = visit_location
        self.office_location = office_location

    def json(self):
        return \
            {
                'employee_ID': self.employee_ID,
                'employee_CNIC': self.employee_CNIC,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'password': self.passcode,
                'visit_location': self.visit_location,
                'office_location': self.office_location
            }, 200

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

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
