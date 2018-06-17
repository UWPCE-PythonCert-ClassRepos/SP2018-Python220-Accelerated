import pandas

spotify = pandas.read_csv('featuresdf.csv')

#Generators
data = ((artist, song) for (artist, song) in zip(spotify.artists, spotify.name)
                                          if artist == 'Kendrick Lamar')
print('Generator ouput - Kendrick Lamar tracks: ')
for artist, song in data:
    print(song)

#Closures
def ingest_data(filename):
    spotify = pandas.read_csv(filename)
    data = ((artist, song, energy) for (artist, song, energy)
                           in zip(spotify.artists, spotify.name, spotify.energy)
                           if energy >= 0.8)
    def print_high_energy():
        print('Artist' + ' ' * 14, 'Song' + ' ' * 46, 'Energy')
        for artist, song, energy in data:
            print(artist + ' ' * (20 - len(artist)),
                  song + ' ' * (50 - len(song)),
                  energy)
    return print_high_energy()

print('Generator ouput - Kendrick Lamar tracks: ')
ingest_data('featuresdf.csv')
