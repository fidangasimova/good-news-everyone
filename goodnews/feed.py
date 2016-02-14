import feedparser
import config
 
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
    feed['entries'] = positive_entries

    return feed

def contains_negative_words(text):
    words = set()
    for word in text.split():
        words.add(word.strip(".,?!"))

    for negative_word in config.negative_words:
        if negative_word in words:
            return True

    return False
          
  
