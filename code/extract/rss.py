import sheets
from db import write
import feedparser


RSS = sheets.main()  # Get a List of RSS feed from Google Sheets

for x in RSS:
    NewsFeed = feedparser.parse(x)
    for i in range(len(NewsFeed.entries)):
        Titles = NewsFeed.entries[i].title
        Links = NewsFeed.entries[i].link
        write(Titles, Links)

# Add Eception Handling Function (raw.py) for Published, Author, Tags
