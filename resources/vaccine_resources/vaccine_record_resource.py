import datetime

from flask_restful import Resource, reqparse

from models.vaccine_record_model import VaccineRecordModel
from models.child_model import ChildModel


# noinspection PyMethodMayBeStatic
class VaccinrRecordResource(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('vac_name', type=str, help='Vaccine name not found')
    parser.add_argument('child_id', type=int, help='Child ID not found')
    parser.add_argument('emp_id', type=int, help='Employee ID not found')

    def post(self):
        data = self.parser.parse_args()

        vac_name = data['vac_name']
        emp_id = data['emp_id']
        child_id = data['child_id']

        if ChildModel.find_by_id(id=child_id):
            datetimestamp = datetime.datetime.now()
            doa = datetimestamp.date()
            toa = datetimestamp.time()
            vac = VaccineRecordModel(vac_name=vac_name, doa=doa, toa=toa,emp_id=emp_id, child_id=child_id)
            vac.update_db()
            vac.save_to_db()
            return {'Message': 'Database updated'}, 200
        else:
            return {'Message': 'Someting went wrong'}, 400
