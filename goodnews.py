import feedparser

def rss_feed_urls():
    return ['http://www.theguardian.com/world/rss']

def download_feed(url):
    return feedparser.parse(url)

def filter_feed(feed):
    positive_entries = []
    for entry in feed['entries']:
        title = entry['title']
        if contains_negative_words(title):
            print title
        else:
            positive_entries.append(entry)

    feed['entries']= positive_entries
    return feed


def contains_negative_words(text):
    for word in negative_words():
        if word in text:
            return True

    return False

def negative_words():
     return {'war', 'terror'}


urls = rss_feed_urls()
url = urls[0]
feed = download_feed(url)
positive_feed = filter_feed(feed)
print positive_feed



