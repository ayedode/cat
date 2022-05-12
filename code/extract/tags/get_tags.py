from loguru import logger
import psycopg2
from decouple import config

DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_HOST = config('DB_HOST')
DB_PASSWORD = config('DB_PASSWORD')

conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, host=DB_HOST, password=DB_PASSWORD)
cur = conn.cursor()


def tags():

    cur.execute("SELECT id,tag FROM tags;")
    rows = cur.fetchall()
    my_set = set()
    tags = []

    for row in rows:
        temps = row[1]
        my_set.add(temps)
        tags.append(str(row[1]))
    return(my_set)

my_set=tags()
seen = set()



def read_all():

    cur.execute("SELECT id,description FROM feed where description is not null ;")
    rows = cur.fetchall()
    
    for i in range(len(rows)):
        id = rows[i][0] # id of the feed
        description = rows[i][1].split(" ")

        for j in range(len(description)):
            if description[j] in my_set:
                logger.critical((id,description[j]))
        pass

read_all()