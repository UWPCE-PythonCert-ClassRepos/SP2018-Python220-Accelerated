#! /usr/local/bin/python3


'''
Write a generator to find and print all of your favorite tracks from the data
set.
'''

import pandas as pd

music = pd.read_csv("featuresdf.csv")


def fav_finder(artist):
    'generator to iterate over data set and return tracks from artist'
    i = 0
    max = (len(music)-1)
    while True:
        if music.loc[i].artists == artist:
            yield music.loc[i].artists, music.loc[i]['name']
        if i < max:
            i += 1
        else:
            break


fav = fav_finder('Imagine Dragons')

while True:
    try:
        x = next(fav)
        print(x[0], ' -- ', x[1])
    except StopIteration:
        break
