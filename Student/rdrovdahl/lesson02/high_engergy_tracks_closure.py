#! /usr/local/bin/python3


'''
Write a closure to find and print all 'high energy' tracks from the data
set.
'''

import pandas as pd


def music_filter():
    music = pd.read_csv("featuresdf.csv")

    def high_energy(val):
        nonlocal music
        return music[music.energy > val][['artists', 'name', 'energy']]
    return high_energy


energy_filter = music_filter()
print(energy_filter(0.8))
