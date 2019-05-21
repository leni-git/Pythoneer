# Latest Edit: 10-April-2019 by Leni.

from connect import DataConenct
from insert import inserting
from search import searching
from delete import deleting

db = DataConenct()
cursor = db.get_cursor()

# Insert a user, Have to write an own key
if inserting(cursor, "'onlyenglish'"):
    db.upload_db()

searching(cursor)

# Delete using 'user_id'
if deleting(cursor, "1"):
    db.upload_db()

searching(cursor)
