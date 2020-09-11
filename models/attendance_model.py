from datetime import datetime
from models.employee_model import EmployeeModel
from db import db


# noinspection PyMethodMayBeStatic
class AttendanceModel(db.Model):
    __tablename__ = 'Attendance'

    attendance_ID = db.Column(db.INTEGER, primary_key=True)
    attendance_date = db.Column(db.Date)
    attendance_time = db.Column(db.Time)
    employee_ID = db.Column(db.INTEGER, db.ForeignKey('Employee.employee_ID'))

    def __init__(self, employee_ID):
        self.employee_ID = employee_ID

    def json(self):
        print(self.attendance_ID, self.attendance_time, self.attendance_date, self.employee_ID)
        return \
            {
                'Employee ID': self.employee_ID,
                'Attendance ID': self.attendance_ID,
                'Date': str(self.attendance_date),
                'Time': str(self.attendance_time)
            }

    def date_time(self):
        self.attendance_date = datetime.now().date()
        self.attendance_time = datetime.now().time()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(attendance_ID=_id).first()

    @classmethod
    def find_by_fid(cls, _id):
        return EmployeeModel.find_by_id(_id=_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def __str__(self):
        return "Attendance_ID: {}, Employee_ID{}, Date: {}, Time: {}".format(self.attendance_ID, self.employee_ID,
                                                                             self.attendance_date, self.attendance_time)
