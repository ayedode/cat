# This files contains comments to be resolved

# Try Exception Block


# NewsFeed = feedparser.parse(RSS[93])
# print( "  :  ", NewsFeed.entries[1].title, " : ", NewsFeed.entries[1].link,
#               " : ", NewsFeed.entries[1].author, "   :  ", NewsFeed.entries[1].tags," : ", NewsFeed.entries[1].published, )
# if NewsFeed.entries[1].tags:
#     print((NewsFeed.entries[1].tags[1]))
# else:
#     print("None")

# try:
#     print((NewsFeed.entries[1].tags[1].term))
# except:
#     print("None")


# def ExceptionChecker(TemporaryVariable):
#     try:
#         available = TemporaryVariable
#         return available
#     except:
#         exception="None"
#         return exception

# def greet(var):
#     ExceptionChecker(var)

# var = greet(NewsFeed.entries[1].tags[1].term)


# def ExceptionChecker(TemporaryVariable):
#     try:
#         print(TemporaryVariable)
#     except:
#         print("None")


# var = NewsFeed.entries[1].tags[1].term
# ExceptionChecker(var)


# from typing import Counter
# import sheets
# import feedparser


# RSS = sheets.main() # Get a List of RSS feed from Google Sheets
# Counterrrr=1
# for x in RSS:
#     NewsFeed = feedparser.parse(x)
#     for i in range(len(NewsFeed.entries)):
#         Titles = NewsFeed.entries[i].title
#         Links = NewsFeed.entries[i].link
#         print(Counterrrr, Titles)
#         print("\n")
#         Counterrrr=Counterrrr+1


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


def read():  # Reading data from the table using the psycopg2 module
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts")
    counterr = 1
    rows = cur.fetchall()
    for row in rows:
        print(counterr, "Data row = (%s, %s)" %
              (str(row[0]), str(row[1])))
        counterr += 1
    conn.close()
    return rows


read()


# Write by checking https://stackoverflow.com/questions/639854/check-if-a-row-exists-otherwise-insert
