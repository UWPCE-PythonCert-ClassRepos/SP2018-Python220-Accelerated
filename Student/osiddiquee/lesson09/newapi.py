import requests
import threading
from math import ceil
import time

#############################
## Assignment              ##
#############################
# If you are struggling with the assignment from
# lesson 9, then modify this script to run.
# I have purposefully disabled the threading code
# to not work (silently... no error will occur).


###################################
## Other Suggested modifications ##
###################################
# - Use recursive function for API pagination
# - Persist / store data collected from API
# - Use generator for API pagination
# - Trying multiprocessing and queue packages
# - Rewrite the whole script


###########################
## Persist or store data ##
###########################
# import sqlite3
# import json
# import pymongo


#################################
## Get initial result metadata ##
#################################
api_key = "d841cf2b36404cc98115f9328bfdfaec"
keywords= ",".join(["Nintendo","Sony", "Microsoft"])
page = 1
url = (f'https://newsapi.org/v2/everything?'
       'q={keywords}&'
       'from=2018-06-21&'
       'sortBy=popularity&'
       'apiKey={api_key}&'
       'page={page}')

url = url.format(keywords=keywords, page=page, api_key=api_key)
print("API URL:", url)

response = requests.get(url)
totalResults = response.json()["totalResults"]
resultsPerPage = len(response.json()["articles"]) # defaults to 20
numPages = ceil(totalResults/resultsPerPage)


################################
## Define `get_page` function ##
## w/ `page` parameter        ##
################################
def get_page(page):
    url = (f'https://newsapi.org/v2/everything?'
           'q={keywords}&'
           'from=2018-06-21&'
           'sortBy=popularity&'
           'apiKey={api_key}&'
           'page={page}')

    url = url.format(keywords=keywords, page=page, api_key=api_key)

    r = requests.get(url)
    if r.status_code == 200:
        raw = r.json()
        articles = raw["articles"]
        ##############################################
        ## `articles` is essentially your data....  ##
        ## do something with it here                ##
        ##############################################
        with open('search_data.csv', 'a') as search_csv:
             for article in articles:
                 #article_row = {}
                 # article_row['title'] = article['title']
                 # article_row['author'] = article['author']
                 # article_row['url'] = article['url']

                 title = article['title']
                 author = article['author']
                 link = article['url']

                 # i want a perfectly clean dataset
                 # i doubt i would lose much data because of multithreading...
                 #       allowing me to get a lot efficiently
                 if not (title or author or link):
                     search_csv.write(f'''{article['title'].encode('utf8')},
                                          {article['author'].encode('utf8')},
                                          {article['url'].encode('utf8')}''')
                 else:
                     pass

    else:
        print("API Error - Status Code", r.status_code)


##############################################
## This here is the single threaded version ##
##############################################
start = time.time()
for i in range(numPages):
    get_page(i+1)
end = time.time()
print("single threaded time: %.3f seconds", end - start)



#############################################
## This here is the multi-threaded version ##
#############################################
start = time.time()
threads = []
for i in range(numPages):
    thread = threading.Thread(target = get_page, args = ((i+1,)))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
end = time.time()
print("multi-threaded time: %.3f seconds", end - start)
