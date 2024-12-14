import psycopg2
import config
# import traceback

# cur = conn.cursor()

def connect():
    try:
        conn = psycopg2.connect(
                database= config.database,
                user= config.user,
                password= config.password,
                host= config.host,
                port= config.port
            )
        return conn
    except Exception as err:
        print(err)


def print_version(connection):
    cursor = connect().cursor()
    cursor.execute('SELECT version()')
    db_version = cursor.fetchone()
    print(db_version)
    cursor.close()
    connection.close()

print_version(connect())
    
def insert(connection):
    cursor = connection.cursor()
    query = "INSERT INTO divisi (divisiname, divisicode) VALUES (%s, %s);"

    try:
        data = ('Quality Assurance', 'QA')
        cursor.execute(query, data)
        connection.commit()
        print("Data inserted successfully")
    except Exception as err:
        print(err)

    cursor.close()
    connection.close()

# insert(connect())

def read(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("Select * from divisi;")
        record = cursor.fetchall()
        print("Success get data all data divisi")
        print(record)
        connection.commit()
    except Exception as err:
        print(err)
    cursor.close()
    connection.close()



def update(connection):
    cursor = connection.cursor()
    query = "Update divisi set divisicode=%s where id=%s;"
    try:
        cursor.execute(query, ("QY", 1))
        print("Success update data")
        connection.commit()
    except Exception as err:
        print(err)
    cursor.close()
    connection.close()

# update(connect())


def delete(connection):
    cursor = connection.cursor()
    query = "DELETE FROM divisi WHERE id=%s;"
    try:
        cursor.execute(query, [4])
        connection.commit()
        print("Success delete data")
    except Exception as err:
        print(err)
    
    cursor.close()
    connection.close()

delete(connect())
read(connect())