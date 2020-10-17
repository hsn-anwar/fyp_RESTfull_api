from db import db
from models.model import ModelTemplate


# noinspection PyMethodMayBeStatic
class VaccineRecordModel(db.Model, ModelTemplate):
    __tablename__ = 'VaccineRecord'
    vaccine_ID = db.Column(db.INTEGER, primary_key=True)
    vaccine_name = db.Column(db.String(50))
    date_of_administration = db.Column(db.DATE)
    time_of_administration = db.Column(db.Time)
    employee_ID = db.Column(db.INTEGER)
    child_id = db.Column(db.INTEGER)

    def __init__(self, vac_name, doa, toa, emp_id, child_id):
        self.vaccine_name = vac_name
        self.date_of_administration = doa
        self.time_of_administration = toa
        self.employee_ID = emp_id
        self.child_id = child_id

    def json(self):
        return \
            {
                'name': self.vaccine_name,
                'id': self.vaccine_name_ID
            }
