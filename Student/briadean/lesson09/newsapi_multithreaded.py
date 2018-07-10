#! /usr/local/bin/python3
"""
Multithreaded NewsAPI application to retrieve all top articles for the day and count keyword appearances
#todo Only return the links/articles which contain the keyword
"""
import threading
import queue
import requests

# may need to rotate these API keys due to rate limiting by the provider
# NEWS_API_KEY = "b87ea971889947be8fe13d7415d62fd3"
# NEWS_API_KEY = "7dcd6b9672554311baa382dcee400d47"
# NEWS_API_KEY = "ae06b517678b4b52a1b160f3ea8a348d"
NEWS_API_KEY = "19dbae9aad404094bebc1b133504b479"

base_url = "https://newsapi.org/v1/"


def get_sources():
    """
    Retrieve English language sources of news
    """
    url = base_url + "sources"
    params = {"language": "en"}
    response = requests.get(url, params=params)
    data = response.json()
    sources = [src['id'].strip() for src in data['sources']]
    return sources


def get_articles(source_list, results, thread):
    """
    Retrieve articles mentioned user provided keyword
    """
    for source in source_list:
        url = base_url + "articles"
        params = {"source": source,
                  "apiKey": NEWS_API_KEY,
                  "sortBy": "top"}
        print("Retrieved from:", source)  # It only seems to be getting some things and not others? Fix?
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print("API Error - Status Code", response.status_code)
            return []

        data = response.json()
        # the url to the article itself is in data['articles'][i]['url']
        new_titles = [str(art["title"]) + str(art["description"])
                      for art in data["articles"]]
        new_links = [str(url["url"]) for url in data["articles"]]
        results.put(new_links)
        results.put(new_titles)
    print(f"{thread} Completed")


def retrieve(source_dict):
    results = queue.Queue()

    def worker(*args):
        get_articles(*args)

    for i in range(len(source_dict)):
        source_list = source_dict[i]
        thread = threading.Thread(target=worker, args=(source_list, results, i))
        thread.start()
        print(f"Thread sequence {i} started: {thread.name}")
    return results


def count_word(word, titles):
    """Count keyword appearances"""
    word = word.lower()
    count = 0
    for title in titles:
        if word in title.lower():
            count += 1
    return count


if __name__ == "__main__":
    """Dictionary to store news source threads lists
    Keys = thread numbers/names
    Values = list of articles
    """
    thread_dict = {}

    num_threads = int(input("\nHow many threads would you like to utilize?>> "))
    keyword = input("Which keyword would you like to find? >> ")
    sources = get_sources()

    for a, b in enumerate(sources):
        # Get thread key value
        x = a % num_threads
        if x in thread_dict.keys():
            thread_dict[x].append(b)
        else:
            thread_dict.update({x: [b]})

    r = retrieve(thread_dict)
    art_count = 0
    word_count = 0

    for source in sources:
        titles = r.get()
        print(f"\n{source} Titles: {titles}\n")
        art_count += len(titles)
        word_count += count_word(keyword, titles)

    print("\n\n" + keyword, "appeared {} times in {} articles".format(word_count, art_count))
