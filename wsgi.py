from flask import Flask
import time
from src.mysql_database_modules.db_queue_monitor import *
application = Flask(__name__)
import pathlib

@application.route("/")
def hello():
    return "Hello World!"

@application.route('/dbtest/')
def test_al():
    test = db_queue_monitor()
    if test.check_connectivity():
        #return("Successful connection to db")
        return(str(pathlib.Path(__file__).parent.absolute()) + str(pathlib.Path().absolute()))
    else:
        return("Failed connecting to db")

if __name__ == "__main__":
    application.run()
