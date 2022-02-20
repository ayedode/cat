import sheets
import db
import feedparser
import datetime
from loguru import logger


RSS = sheets.main()  
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
            logger.warning(" FOUND IN DB  "+Title)
            return True
    else:
        logger.warning("FOUND IN BAG  "+Title)
        return True


for x in RSS:
    NewsFeed = feedparser.parse(x)
    for posts in range(len(NewsFeed.entries)):

        try:
            Author = NewsFeed.entries[posts].author
        except:
            Author = "None"

        try:
            Category = NewsFeed.entries[posts].category
        except:
            Category = "Not Specified"

        try:
            Year = NewsFeed.entries[posts].published_parsed.tm_year
            Month = NewsFeed.entries[posts].published_parsed.tm_mon
            Date = NewsFeed.entries[posts].published_parsed.tm_mday
        except:
            pass

        try:
            Link = NewsFeed.entries[posts].link
            RemoveTrackingInLink = Link.split("?", 1)[0]
            RemoveHashInLink = RemoveTrackingInLink.split("#", 1)[0]

        except:
            pass

        try:
            Title = str(NewsFeed.entries[posts].title)
        except:
            Title = "Not Available"

        if checkExsistence(Title):
            pass
        else:
            cur.execute('INSERT INTO feed (Titles, URL, Author, CATEGORY, DATE) VALUES (%s, %s, %s, %s, %s);',
                        (Title, RemoveHashInLink, Author, Category, datetime.date(Year, Month, Date)))
            logger.success("ADDING  " + Title)
            bag.append(Title)

conn.commit()
conn.close()

