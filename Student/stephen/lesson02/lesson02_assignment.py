import pandas as pd


music = pd.read_csv("featuresdf.csv")


songlist = zip(music.name, music.artists)

# Generator
def fav_generator(artist, songlist):
    return ((artists, name) for name, artists in songlist if artist in artists)

ed_sheeran =  fav_generator("Ed Sheeran", songlist)

# print Ed Sheeran songs using generator
while True:
    try:
        print(next(ed_sheeran))
    except StopIteration:
        break

# Output:
# ('Ed Sheeran', 'Shape of You')
# ('Ed Sheeran', 'Castle on the Hill')
# ('Ed Sheeran', 'Galway Girl')
# ('Ed Sheeran', 'Perfect')



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

# Output:
# Luis Fonsi ,  Despacito - Remix ,  0.815
# Post Malone ,  Congratulations ,  0.812
# Jason Derulo ,  Swalla (feat. Nicki Minaj & Ty Dolla $ign) ,  0.8170000000000001
# Ed Sheeran ,  Castle on the Hill ,  0.8340000000000001
# Imagine Dragons ,  Thunder ,  0.81
# Shawn Mendes ,  There's Nothing Holdin' Me Back ,  0.8
# Danny Ocean ,  Me Rehúso ,  0.804
# Ed Sheeran ,  Galway Girl ,  0.8759999999999999
# The Weeknd ,  I Feel It Coming ,  0.813
# Starley ,  Call On Me - Ryan Riback Extended Remix ,  0.843
# Martin Jensen ,  Solo Dance ,  0.836
# Enrique Iglesias ,  SUBEME LA RADIO ,  0.823
# Maggie Lindemann ,  Pretty Girl - Cheat Codes X CADE Remix ,  0.868
# Bruno Mars ,  24K Magic ,  0.8029999999999999
# Katy Perry ,  Chained To The Rhythm ,  0.8009999999999999
# Wisin ,  Escápate Conmigo ,  0.8640000000000001
# Steve Aoki ,  Just Hold On ,  0.932
# CNCO ,  Reggaetón Lento (Bailemos) ,  0.838
# The Vamps ,  All Night ,  0.809
# The Chainsmokers ,  Don't Let Me Down ,  0.8590000000000001
