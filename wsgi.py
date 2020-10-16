from flask import Flask
import time
from pygisblt.src.db_queue_monitor import *
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route('/test/')
def test_al():
    test = db_queue_monitor()
    if test.check_connectivity():
        return("Success")
    else:
        return("Fail")

if __name__ == "__main__":
    application.run()
