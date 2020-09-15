from db import db


# noinspection PyMethodMayBeStatic
class ChildModel(db.Model):
    __tablename__ = 'Child'

    child_id = db.Column(db.INTEGER, primary_key=True)

    child_name = db.Column(db.String(35))
    date_of_birth = db.Column(db.Date)

    parent_id = db.Column(db.INTEGER, db.ForeignKey('Parent.parent_ID'))

    def __init__(self,  child_name, date_of_birth, parent_id):
        self.child_name = child_name
        self.date_of_birth = date_of_birth
        self.parent_id = parent_id

    def json(self):
        return \
            {
                'child_id': self.child_id,
                'name': self.child_name,
                'dob': str(self.date_of_birth),
                'parent_id': self.parent_id
            }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(child_id=id).first()
