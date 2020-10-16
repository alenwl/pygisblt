import pymysql
import threading

class db_queue_monitor():

    def check_connectivity(self):
        # Attempt to open connection to dabatase
        try:
            db = pymysql.connect("172.30.176.197","user","password","gisbltdb" )
            db.close()
        except:
            return False
            # prepare a cursor object using cursor() method
            #cursor = db.cursor()
            # execute SQL query using execute() method.
            #cursor.execute("SELECT VERSION()")
            # Fetch a single row using fetchone() method.
            #data = cursor.fetchone()
            # disconnect from server
            #db.close()
        return True

    