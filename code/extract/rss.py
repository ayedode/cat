import sheets
import db
import feedparser
import datetime
from loguru import logger


RSS = sheets.main()  # Get a List of RSS feed from Google Sheets
conn = db.connect()
cur = conn.cursor()

bag = []

def checkExsistence(Title):
    if not Title in bag:
        cur.execute("SELECT * FROM feed WHERE TITLES=%s;", (Title,))
        rows = cur.fetchall()
        if len(rows) == 0:
            return False
        else:
            logger.debug(" FOUND IN DB  "+Title)
            return True
    else:
        logger.debug("FOUND IN BAG  "+Title)
        return True

for x in RSS:
    NewsFeed = feedparser.parse(x)
    for posts in range(len(NewsFeed.entries)):

        try:
            Author = NewsFeed.entries[posts].author
        except:
            Author = "None"

        try:
            Year = NewsFeed.entries[posts].published_parsed.tm_year
            Month=NewsFeed.entries[posts].published_parsed.tm_mon
            Date=NewsFeed.entries[posts].published_parsed.tm_mday
        except:
            pass

        try:
            Link = NewsFeed.entries[posts].link
        except:
            Link = "Not Available"

        try:
            Title = str(NewsFeed.entries[posts].title)
        except:
            Title = "Not Available"

        if checkExsistence(Title):
            pass
        else:
            cur.execute('INSERT INTO feed (Titles, URL, Author, DATE) VALUES (%s, %s, %s, %s);', (Title, Link, Author, datetime.date(Year, Month, Date)))
            logger.debug("ADDING  "+ Title)
            bag.append(Title)

        # cur.execute(
        # "INSERT INTO feed (date) VALUES (%s);", (Published))

conn.commit()
conn.close()

# c=1
# NewsFeed = feedparser.parse('https://www.p3r.one/feed/')
# for posts in range(len(NewsFeed.entries)):
#     print(c, "      ", NewsFeed.entries[posts].title)
#     c=c+1