# Required modules
from flask import Flask
from flask import request
import time
from src.mysql_database_modules.db_queue_monitor import *
from src.blt_generation_modules.iccp_config_generator import *
application = Flask(__name__)

@application.route('/dbtest/')
def dbtest():
    test = db_queue_monitor()
    if test.check_connectivity():
        return("Successful connection to db")
    else:
        return("Failed connecting to db")

@application.route('/iccptest/')
def iccptest():
    test = iccp_config_generator()
    data = test.test()
    if data:
        return("Success")
    else:
        return("Failed starting iccp config module")

@application.route('/historical/')
def historical():
    test = db_queue_monitor()
    data = test.get_historical()
    if data:
        return("Success")
    else:
        return("Fail")

@application.route('/api')
def apitest():
    key = request.headers.get('key')
    return(key)

if __name__ == "__main__":
    application.run()
