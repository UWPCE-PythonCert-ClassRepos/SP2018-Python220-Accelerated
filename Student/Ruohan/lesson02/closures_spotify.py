#! /usr/local/bin/python3

import pandas as pd
music = pd.read_csv('featuresdf.csv')

def high_engergy_check(critical_value = 0.8):
    value = critical_value
    def high_energy_track(file = music):
        nonlocal value
        return file[['name', 'artists', 'energy']][file['energy'] > value]
    return high_energy_track

high_energy = high_engergy_check(0.8)
print(high_energy(music))
