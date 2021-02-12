import pymysql
import os

class get_iccp_data():

    def __init__(self):
        # These parameters are defined as secrets and config maps in Openshift
        self.MYSQL_USER = os.environ.get('MYSQL_USER')
        self.MYSQL_HOST = os.environ.get('MYSQL_HOST')
        self.MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
        self.MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')

    def get_data(self):
        # TO-DO
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