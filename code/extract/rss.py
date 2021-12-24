from sheets import *
from db import *
import feedparser
counter = 0
for x in RSS:
    NewsFeed = feedparser.parse(x)
    for i in range(len(NewsFeed.entries)):
        print(counter, "  :  ",NewsFeed.entries[i].title, " : " , NewsFeed.entries[i].link, " : " , NewsFeed.entries[i].author , " : " , NewsFeed.entries[i].published, )
        counter += 1





# print(NewsFeed.entries[1].summary)  Find How to get the summary without the html tags
# https://stackoverflow.com/questions/27676982/delete-html-tags-from-string-python
