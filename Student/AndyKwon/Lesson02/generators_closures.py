# Andy K
# Lesson02
# Generators & Closures


import pandas as pd
music = pd.read_csv("featuresdf.csv")


# Generator by artist
"""
Write a generator to find and print all of your favorite artist’s tracks from the data set
"""

def artist_generator(name = ""):

    for artist_name_combo in ([artist, name] for artist, name in zip(music.artists, music.name)):
        if artist_name_combo[0] == name:
            yield artist_name_combo

x = artist_generator("Ed Sheeran")
print(list(x))

"""
Results:
[['Ed Sheeran', 'Shape of You'],
 ['Ed Sheeran', 'Castle on the Hill'],
 ['Ed Sheeran', 'Galway Girl'],
 ['Ed Sheeran', 'Perfect']]
"""


# Closure
"""
Using the same data set, write a closure to capture high energy tracks
"""

def make_high_energy():
    def high_energy(val = 0):
        return sorted([(artist, track, energy) for artist, track, energy in zip(music.artists, music.name, music.energy)
                     if energy > val], key = lambda x: x[1], reverse = True)
    return high_energy

x = make_high_energy()

x(0.8)


"""
Results:
 ('Jason Derulo', 'Swalla (feat. Nicki Minaj & Ty Dolla $ign)', 0.8170000000000001),
 ('Martin Jensen', 'Solo Dance', 0.836),
 ('Enrique Iglesias', 'SUBEME LA RADIO', 0.823),
 ('CNCO', 'Reggaetón Lento (Bailemos)', 0.838),
 ('Maggie Lindemann', 'Pretty Girl - Cheat Codes X CADE Remix', 0.868),
 ('Danny Ocean', 'Me Rehúso', 0.804),
 ('Steve Aoki', 'Just Hold On', 0.932),
 ('The Weeknd', 'I Feel It Coming', 0.813),
 ('Ed Sheeran', 'Galway Girl', 0.8759999999999999),
 ('Wisin', 'Escápate Conmigo', 0.8640000000000001),
 ('The Chainsmokers', "Don't Let Me Down", 0.8590000000000001),
 ('Luis Fonsi', 'Despacito - Remix', 0.815),
 ('Post Malone', 'Congratulations', 0.812),
 ('Katy Perry', 'Chained To The Rhythm', 0.8009999999999999),
 ('Ed Sheeran', 'Castle on the Hill', 0.8340000000000001),
 ('Starley', 'Call On Me - Ryan Riback Extended Remix', 0.843),
 ('The Vamps', 'All Night', 0.809),
 ('Bruno Mars', '24K Magic', 0.8029999999999999)]
 """