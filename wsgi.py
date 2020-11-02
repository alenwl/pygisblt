# Required modules
from flask import Flask
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

@application.route('/historical/')
def historical():
    test = db_queue_monitor()
    data = test.get_historical()
    if data:
        return("Success")
    else:
        return("Fail")

@application.route('/iccp_config/')
def iccp_config():
    test = iccp_config_generator()
    data = test.test()
    if data:
        return(data)
    else:
        return("Fail")

if __name__ == "__main__":
    application.run()
