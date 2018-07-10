"""
Attempt at threaded approach to news webscraper. I kept running into this
error {"status":"error","code":"rateLimited","message":"You have made too many requests recently. Developer accounts are limited to 1,000 requests over a 24 hour period (250 requests available every 6 hours). Please upgrade to a paid plan if you need more requests."}
"""
import time
import requests
import threading

NEWS_API_KEY = 'ebb338c04b1c416ba9ea2ab24f5c0fa6'#'fa5580717eab48e3bca211c82602c5c4'#'0b8b3765b41643e69374333bb63a4d5a'

WORD = 'trump'

base_url = 'https://newsapi.org/v1/'

max_threads = 10

def get_sources():
    """
    Get all the english language sources of news
    'https://newsapi.org/v1/sources?language=en'
    """
    url = base_url + "sources"
    params = {"language": "en"}
    resp = requests.get(url, params=params)
    data = resp.json()
    sources = [src['id'].strip() for src in data['sources']]
    print("all the sources")
    print(sources)
    return sources


art_count = 0
word_count = 0

def get_articles(source):
    """
    https://newsapi.org/v1/articles?source=associated-press
    """
    url = base_url + "articles"
    params = {"source": source,
        "apiKey": NEWS_API_KEY,
        "sortBy": "top"
        }
    print("requesting:", source)
    resp = requests.get(url, params=params)
    if resp.status_code != 200:
        print("something went wrong with {}".format(source))
        print(resp)
        print(resp.text)
        return []
    data = resp.json()
    # the url to the article itself is in data['articles'][i]['url']
    new_titles = [str(art['title']) + str(art['description'])
        for art in data['articles']]
    titles.extend(new_titles)

    #return titles

def count_word(word, titles):
    word = word.lower()
    count = 0
    for title in titles:
        if word in title.lower():
            count += 1
    return count

start = time.time()
sources = get_sources()

titles = []

# I think this is how we might implement threading based on class examples
# but I'm not sure since it's really difficult to test
for source in sources:
    for i in range(max_threads):
        thread = threading.Thread(target=get_articles, args=[source])
        thread.start()

art_count = len(titles)
word_count = count_word(WORD, titles)

print(WORD, "found {} times in {} articles".format(word_count, art_count))
print("Process took {:.0f} seconds".format(time.time() - start))