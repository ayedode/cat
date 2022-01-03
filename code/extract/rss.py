import sheets
import time

import db
import feedparser


RSS = sheets.main()  # Get a List of RSS feed from Google Sheets
conn = db.connect()
cur = conn.cursor()

# for x in RSS:
#     NewsFeed = feedparser.parse(x)
#     for posts in range(len(NewsFeed.entries)):



#         try:
#             Author= NewsFeed.entries[posts].author
#         except:
#             Author="None"

#         try:
#             Temp=str(NewsFeed.entries[posts].published_parsed.tm_year)+str(NewsFeed.entries[posts].published_parsed.tm_mon)+str(NewsFeed.entries[posts].published_parsed.tm_mday)
#         except:
#             Published=00000000

#         try:
#             Link=NewsFeed.entries[posts].link
#         except:
#             Link="Not Available"

#         try:
#             Title=NewsFeed.entries[posts].title
#         except:
#             Title="Not Available"


#         print("Now starting DB Connection", time.time())
#         cur.execute(
#         "INSERT INTO feed (Titles, URL, Author, POSTING_DATE) VALUES (%s, %s, %s, %s);", (Title, Link, Author, to_date()))



# conn.commit()
# conn.close()

