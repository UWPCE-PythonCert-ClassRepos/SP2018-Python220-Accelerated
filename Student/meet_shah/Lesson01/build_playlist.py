#!/usr/bin/env python3
"""
Build Playlist
Reads a csv file with list of songs and their danceability and loudness values
Prints a list with danceability > 0.8 and loudness < -0.5 sorted by highest danceability
"""

import pandas as pd
from operator import itemgetter

def process_list():

    music = pd.read_csv("featuresdf.csv")
    mylist = [x for _, x in music.iterrows() if x['danceability'] > 0.8 and x['loudness'] < -0.5]
    #test.sort_values(by = 'danceability', ascending = False)
    mylist = sorted(mylist, key=itemgetter(3), reverse=True)
    print("\nSong Name : Artist Name")
    print("-----------------------")
    [print(x['name'],":", x['artists']) for x in mylist]


if __name__ == "__main__":
    process_list()
