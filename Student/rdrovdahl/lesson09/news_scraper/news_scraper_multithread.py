#! /usr/local/bin/python3
"""
This is a multi-threaded application that pulls data from multiple online news
sources.  Returns how much a given word is mentioned in the news today.

Uses data from the NewsAPI:
  https://newsapi.org
Note: you need to register with the web site to get a KEY
"""
import threading
import queue
import time
import requests

# may need to rotate these API keys due to rate limiting by the provider
# NEWS_API_KEY = "59e0f77b685844edabefafa4fdd8550e"
# NEWS_API_KEY = "a19a67269a0b4d2682f3ca8bbeec7478"
# NEWS_API_KEY = "00d78fd818ef4ad297890870a42327fe"
# NEWS_API_KEY = "96185018a12545d4bb56495d65ab7382"
NEWS_API_KEY = "412ab9eba73743f0a29a0e02565a2b41"

base_url = 'https://newsapi.org/v1/'


def get_sources():
    """
    Get all the english language sources of news

    'https://newsapi.org/v1/sources?language=en'
    """
    # single threaded function
    url = base_url + "sources"
    params = {"language": "en"}
    resp = requests.get(url, params=params)
    data = resp.json()
    sources = [src['id'].strip() for src in data['sources']]
    print("all the sources")
    print(sources)
    return sources


def get_articles(source_list, results, thread):
    """
    https://newsapi.org/v1/articles?source=associated-press&sortBy=top&apiKey=1fabc23bb9bc485ca59b3966cbd6ea26
    """
    for source in source_list:
        url = base_url + "articles"
        params = {"source": source,
                  "apiKey": NEWS_API_KEY,
                  # "sortBy": "latest", # some sources don't support latest
                  "sortBy": "top",
                  # "sortBy": "popular",
                  }
        print("requesting:", source)
        resp = requests.get(url, params=params)
        if resp.status_code != 200:  # aiohttpp has "status"
            print("something went wrong with {}".format(source))
            print(resp)
            print(resp.text)
            return []
        data = resp.json()
        # the url to the article itself is in data['articles'][i]['url']
        new_titles = [str(art['title']) + str(art['description'])
                      for art in data['articles']]
        results.put(new_titles)
    print(f'done with thread sequence: {thread}')


def retrieve(source_dictionary):
    results = queue.Queue()
    # sl = source_list[:]

    def worker(*args):
        get_articles(*args)

    for i in range(len(source_dictionary)):
        source_list = source_dictionary[i]
        thread = threading.Thread(target=worker, args=(source_list, results, i))
        thread.start()
        print(f'Thread sequence {i} started: {thread.name}')
    return results


def count_word(word, titles):
    word = word.lower()
    count = 0
    for title in titles:
        if word in title.lower():
            count += 1
    return count


if __name__ == "__main__":
    # create a dictionary to assign news 'source' lists to threads
    # the keys will be the thread numbers
    # the values will be a list of news 'sources'
    d = {}
    # thread count
    tc = int(input('\nhow many threads would you like to run? >> '))
    WORD = input('what is the keyword you want to search for? >> ')
    sources = get_sources()
    for a, b in enumerate(sources):
        # get a thread 'key' value based on number of threads
        x = a % tc
        if x in d.keys():
            d[x].append(b)
        else:
            d.update({x: [b]})

    start = time.time()
    r = retrieve(d)
    art_count = 0
    word_count = 0
    for source in sources:
        titles = r.get()
        # print(f'\n{source} titles: {titles}')
        art_count += len(titles)
        word_count += count_word(WORD, titles)

    print('\n\n' + WORD, "found {} times in {} articles".format(word_count, art_count))
    print("Process took {:.0f} seconds".format(time.time() - start))
    print('number of threads =', tc, '\n')
