import pymysql
import threading
import json

class db_queue_monitor():

    def __init__(self):
        # Parameters stored in /opt/app-root/src/json/db_access_parameters.json
        db_parameters = json.load(open('/opt/app-root/src/json/db_access_parameters.json'))
        self.MYSQL_USER = db_parameters['MYSQL_USER']
        self.MYSQL_HOST = db_parameters['MYSQL_HOST']
        self.MYSQL_PASSWORD = db_parameters['MYSQL_PASSWORD']
        self.MYSQL_DATABASE = db_parameters['MYSQL_DATABASE']

    def check_connectivity(self):
        # Attempt to open connection to dabatase
        # Return true if success. False if otherwise
        try:
            db = pymysql.connect(self.MYSQL_HOST,
                    self.MYSQL_USER,
                    self.MYSQL_PASSWORD,
                    self.MYSQL_DATABASE )
            db.close()
        except pymysql.Error as e:
            print("Connection error %d: %s" %(e.args[0], e.args[1]))
            return False
        return True

    def get_historical(self):
        # Attempt to open connection to dabatase
        data = []
        try:
            db = pymysql.connect(self.MYSQL_HOST,
                    self.MYSQL_USER,
                    self.MYSQL_PASSWORD,
                    self.MYSQL_DATABASE )
            with db.cursor() as cursor:
                sql = "SELECT * FROM historical ORDER BY id DESC"
                cursor.execute(sql)
                data = cursor.fetchall()
            db.close()
            return data
        except pymysql.Error as e:
            print("Connection error %d: %s" %(e.args[0], e.args[1]))
            return False