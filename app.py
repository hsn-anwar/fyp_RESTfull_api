from flask import Flask
from flask_restful import Api
import socket

from resources.employee_resources.employee import EmployeeResource
from resources.employee_resources.employee_login import EmployeeAccountResource


from resources.attendance import AttendanceResource, AttendanceList

from resources.parent_resources.parent_resource import ParentResource
from resources.parent_resources.parent_account_resource import ParentAcccountResource
from resources.parent_resources.password_resource import PasswordResource
from resources.child.child_resource import ChildResource, ChildList, ChildParentResource, ChildToken

from resources.location_resources.location_resource import LocationsResource
from resources.location_resources.office_location_resource import OfficeLocationsResource

from resources.vaccine_resources.vaccine_name_resource import VaccineNameList
from resources.vaccine_resources.vaccine_record_resource import VaccineRecordResource


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/online_vrs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'hellothere'
api = Api(app)

api.add_resource(EmployeeResource, '/employee/<int:_id>')
api.add_resource(EmployeeAccountResource, '/employee/account/<string:email>')

api.add_resource(AttendanceResource, '/attendance/<int:_id>')
api.add_resource(AttendanceList, '/attendancelist')

api.add_resource(ParentResource, '/parent')
api.add_resource(ChildParentResource, '/parent_info/<int:pid>')

api.add_resource(ParentAcccountResource, '/parent_account/<string:email>')

api.add_resource(PasswordResource, '/parent_account/password/<string:email>')

api.add_resource(ChildResource, '/child/<int:id>')
api.add_resource(ChildList, '/childlist/<int:fid>')

api.add_resource(LocationsResource, '/visit_locations/<int:fid>')
api.add_resource(OfficeLocationsResource, '/office_location/<int:fid>')

api.add_resource(VaccineNameList, '/vaccine_list')

api.add_resource(VaccineRecordResource, '/vaccine_records/<int:fid>')

api.add_resource(ChildToken, '/child_token')

if __name__ == '__main__':
    from db import db

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    db.init_app(app)
    print(str(ip_address))
    app.run(host=str(ip_address), port=5000, debug=True)
    # app.run(host='192.168.1.184', port=5000, debug=True)
