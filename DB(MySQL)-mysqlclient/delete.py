# Latest Edit: 10-April-2019 by Leni.

from dbinfo import TABLE_NAME

query_DELETE = "DELETE FROM {tName} WHERE user_id=%s".format(tName=TABLE_NAME)

def deleting(cursor, value):
    print('\t>>> {}'.format(query_DELETE % value))
    try:
        result = cursor.execute(query_DELETE % value)
    except Exception as e:
        print('error: {}'.format(e))
        return False

    else:
        print(result)
        return True
