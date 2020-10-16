from flask import Flask
import time
from src.mysql_database_modules.db_queue_monitor import *
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route('/dbtest/')
def test_al():
    test = db_queue_monitor()
    if test.check_connectivity():x
        return("Successful connection to db")
    else:
        return("Failed connecting to db")

if __name__ == "__main__":
    application.run()
