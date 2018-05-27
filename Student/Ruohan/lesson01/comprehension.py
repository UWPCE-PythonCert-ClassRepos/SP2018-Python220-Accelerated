#! /usr/local/bin/python3

import pandas as pd
music = pd.read_csv('featuresdf.csv')


# use pandas
gimme = music[music.danceability > 0.8]
gimme = gimme[music.loudness < -0.5]
gimme.sort_values(by = 'danceability', ascending = False)
gimme = gimme[['name', 'artists']]
print(gimme)


#use comprehension
paly_list = [(name,artists,dancebility,loudness) \
      for name,artists,dancebility,loudness in \
      zip(music.name, music.artists, music.danceability, music.loudness) \
      if dancebility > 0.8 and loudness < -5.0]

sorted_paly_list = sorted(paly_list, key = lambda x: x[2], reverse = True)
