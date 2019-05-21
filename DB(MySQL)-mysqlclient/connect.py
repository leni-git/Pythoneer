# Latest Edit: 10-April-2019 by Leni.

import MySQLdb

# Import user account
from dbinfo import *

# Oepn Database Connection
class DataConenct:
    def __init__(self):
        self.db = MySQLdb.connect(
            host=HOST,
            user=USER,
            password=PWD,
            database=DB_NAME
        )

        # Prepare a cursor object using cursor() method
        self.cursor = self.db.cursor()

        # Execute SQL query using execute() method.
        self.cursor.execute("SELECT VERSION()")

        # Fetch a single row using fetchone() method.
        data = self.cursor.fetchone()
        print ("Database version : %s " % data)

    def upload_db(self):
        # You have to commit When you use inser and delete queries.
        self.db.commit()

    def get_cursor(self):
        return self.cursor

        # Disconnect from server
    def closing(self):
        db.close()
