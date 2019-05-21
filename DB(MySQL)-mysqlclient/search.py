# Latest Edit: 10-April-2019 by Leni.

from dbinfo import TABLE_NAME

query_SELECT = "SELECT * FROM {tName}".format(tName=TABLE_NAME)

def searching(cursor):
    print('\t>>> {}'.format(query_SELECT))
    result = cursor.execute(query_SELECT)
    print(result)
    data = cursor.fetchone()
    print(data)
