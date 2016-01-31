import feedparser
feed = feedparser.parse('http://www.theguardian.com/world/rss')
NEGATIVE_WORDS = ['war', 'war']
for entry in feed['entries']:
    title = entry['title']
    for word in NEGATIVE_WORDS:
        if word in title:
            print title
