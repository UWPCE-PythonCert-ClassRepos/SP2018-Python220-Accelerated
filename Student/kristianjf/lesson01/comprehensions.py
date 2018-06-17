#!/usr/bin/env python3
'''
Your job, now, is to get artists and song names for for tracks with danceability
scores over 0.8 and loudness scores below -5.0. In other words, quiet yet danceable tracks.
'''
import pandas as pd

MUSIC = pd.read_csv("featuresdf.csv")
SMOOTH_DANCE = [{'id':id, 'name':name, 'artist':artist, 'danceability':da, 'loudness':loud} \
for id, name, artist, da, loud in \
zip(MUSIC.id, MUSIC.name, MUSIC.artists, MUSIC.danceability, MUSIC.loudness) \
if da > 0.8 and loud < -5.0]
sorted(SMOOTH_DANCE, key=lambda x: x['danceability'], reverse=True)
