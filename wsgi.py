# Required modules
from flask import Flask
import time
from src.mysql_database_modules.db_queue_monitor import *
application = Flask(__name__)

@application.route('/dbtest/')
def dbtest():
    test = db_queue_monitor()
    if test.check_connectivity():
        return("Successful connection to db")
    else:
        return("Failed connecting to db")

if __name__ == "__main__":
    application.run()
