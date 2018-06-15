#!/usr/bin/env python3
'''
Your job, now, is to get artists and song names for for tracks with danceability
scores over 0.8 and loudness scores below -5.0. In other words, quiet yet danceable tracks.
'''
import pandas as pd

MUSIC = pd.read_csv("featuresdf.csv")
SMOOTH_DANCE = [{'id':id, 'name':name, 'artist':artist, 'danceability':da, 'loudness':loud} \
for id, name, artist, da, loud in \
zip(MUSIC.id, MUSIC.name, MUSIC.artists, MUSIC.danceability, MUSIC.loudness) \
if da > 0.8 and loud < -5.0]
sorted(SMOOTH_DANCE, key=lambda x: x['danceability'], reverse=True)

def music_gen(music_obj, artist_name):
    music_comp = ({'id':id, 'name':name, 'artist':artist, 'danceability':da, 'loudness':loud} \
    for id, name, artist, da, loud in \
    zip(music_obj.id, music_obj.name, music_obj.artists, \
    music_obj.danceability, music_obj.loudness) \
    if artist_name in artist)
    for i in music_comp:
        yield i

def music_closure(music_obj):
    music_list = [{'id':id, 'name':name, 'artist':artist, 'energy':ene} \
    for id, name, artist, ene in \
    zip(music_obj.id, music_obj.name, music_obj.artists, music_obj.energy)]
    #print(music_list)
    def high_energy(energy_level=0.8):
        return [i for i in music_list if i['energy'] > energy_level]
    return high_energy

def main():
    print('Favorite Artist: Kendrick Lamar')
    a = music_gen(MUSIC, 'Kendrick Lamar')
    for i in range(2):
        print(next(a))

    print('High Energy Music')
    b = music_closure(MUSIC)()
    for i in b:
        print(i)

if __name__ == '__main__':
    main()
