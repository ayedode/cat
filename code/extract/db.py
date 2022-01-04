import psycopg2
from decouple import config


DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_HOST = config('DB_HOST')
DB_PASSWORD = config('DB_PASSWORD')


def connect():  # Connecting to the database using the psycopg2 module
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, host=DB_HOST, password=DB_PASSWORD)
        return conn
    except:
        print("Database connection failed")


# def read_all(conn):  # Reading data from the table using the psycopg2 module
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM feed")
#     rows = cur.fetchall()
#     for row in rows:
#         print("Data row = (%s, %s)" %
#               (str(row[0]), str(row[1])))
#     return rows


# def checkExsistence(Title, conn):
#     cur = conn.cursor()
#     print(Title)
#     cur.execute("SELECT * FROM feed WHERE TITLES=(%s);", (Title))
#     rows = cur.fetchall()
#     if len(rows) == 0:
#         return False
#     else:
#         return True


# def write(Title, Link, conn):  # Inserting data into the table using the psycopg2 module
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO posts (Titles, Link) VALUES (%s, %s);", (Title, Link))
#     conn.commit()


def create():  # Creating a table using the psycopg2 module
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE feed (ID SERIAL PRIMARY KEY, TITLES VARCHAR(255) , URL TEXT, AUTHOR VARCHAR(255), DATE DATE);")
    conn.commit()
    conn.close()

# create()
