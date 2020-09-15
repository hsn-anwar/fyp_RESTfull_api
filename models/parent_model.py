from db import db


# noinspection PyMethodMayBeStatic
class ParentModel(db.Model):
    __tablename__ = 'Parent'

    parent_ID = db.Column(db.INTEGER, primary_key=True)

    father_first_name = db.Column(db.String(35))
    father_last_name = db.Column(db.String(35))
    father_CNIC = db.Column(db.String(15))
    father_mobile = db.Column(db.INTEGER)
    father_address = db.Column(db.String(100))

    mother_first_name = db.Column(db.String(35))
    mother_last_name = db.Column(db.String(35))
    mother_CNIC = db.Column(db.String(15))
    mother_mobile = db.Column(db.INTEGER)
    mother_address = db.Column(db.String(100))

    parent_id = db.relationship('ParentAccountModel', backref='parentid')
    child_id = db.relationship('ChildModel', backref='childid')

    def __init__(self, father_first_name, father_last_name, father_CNIC, father_mobile, father_address,
                 mother_first_name, mother_last_name, mother_mobile, mother_CNIC, mother_address):
        self.father_first_name = father_first_name
        self.father_last_name = father_last_name
        self.father_CNIC = father_CNIC
        self.father_mobile = father_mobile
        self.father_address = father_address
        self.mother_first_name = mother_first_name
        self.mother_last_name = mother_last_name
        self.mother_CNIC = mother_CNIC
        self.mother_mobile = mother_mobile
        self.address = mother_address

    def json(self):
        return \
            {
                'id': self.parent_ID,
                'father_first_name': self.father_first_name,
                'father_last_name': self.father_last_name,
                'father_CNIC': self.father_CNIC,
                'father_mobile': self.father_mobile,
                'father_address': self.father_address,
                'mother_first_name': self.mother_first_name,
                'mother_last_name': self.mother_last_name,
                'mother_CNIC': self.mother_CNIC,
                'mother_mobile': self.mother_mobile,
                'mother_address': self.mother_address
            }, 200

    def __str__(self):
        return f'Father name: {self.father_first_name + " " + self.father_last_name}\nFather CNIC: {self.father_CNIC}' \
               f'\n'f'Mother name: {self.mother_first_name + " " + self.mother_last_name}' \
                f'\nMother CNIC: {self.mother_CNIC}'

    @classmethod
    def find_by_father_cnic(cls, cnic):
        return cls.query.filter_by(father_CNIC=cnic).first()

    @classmethod
    def find_by_mother_cnic(cls, cnic):
        return cls.query.filter_by(mother_CNIC=cnic).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(parent_ID=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def update_db(self):
        db.session.commit()