import datetime

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
    readministration_date = db.Column(db.DATE)

    def __init__(self, vac_name, doa, toa, emp_id, child_id, dor):
        self.vaccine_name = vac_name
        self.date_of_administration = doa
        self.time_of_administration = toa
        self.employee_ID = emp_id
        self.child_id = child_id
        self.readministration_date = dor

    def json(self):
        return {'vaccine': self.vaccine_name, 'doa': str(self.reverse_doa()), 'toa': str(self.time_of_administration),
                'dor': str(self.readministration_date)}

    def reverse_doa(self):
        return datetime.datetime.strptime(str(self.date_of_administration), "%Y-%m-%d").strftime("%d-%m-%Y")

    def reverse_dor(self, dor):
        return datetime.datetime.strptime(str(self.readministration_date), "%Y%m%d").strftime("%d%m%Y")
