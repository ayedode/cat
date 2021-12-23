from sheets import *
import feedparser
counter = 0
print(RSS[1])
NewsFeed = feedparser.parse(RSS[1])
for i in range(len(NewsFeed.entries)):
    print(counter, "    ",NewsFeed.entries[i].title, " : " , NewsFeed.entries[i].link)
    counter += 1
