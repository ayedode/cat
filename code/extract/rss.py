from sheets import *
from db import *
import feedparser
counter = 0
for x in RSS:
    NewsFeed = feedparser.parse(x)
    for i in range(len(NewsFeed.entries)):
        print(counter, "  :  ", NewsFeed.entries[i].title, " : ", NewsFeed.entries[i].link,
              " : ", NewsFeed.entries[i].author, " : ", NewsFeed.entries[i].published, )
        counter += 1

