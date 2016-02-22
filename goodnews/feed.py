import feedparser
import config
import PyRSS2Gen
 
def download_feed(url):
    return feedparser.parse(url)

def filter_feed(feed_dict):
    positive_entries = []
    for entry in feed_dict.entries:
        title = entry.title
        if contains_negative_words(title):
            print title
        else:
            positive_entries.append(entry)
    feed_dict.entries = positive_entries

    return feed_dict

def contains_negative_words(text):
    words = set()
    for word in text.split():
        stripped_word = word.strip(".,?!").lower()
        words.add(stripped_word)

    for negative_word in config.negative_words:
        if negative_word in words:
            return True

    return False
          
def generate_rss(feed_dict):
    items = []
    for entry in feed_dict.entries:
        item = PyRSS2Gen.RSSItem(
            title = entry.title,
            link = entry.link, 
            description = entry.description,
            pubDate = entry.published,
        )
        items.append(item)

    rss = PyRSS2Gen.RSS2(
        title = feed_dict.feed.title,
        link = feed_dict.feed.link,
        description = feed_dict.feed.description,
        lastBuildDate = feed_dict.feed.published, 
        items = items
    )
    return rss.to_xml()


