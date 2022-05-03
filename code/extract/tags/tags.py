import scrapy
from loguru import logger
from scrapy.crawler import CrawlerProcess
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

    cur.execute("SELECT id,description FROM feed limit 1900;")
    rows = cur.fetchall()
    
    
    for i in range(len(rows)):
        id = rows[i][0]

        description = rows[i][1].split(" ")
        for j in range(len(description)):
            if description[j] in my_set:
                # logger.debug(description[j])
                # logger.critical(id)
      
                seen.add((id,description[j]))

    logger.error(seen)         
    pass

print(read_all())