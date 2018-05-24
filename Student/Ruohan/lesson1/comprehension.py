import pandas as pd
music = pd.read_csv('featuresdf.csv')

gimme = music[music.danceability > 0.8]
gimme = gimme[music.loudness < -0.5]
gimme.sort_values(by = 'danceability', ascending = False)
gimme = gimme[['name', 'artists']]

print(gimme)
