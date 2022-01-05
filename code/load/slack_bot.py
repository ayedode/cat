import slack
from decouple import config
import psycopg2
import time
from loguru import logger

DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_HOST = config('DB_HOST')
DB_PASSWORD = config('DB_PASSWORD')
SLACK_TOKEN = config('SLACK_TOKEN')


def connect():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, host=DB_HOST, password=DB_PASSWORD)
        return conn
    except:
        logger.debug("Unable to connect to the database")


conn = connect()
cur = conn.cursor()
client = slack.WebClient(token=SLACK_TOKEN)


# First we need to check what's the last index of the sent message
# Then we need to fetch the data from the database after the index
# Then we need to post
# Then we need to update the status on db
# Repeat
#


def get_last_index():
    cur.execute("SELECT SLACK FROM status;")
    rows = cur.fetchall()
    return(rows[0][0])


def update(new_index):  # Updating data into the table using the psycopg2 module
    cur.execute("UPDATE STATUS SET SLACK=%s;", (new_index,))
    conn.commit()


cur.execute("SELECT * FROM feed")
rows = cur.fetchall()
for row in rows:
    if row[0] > get_last_index():
        logger.debug(row[0])
        client.chat_postMessage(
            channel='#a-better-yt',
            text="New Post: `"+row[1]+"` \n " +
            row[2] + "        " )
        logger.debug("Sent    "+row[1])
        update(row[0])
        time.sleep(1800) #30 mins


conn.close()
