#=========================================================================================
#Name: Comprehensions - Quiet yet Danceable Tracks
#Author: Wesley Wang
#Date: 5/28/2018
#=========================================================================================

import pandas as pd

music = pd.read_csv("C:\_Python220AC\SP2018-Python220-Accelerated\Student\WesWang\Lesson1\Assignment\\featuresdf.csv")

def quiet_danceable():
    dlist = [(name, artist, dance, loud) for (name, artist, dance, loud) 
        in zip(music.name, music.artists, music.danceability, music.loudness) if dance > 0.8 and loud < -5]
    
    output = ""
    header = ["Name", "Artist", "Danceability", "Loudness"]
    output = f"{header[0]:40}{header[1]:20}{header[2]:15}{header[3]:15}\n" + "-"*90
    for song in sorted(dlist, key=lambda song:song[2], reverse=True):
        output += "\n{:40}{:20}{:<15,.5f}{:<15,.5f}".format(song[0], song[1], song[2], song[3])
    
    return output

print(quiet_danceable())

