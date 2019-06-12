#!usr/local/bin/python3

"""

Py220: Advanced Programming in Python
Lesson 02 Assignment: Generators and Closures

Generators and Closures

"""


import pandas as pd

music = pd.read_csv("featuresdf.csv")

# write a generator to print all of Ed Sheeran’s tracks
music_data = [x for x in zip(music.artists, music.name)]

def track_generator(music_data):
    for data in music_data:
        if data[0] == "Ed Sheeran":
            yield "{}: {}".format(data[0], data[1])

ed_sheeran = track_generator(music_data)
print(next(ed_sheeran))
print(next(ed_sheeran))
print(next(ed_sheeran))
print(next(ed_sheeran))
print()



# Write a closure to capture high energy tracks over 8.0. 
music_data2 = [x for x in zip(music.artists, music.name, music.energy)
               if x[2] > 0.8]

def high_energy_closure():
    def return_high_energy(music_data2):
        return sorted(music_data2, key=lambda x: x[2], reverse=True)
    return return_high_energy(music_data2)


# Submit your code and the tracks it finds, artist name, track name and energy value.
energy_data = high_energy_closure()
for data in energy_data:
    print(data[0], data[1], data[2])
