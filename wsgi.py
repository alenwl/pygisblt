from flask import Flask
import time
import pymysql
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route('/test/')
def test_al():
    # Open database connection
    db = pymysql.connect("172.30.176.197","user","password","gisbltdb" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")
    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    # disconnect from server
    db.close()
    return("Database version : %s " % data)

if __name__ == "__main__":
    application.run()
