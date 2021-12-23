from sheets import *
import feedparser
i=0
for x in RSS:
    NewsFeed = feedparser.parse(x)
    entry = NewsFeed.entries[1]

    titles = entry.title
    links = entry.link
    print() 
    print(i,"    ",  titles, ' : ' , links)
    i+=1
    