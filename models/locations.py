from db import db
from models.employee_model import EmployeeModel


# noinspection PyMethodMayBeStatic
class LocationsModel(db.Model):
    __tablename__ = 'Locations'

    locations_ID = db.Column(db.INTEGER, primary_key=True)
    location = db.Column(db.String(1000))
    employee_ID = db.Column(db.INTEGER, db.ForeignKey('Employee.employee_ID'))

    def __init__(self, location, employee_ID):
        self.location = location
        self.employee_ID = employee_ID

    def json(self):
        return {'loc': self.location}

    # @classmethod
    # def find_by_id(cls, _id):
    #     return cls.query.filter_by(attendance_ID=_id).first()
    #
    # @classmethod
    # def find_by_fid(cls, _id):
    #     return EmployeeModel.find_by_id(_id=_id)
    #
    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()
    #
    # def delete_from_db(self):
    #     db.session.delete(self)
    #     db.session.commit()
