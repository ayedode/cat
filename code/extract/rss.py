import sheets
import db
import feedparser
import datetime
from meta_image import get_image
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
        except:
            pass

        try:
           Title = str(NewsFeed.entries[posts].title)
        except:
            Title = "Not Available"

        try:
            ImageURL = get_image(Link)
        except:
            ImageURL = "https://raw.githubusercontent.com/ayedode/cat/main/assests/no_image.png"

        # try:
        #     DescriptionRaw = NewsFeed.entries[posts].summary
        #     Description = DescriptionRaw[:120]
        #     print(DescriptionRaw)
        # except:
        #     Description = " "    


        if checkExsistence(Title):
            pass
        else:
            cur.execute('INSERT INTO feed (Titles, URL, Author, CATEGORY, DATE, IMAGEURL) VALUES (%s, %s, %s, %s, %s, %s);',
                        (Title, RemoveTrackingInLink, Author, Category, datetime.date(Year, Month, Date), ImageURL))
            logger.debug("ADDING  " + Title)
            bag.append(Title)       
conn.commit()
conn.close()

# c=1
# NewsFeed = feedparser.parse('https://www.p3r.one/feed/')
# for posts in range(len(NewsFeed.entries)):
#     print(c, "      ", NewsFeed.entries[posts].title)
#     c=c+1
