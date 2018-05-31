#=========================================================================================
#Name: Closure
#Author: Wesley Wang
#Date: 5/30/2018
#=========================================================================================

import pandas as pd

music = pd.read_csv("C:\_Python220AC\SP2018-Python220-Accelerated\Student\WesWang\Lesson2\Assignment\\featuresdf.csv")

def high_energy(music):
  tracks = [(name, artist, energy) for (name, artist, energy) in zip(music.name, music.artists, music.energy) if energy > 0.8]
  def print_track():
    header = ["Name", "Artist", "Energy"]
    print(f"{header[0]:45}{header[1]:20}{header[2]:15}\n" + "-"*80)
    for track in sorted(tracks, key=lambda track:track[2], reverse=True):
      print("\n{:45}{:20}{:<15,.5f}".format(track[0], track[1], track[2]))
  return print_track()

high_energy(music)