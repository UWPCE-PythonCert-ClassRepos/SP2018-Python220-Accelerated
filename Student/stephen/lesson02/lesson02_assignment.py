import pandas as pd


music = pd.read_csv("featuresdf.csv")


songlist = zip(music.name, music.artists)

# Generator
ed_sheeran =  ((artists, name) for name, artists in songlist if "Sheeran" in artists)

# print Ed Sheeran songs using generator
while True:
    try:
        print(next(ed_sheeran))
    except StopIteration:
        break

# Closure
tracklist =  zip(music.artists, music.name, music.energy)

def energy(tracklist):
    def filtered_list(threshold):
        for name, artists, energy in tracklist:
            if energy >= threshold:
                print(name, ', ', artists, ', ', energy)
        return [(artists, name, energy) for name, artists, energy in tracklist if energy >= threshold]
    return filtered_list


high_energy = energy(tracklist)
high_energy(0.8)
