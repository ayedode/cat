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

tags_dict = {}


def check_if_exists(id, tagid):
    cur.execute(
        "SELECT * FROM connect WHERE postid=%s AND tagsid=%s", (id, tagid))
    rows = cur.fetchall()
    if len(rows) == 0:
        return False
    else:
        return True


def tags():

    cur.execute("SELECT id,tag FROM tags;")
    rows = cur.fetchall()
    my_set = set()
    tags = []

    for row in rows:
        temps = row[1]
        tags_dict[temps] = row[0]
        my_set.add(temps)
        tags.append(str(row[1]))
    return(my_set)


my_set = tags()
seen = set()


def read_all():

    cur.execute(
        "SELECT id,description FROM feed where description is not null ;")
    rows = cur.fetchall()

    for i in range(len(rows)):
        id = rows[i][0]  # id of the feed
        description = rows[i][1].split(" ")

        for j in range(len(description)):
            if description[j] in my_set:
                # logger.critical((id, tags_dict[description[j]]))
                seen.add((id, tags_dict[description[j]]))
        pass


def write_to_db():
    for relation in seen:
        if check_if_exists(relation[0], relation[1]):
            logger.debug(
                {'postid': relation[0], 'tagsid': relation[1], 'status': 'failed'})

        else:
            cur.execute("INSERT INTO connect (postid, tagsid) VALUES (%s, %s)",
                        (relation[0], relation[1]))
            logger.debug(
                {'postid': relation[0], 'tagsid': relation[1], 'status': 'success'})
           

read_all()
write_to_db()

conn.commit()
conn.close()
