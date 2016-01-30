import feedparser

def rss_feed_urls():
    return ['http://www.theguardian.com/world/rss']

def download_feed(url):
    return feedparser.parse(url)

def filter_feed(feed):
    for entry in feed['entries']:
        title = entry['title']
        if contains_negative_words(title):
            print title

def contains_negative_words(text):
    for word in negative_words():
        if word in text:
            return True

    return False

def negative_words():
     return {'war', 'terror'}


for url in rss_feed_urls():
    print url
    feed = download_feed(url)
    filter_feed(feed)
