from flask import Flask
import time
import src/db-queue-monitor
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route('/test/')
def test_al():
    test = db-queue-monitor()
    if test.check_connectivity():
        return("Success")
    else:
        return("Fail")

if __name__ == "__main__":
    application.run()
