from db import db


# noinspection PyMethodMayBeStatic
class VaccineNameModel(db.Model):
    __tablename__ = 'VaccineNames'
    vaccine_name_ID = db.Column(db.INTEGER, primary_key=True)
    vaccine_name = db.Column(db.String(50))

    def __init__(self, vaccine_name, vaccine_name_ID):
        self.vaccine_name = vaccine_name
        self.vaccine_name_ID = vaccine_name_ID

    def json(self):
        return \
            {
                'name': self.vaccine_name,
                'id': self.vaccine_name_ID
            }
