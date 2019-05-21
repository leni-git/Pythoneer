# Latest Edit: 10-April-2019 by Leni.

from dbinfo import TABLE_NAME

query_INSERT = "INSERT INTO {tName} (uuid) VALUES (%s)".format(tName=TABLE_NAME)

def inserting(cursor, value):
    print('\t>>> {}'.format(query_INSERT % value))
    try:
        result = cursor.execute(query_INSERT % value)
    except Exception as e:
        print('error: {}'.format(e))
        return False

    else:
        print(result)
        return True
