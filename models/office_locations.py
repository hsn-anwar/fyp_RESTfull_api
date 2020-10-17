from db import db


# noinspection PyMethodMayBeStatic
class OfficeLocationModel(db.Model):
    __tablename__ = 'OfficeLocation'

    office_ID = db.Column(db.INTEGER, primary_key=True)
    address = db.Column(db.String(1000))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    emp = db.relationship('EmployeeModel', backref='emp_model')

    def json(self):
        return \
            {
                'address': self.address,
                'lat': self.latitude,
                'long': self.longitude
            }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(office_ID=_id).first()
