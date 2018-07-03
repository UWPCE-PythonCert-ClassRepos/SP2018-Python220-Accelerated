import pandas as pd

music = pd.read_csv('featuresdf.csv')

artists = [artists for artists in
           music[(music['danceability'] > 0.8) &
                 (music['loudness'] < -5.0)].artists]

songs = [name for name in
         music[(music['danceability'] > 0.8) &
               (music['loudness'] < -5.0)].name]

danceability = [danceability for danceability in
                music[(music['danceability'] > 0.8) &
                      (music['loudness'] < -5.0)].danceability]

spotify_data = list(zip(artists, songs, danceability))

sorted_spotify = sorted(spotify_data, key = lambda x: x[2], reverse = True)

print('Simple solution output: ')
for artist, song, dance in sorted_spotify[:5]:
    print(song)

print('\nA much more elegant solution output: ')
''' A much more elegant solution is below '''
spotify_query = [(artist, song, dance, loud)
             for (artist, song, dance, loud) in
             zip(music.artists, music.name, music.danceability, music.loudness)
             if (dance > 0.8) & (loud < -5.0)]

for artist, song, dance, loud in sorted(spotify_query,
                                        key = lambda x: x[2],
                                        reverse = True)[:5]:
    print(song)
