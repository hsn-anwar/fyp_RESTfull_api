from db import db

from models.parent_model import ParentModel


# noinspection PyMethodMayBeStatic
class ParentAccountModel(db.Model):
    __tablename__ = 'ParentAccount'

    account_ID = db.Column(db.INTEGER, primary_key=True)
    f_username = db.Column(db.String(50))
    f_password = db.Column(db.String(20))
    m_username = db.Column(db.String(50))
    m_password = db.Column(db.String(20))
    parent_id = db.Column(db.INTEGER, db.ForeignKey('Parent.parent_ID'))

    def __init__(self, f_username, f_password, m_username, m_password, parent_id):
        self.f_username = f_username
        self.f_password = f_password
        self.m_username = m_username
        self.m_password = m_password
        self.parent_id = parent_id

    def json(self):
        return \
            {
                'f_username': self.f_username,
                'f_password': self.f_password,
                'm_username': self.m_username,
                'm_password': self.m_password,
                'parent_id': self.parent_id
            }

    @classmethod
    def find_by_f_email(cls, username):
        return cls.query.filter_by(f_username=username).first()

    @classmethod
    def find_by_m_email(cls, username):
        return cls.query.filter_by(m_username=username).first()

    @classmethod
    def find_by_fid(cls, _id):
        return cls.find_by_id(_id=_id)

    @classmethod
    def find_by_fcnic(cls, cnic):
        return ParentModel.find_by_father_cnic()

    @classmethod
    def find_by_mcnic(cls, cnic):
        return ParentModel.find_by_mother_cnic()

    def update_to_db(self):
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
