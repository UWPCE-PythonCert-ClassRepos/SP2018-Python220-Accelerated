'''
Jay Johnson - Lesson01 - Assignment01 - Comprehensions

Dance Party
////
v1.0 sorting isnt that efficent
need to add top 5 or 10
////
'''

import pandas as pd
music = pd.read_csv("featuresdf.csv")

#music = sorted(music)
#print(music)

music.head()
music.describe()
music.name
music.artists
music.loudness

dance = [x for x in music.danceability if x > 0.8]
loud = [y for y in music.loudness if y < -5.0]

#[x for x in music.danceability if x > 0.8]
#[y for y in music.loudness if y < -5.0]
#[y for y in music.loudness if y < -5.0]

#both_of_them = [(x for x in music.danceability if x > 0.8) or (y for y in music.loudness if y < -5.0)]

#print(both_of_them)\
#print(dance)
#print(loud)

loud = sorted(loud)
dance = sorted(dance)

#music.query('music.danceability == dance | music.loudness == loud')

#some_value = float(-6.769)

# print from list[0]
loud_len = len(loud)
dance_len = len(dance)

print(dance_len)

#new_artist = music[music.loudness == loud[1]]
#print(new_artist.name)
#print(new_artist.artists)


# Your job, now, is to get artists and song names
# for for tracks with
# danceability scores over 0.8 and loudness scores below -5.0
for i in range(0, loud_len):
    new_artist = music[music.loudness == loud[i]]
    #print(new_artist.name)
    #print(new_artist.artists)
    # compare loop here
    for i2 in range(0, dance_len):
        new_artist_2 = music[music.danceability == dance[i2]]
        #print(new_artist_2.name)
        #print(new_artist_2.artists)
        name1 = new_artist.name
        name2 = new_artist_2.name
        if str(name1) == str(name2):
            print(new_artist.name)
            print(new_artist.artists)
        #else:
            #print('nope')
    i2=0
