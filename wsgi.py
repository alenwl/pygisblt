# Required modules
from flask import Flask
from flask import request
from flask import Response
from flask import send_file
import time
from src.mysql_database_modules.db_queue_monitor import *
from src.blt_generation_modules.iccp_config_generator import *
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
    # Temporary 
    my_key = 'ander'
    key = request.headers.get('API-Key')
    if my_key==key:
        if request.args.get('type') == 'iccp':
            xml = ElementTree.Element('Type', Name='iccp_config')
            xml_str = ElementTree.tostring(xml,encoding='unicode')
            return Response(xml_str,mimetype='text/xml')
        elif request.args.get('type') == 'network_config':
            xml = ElementTree.Element('Type', Name='network_config')
            xml_str = ElementTree.tostring(xml,encoding='unicode')
            return Response(xml_str,mimetype='text/xml')
        elif request.args.get('type') == 'rcc':
            xml = ElementTree.Element('Type', Name='rcc')
            xml_str = ElementTree.tostring(xml,encoding='unicode')
            return Response(xml_str,mimetype='text/xml')
        else:
            return 'Invalid type'
    else:
        return 'Invalid key'

if __name__ == '__main__':
    application.run()
