#=========================================================================================
#Name: Generators - 2
#Author: Wesley Wang
#Date: 5/30/2018
#=========================================================================================

import pandas as pd

music = pd.read_csv("C:\_Python220AC\SP2018-Python220-Accelerated\Student\WesWang\Lesson2\Assignment\\featuresdf.csv")

generator_ed = ((name, artist) for (name, artist) in zip(music.name, music.artists) if artist == 'Ed Sheeran')

print("""Ed Sheeran's tracks:""")
for track in sorted(generator_ed, key=lambda track:track[0]):
  print(track[0])