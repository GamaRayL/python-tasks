import psycopg2

# connect to db
db = psycopg2.connect(host='localhost', database='test', user='postgres', password='1612')
try:
    with db:
        with db.cursor() as cursor:
            # execute query
            cursor.execute('INSERT INTO user_account VALUES(%s, %s)', (7, 'Арина'))

            cursor.execute('SELECT * FROM user_account')
            rows = cursor.fetchall()
            for row in rows:
                print(row)
finally:
    db.close()
