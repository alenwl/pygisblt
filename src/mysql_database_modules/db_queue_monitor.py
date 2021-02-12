import pymysql
import threading
import json
import os

class db_queue_monitor():

    def __init__(self):
        # Parameters can be found in /opt/app-root/src/json/db_access_parameters.json
        # These parameters are defined as secrets and config maps in Openshift
        self.MYSQL_USER = os.environ.get('MYSQL_USER')
        self.MYSQL_HOST = os.environ.get('MYSQL_HOST')
        self.MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
        self.MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')

    def check_connectivity(self):
        # Attempt to open connection to dabatase
        # Return true if success. False if otherwise
        try:
            db = pymysql.connect(host=self.MYSQL_HOST,
                    user=self.MYSQL_USER,
                    password=self.MYSQL_PASSWORD,
                    database=self.MYSQL_DATABASE )
            db.close()
        except pymysql.Error as e:
            print("Connection error %d: %s" %(e.args[0], e.args[1]))
            return False
        return True

    def get_historical(self):
        # Attempt to open connection to dabatase
        data = []
        try:
            db = pymysql.connect(host=self.MYSQL_HOST,
                    user=self.MYSQL_USER,
                    password=self.MYSQL_PASSWORD,
                    database=self.MYSQL_DATABASE )
            with db.cursor() as cursor:
                sql = "SELECT * FROM historical"
                cursor.execute(sql)
                data = cursor.fetchall()
            db.close()
            return data
        except pymysql.Error as e:
            print("Connection error %d: %s" %(e.args[0], e.args[1]))
            return False