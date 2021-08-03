import feedparser
import re
import config
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

NewsFeed = feedparser.parse(config.htmlurlarticles)

print('Number of RSS posts :', len(NewsFeed.entries))
print(NewsFeed.entries[0])
entry = NewsFeed.entries[0]
print('Post Title :', entry.title)
print('Post Description :', entry.description.split('\n')[1])
#print('Summary :', entry.summary)
for tag in entry.tags:
    print('Tags :', tag['term'])

title = str(entry.title)
description = entry.description
index = description.find('/>')
description = description[index:]
link = re.search("(?P<url>https?://[^\s]+)", entry.description).group("url")
link = link[:-1]
