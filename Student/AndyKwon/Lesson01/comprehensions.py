# Andy K
# Lesson01 
# Comprehensions


import pandas as pd
music = pd.read_csv("featuresdf.csv")


# comprehension for dance
dance = [x for x in music.danceability if x > 0.8]


# comprehension for loudness
loud = [x for x in music.loudness if x < -5.0]


# comprehension that fit both danceability and loudness criteria
# also sorts in descending order
danceloud = sorted([(track, dance, loud) for track, dance, loud in zip(music.name, music.danceability, music.loudness)
                     if dance > 0.8 and loud < -5], key = lambda x: x[1], reverse = True)

# print the first 5 song names that fit the above comprehension and sorting
for i in range(5):
    print(danceloud[i][0])

# RESULTS:
# Bad and Boujee (feat. Lil Uzi Vert)
# Fake Love
# HUMBLE.
# Bank Account
# You Don't Know Me - Radio Edit
