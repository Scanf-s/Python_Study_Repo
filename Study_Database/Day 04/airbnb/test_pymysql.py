import pymysql.cursors

# DB Connection
# https://pymysql.readthedocs.io/en/latest/user/examples.html

# Connection class
# https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123123',
                             database='classicmodels',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# Cursors : https://pymysql.readthedocs.io/en/latest/modules/cursors.html
# DictCursor : A cursor which returns results as a dictionary

try:
    # CRUD example
    with connection:
        with connection.cursor() as cursor:
            # Write a single record
            sql = "INSERT INTO `classicmodels`.employees VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, ('2005', 'Sullung_Python', 'Python', 'x1234', 'python@python.org', '9', '1102', 'Sales Rep'))

        # connection is not autocommit by default. So i must commit to save these changes
        connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `classicmodels`.employees"
            cursor.execute(sql)
            for row in cursor.fetchall():
                print(row)
finally:
    connection.close()