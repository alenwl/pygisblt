import pymysql
import os
# Read this again https://pypi.org/project/PyMySQL/

class validate_user():

    def __init__(self):
        # These parameters are defined as secrets and config maps in Openshift
        self.MYSQL_USER = os.environ.get('MYSQL_USER')
        self.MYSQL_HOST = os.environ.get('MYSQL_HOST')
        self.MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
        self.MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')

    def validate(self,client):
        # Attempt to open connection to dabatase
        data = []
        if not client:
            return False
        try:
            db = pymysql.connect(host=self.MYSQL_HOST,
                    user=self.MYSQL_USER,
                    password=self.MYSQL_PASSWORD,
                    database=self.MYSQL_DATABASE )
            with db.cursor() as cursor:
                sql = ("SELECT password FROM credentials WHERE client=\""
                        + client + "\"")
                cursor.execute(sql)
                data = cursor.fetchall()
            db.close()
            if not data[0][0]:
                return False
            else:
                return data[0][0]
        except pymysql.Error as e:
            print("Connection error %d: %s" %(e.args[0], e.args[1]))
            return False