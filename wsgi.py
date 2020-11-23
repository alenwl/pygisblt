# Required modules
from flask import Flask
from flask import request
from flask import Response
from flask import send_file
import time
from src.mysql_database_modules.db_queue_monitor import *
from src.blt_generation_modules.iccp_config_generator import *
from src.blt_generation_modules.rcc_generator import *
from src.blt_generation_modules.network_config_generator import *
from src.authentication.validate_client import *
application = Flask(__name__)
from xml.etree import ElementTree

@application.route('/dbtest/')
def dbtest():
    test = db_queue_monitor()
    if test.check_connectivity():
        return('Successful connection to db')
    else:
        return('Failed connecting to db')

@application.route('/iccptest/')
def iccptest():
    test = iccp_config_generator()
    data = test.test()
    if data:
        return('Success')
    else:
        return('Failed starting iccp config module')

@application.route('/historical/')
def historical():
    test = db_queue_monitor()
    data = test.get_historical()
    if data:
        return('Success')
    else:
        return('Fail')

@application.route('/api')
def apitest():
    # Validate key and client_id
    validate = validate_client()
    if validate.check_client(request.headers.get('API-Key'),request.headers.get('client_id')):
        if request.args.get('type') == 'iccp':
            iccp = iccp_config_generator()
            return Response(iccp.generate(),mimetype='text/xml')
        elif request.args.get('type') == 'network_config':
            nc = network_config_generator()
            return Response(nc.generate(),mimetype='text/xml')
        elif request.args.get('type') == 'rcc':
            rcc = rcc_generator()
            return Response(rcc.generate(),mimetype='text/xml')
        else:
            return 'Invalid type'
    else:
        return 'Invalid key/client_id'

if __name__ == '__main__':
    application.run()
