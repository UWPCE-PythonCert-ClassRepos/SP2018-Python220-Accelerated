# Andy Kwon
# Activity 09:
# getting sources from newsapi via threading
# main and worker threads concept


import requests
import threading
import time

NEWS_API_KEY = "1b11a000184c4f13a34296455bb0ed02"
WORD = "Korea"
base_url = "https://newsapi.org/v1/"


def get_sources():
    """
    Gets all english language sources and returns a list of the sources.

    Sort of like: 'https://newsapi.org/v1/sources?language=en'
    """
    url = base_url + "sources"
    params = {"language": "en"}
    resp = requests.get(url, params=params)
    data = resp.json()
    sources = [src['id'].strip() for src in data['sources']]
    print("all the sources")
    print(sources)
    return sources


def get_articles(source):
    """
    Gets the articles from the sources and returns a list of titles
    """

    url = base_url + "articles"
    params = {"source": source,
              "apiKey": NEWS_API_KEY,
              }
    print("requesting: " + source + ", %s" %
          threading.current_thread().name)

    resp = requests.get(url, params=params)

    data = resp.json()

    # the url to the article itself is in data['articles'][i]['url']
    titles = [str(art['title']) + str(art['description']) for art in data['articles']]

    return titles


def split_list_many(alist, wanted_parts):
    length = len(alist)
    return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
            for i in range(wanted_parts)]


def split_list(a_list):
    half = int(len(a_list) / 2)
    return a_list[:half], a_list[half:]


def worker(lock, source):
    global titles
    print("thread %s" % threading.current_thread().name)
    for news in source:
        lock.acquire()
        titles = get_articles(news)
        lock.release()


def count_words(x, y):
    """
    Maybe to make a way to count words... in the article?
    """
    # lower/upper case the word
    # initiate a counter
    # for each title, see if word is in it. if yes, up my counter

    # word = x.upper()
    # counter = 0
    # for title in y:
    #     if word in title.upper():
    #         counter += 1
    # return counter


    pass


def main():

    global titles
    start = time.time()
    sources = get_sources()
    list_sources = split_list_many(sources, wanted_parts = 4)

    lock = threading.Lock()

    threads = []
    for i in range(4):
        thread = threading.Thread(target = worker, args = (lock, list_sources[i],))
        thread.start()
        threads.append(threads)
        thread.join()


    # create reports from title list
    print("Number of sources: " + str(len(sources)))
    print("Time: {:.0f} seconds".format(time.time() - start))

if __name__ == '__main__':
    main()
