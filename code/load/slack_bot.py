import slack
from decouple import config
import psycopg2
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


cur.execute("SELECT * FROM feed")
rows = cur.fetchall()
# for row in rows:
row = rows[14]
client.chat_postMessage(
    channel='#a-better-yt',
    text="New Post: `"+row[1]+"` \n Visit here: "+row[2]
)

logger.debug("Sent"+row[1])
