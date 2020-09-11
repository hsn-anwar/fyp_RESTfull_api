from flask import Flask
from flask_restful import Api

from resources.employee_resources.employee import EmployeeResource
from resources.employee_resources.employee_login import EmployeeAccountResource
from resources.attendance import AttendanceResource, AttendanceList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost/online_vrs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'hellothere'
api = Api(app)

api.add_resource(EmployeeResource, '/employee/<int:_id>')
api.add_resource(EmployeeAccountResource, '/employee/account/<string:email>')
api.add_resource(AttendanceResource, '/attendance/<int:_id>')
api.add_resource(AttendanceList, '/attendance_list')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(host='192.168.1.5', port=5000, debug=True)
