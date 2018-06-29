#! /usr/local/bin/python3

import pandas as pd
music = pd.read_csv('featuresdf.csv')

title_artists = zip(music.name, music.artists)

gen1 = (Ed_data for Ed_data in title_artists if Ed_data[1] == 'Ed Sheeran')
play_list_ES = list(gen1)
print(play_list_ES)
