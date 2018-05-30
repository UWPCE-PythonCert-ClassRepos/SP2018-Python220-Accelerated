#!/usr/bin/env python3

import pandas as pd

music = pd.read_csv("featuresdf.csv")

# Get artists and song names for tracks with danceability scores over 0.8 and loudness scores below 5.0.
playlist = [(track, artist, dance, vol) for track, artist, dance, vol
            in zip(music.name, music.artists, music.danceability, music.loudness)
            if dance > 0.8 and vol < 5.0]

# Sort tracks in decending order of danceability score, so most danceable tracks are on top.
pretty_playlist = sorted(playlist, key=lambda x: x[2], reverse=True)

# Print top 5 tracks
for song in pretty_playlist[:5]:
    print(song)
