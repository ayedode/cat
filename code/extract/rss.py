import sheets
from db import *
import feedparser


RSS = sheets.main() # Get a List of RSS feed from Google Sheets

counter = 0
for x in RSS:
    NewsFeed = feedparser.parse(x)
    for i in range(len(NewsFeed.entries)):
        print(counter, "  :  ", NewsFeed.entries[i].title, " : ", NewsFeed.entries[i].link,
              " : ", NewsFeed.entries[i].author, " : ", NewsFeed.entries[i].published, )
        counter += 1
