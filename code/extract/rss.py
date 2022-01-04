import sheets
import db
import feedparser


RSS = sheets.main()  # Get a List of RSS feed from Google Sheets
conn = db.connect()
cur = conn.cursor()

def checkExsistence(Title):
    cur.execute("SELECT * FROM feed WHERE TITLES=%s;", (Title,))
    rows = cur.fetchall()
    if len(rows) == 0:
        return False
    else:
        return True


for x in RSS:
    NewsFeed = feedparser.parse(x)
    for posts in range(len(NewsFeed.entries)):

        try:
            Author = NewsFeed.entries[posts].author
        except:
            Author = "None"

        try:
            Temp = str(NewsFeed.entries[posts].published_parsed.tm_year)+"-"+str(
                NewsFeed.entries[posts].published_parsed.tm_mon)+"-"+str(NewsFeed.entries[posts].published_parsed.tm_mday)
            Published = Temp
        except:
            Published = str("01-01-1999")

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
            cur.execute(
                'INSERT INTO feed (Titles, URL, Author) VALUES (%s, %s, %s);', (Title, Link, Author))

        # cur.execute(
        # "INSERT INTO feed (date) VALUES (%s);", (Published))

conn.commit()
conn.close()

# c=1
# NewsFeed = feedparser.parse('https://www.p3r.one/feed/')
# for posts in range(len(NewsFeed.entries)):
#     print(c, "      ", NewsFeed.entries[posts].title)
#     c=c+1