import psycopg2


def connect(): # Connecting to the database using the psycopg2 module
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, host=DB_HOST, password=DB_PASSWORD)
        print("Database connection established")
        return conn
    except:
        print("Database connection failed")


def read(): # Reading data from the table using the psycopg2 module
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventory")
    rows = cur.fetchall()
    for row in rows:
     print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))
    conn.close()
    return rows

def write(): # Inserting data into the table using the psycopg2 module
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("Trial", 124))
    conn.commit()
    conn.close()


def create(): # Creating a table using the psycopg2 module
    conn = connect()
    cur = conn.cursor()
    cur.execute("CREATE TABLE posts (name VARCHAR(255), quantity INTEGER);")
    conn.commit()
    conn.close()