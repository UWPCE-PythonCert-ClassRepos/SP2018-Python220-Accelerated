import pandas as pd
music = pd.read_csv('featuresdf.csv')

print(music.head())
print(music.describe())
gimme = [x for x in music.danceability if x > 0.8]
print(gimme)
