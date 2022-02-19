import pandas as pd
import psycopg2
from decouple import config
from loguru import logger


DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_HOST = config('DB_HOST')
DB_PASSWORD = config('DB_PASSWORD')
filename = '1620197.csv'


def connect():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, host=DB_HOST, password=DB_PASSWORD)
        return conn
    except:
        logger.error("Database connection failed")


col_list = ["TagName", "Description"]
df = pd.read_csv(filename, usecols=col_list)


conn = connect()
cur = conn.cursor()


for itr in df.iterrows():
    tagname = str(itr[1].TagName)
    description = str(itr[1].Description)
    logger.debug(tagname)
    logger.debug(description)
    cur.execute("INSERT INTO tags (tag, description) VALUES (%s, %s);",
                (tagname, description))
    logger.success("Logging Entry" + tagname)


# itr = next(
#     df.iterrows())
# print(itr[1].TagName)
# print(itr[1].Description)
conn.commit()
logger.success("Committed")
conn.close()
