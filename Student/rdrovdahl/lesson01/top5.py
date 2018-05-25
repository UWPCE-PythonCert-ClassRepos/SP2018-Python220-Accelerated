#! /usr/local/bin/python3


'''
use pandas to scrub top 100 csv file and find songs with with danceability
scores over 0.8 and loundess scores under -5.0
'''

import pandas as pd

music = pd.read_csv("featuresdf.csv")

l1 = [(b,a,c,d) for a,b,c,d in zip(music.name, music.artists, music.danceability, music.loudness) if c > 0.8 and d < -5.0]
l2 = sorted(l1, key=lambda danceability: danceability[2], reverse=True)

print('\n\nTop 5 - Quiet Dance Songs\n  Sorted by Danceability:')

for c, line in enumerate(l2, 1):
    if c <= 5:
        print(c, line[0] + ' --> ' + line[1])
