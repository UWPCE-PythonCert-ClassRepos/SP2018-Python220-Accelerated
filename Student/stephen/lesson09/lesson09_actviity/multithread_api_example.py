import requests
import threading
import json
from math import ceil
import sqlite3

api_key = '0b8b3765b41643e69374333bb63a4d5a'
keywords = ','.join(['Amazon', 'Bezos'])
page = 1
url = (f'https://newsapi.org/v2/everything?'
        'q={keywords}&'
        'from=2018-06-21&'
        'sortBy=popularity&'
        'apiKey={api_key}&'
        'page={page}')

url = url.format(keywords=keywords, page=page, api_key=api_key)
print(url)

