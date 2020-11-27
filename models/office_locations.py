from db import db


# noinspection PyMethodMayBeStatic
class OfficeLocationModel(db.Model):
    __tablename__ = 'OfficeLocation'

    office_ID = db.Column(db.INTEGER, primary_key=True)
    address = db.Column(db.String(1000))
    latitude = db.Column(db.String(20))
    longitude = db.Column(db.String(20))

    emp = db.relationship('EmployeeModel', backref='emp_model')

    def json(self):
        return \
            {
                'address': self.address,
                'lat': float(self.latitude),
                'long': float(self.longitude)
            }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(office_ID=_id).first()
