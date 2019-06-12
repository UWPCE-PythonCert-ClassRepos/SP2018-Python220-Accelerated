#!usr/local/bin/python3

"""

Py220: Advanced Programming in Python
Lesson 01 Activity and Assignment

Comprehensions
Use Pandas library to find music that you can dance to and is not too loud. 

"""

import pandas as pd

music = pd.read_csv("featuresdf.csv")
# print(music)

# print("File head: \n", music.head())
# print("Description: \n", music.describe())

# use a comprehension to get danceability scores over 0.8
#dance_level = sorted([x for x in music.danceability if x > 0.8], reverse= True)
#print(dance_level)


# Now, get artists and song names for tracks with danceability scores over 0.8 and loudness scores below -5.0. 
# Sort tracks in descending order by danceability 
# While you could use Pandas features along the way, you don’t need to. 
# Handy library functions include zip() and sorted().


quiet_and_dance = [x for x in zip(music.artists, music.name, music.danceability, music.loudness)
                   if x[2] > 0.8 and x[3] < -5.0]
                   
# print(quiet_and_dance)

top5 = sorted(quiet_and_dance, key=lambda x: x[2], reverse = True)

print("The top 5 danceable and quiet songs:")
for x in top5[:5]:
    print("  -{}, {}".format(x[0], x[1]))