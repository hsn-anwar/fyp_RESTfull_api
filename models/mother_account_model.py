from db import db

from models.parent_model import ParentModel


# noinspection PyMethodMayBeStatic
class MotherAccountModel(db.Model):
    __tablename__ = 'MotherAccount'

    mother_ID = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(50))
    passcode = db.Column(db.String(20))
    # parent_id = db.relationship('ParentModel', backref='parent_id')
    # employee_ID = db.Column(db.INTEGER, db.ForeignKey('Employee.employee_ID'))
    parent_id = db.Column(db.INTEGER, db.ForeignKey('Parent.parent_ID'))

    def __init__(self, username, passcode, parent_id):
        self.username = username
        self.passcode = passcode
        self.parent_id = parent_id

    def json(self):
        return \
            {
                'username': self.username,
                'password': self.passcode,
                'parent_id': self.parent_id
            }

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_fid(cls, _id):
        return cls.find_by_id(_id=_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
