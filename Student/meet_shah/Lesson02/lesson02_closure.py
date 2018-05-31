#!/usr/bin/env python3

import pandas as pd

def high_energy_tracks(energy=0.8):

    energy = energy

    def print_tracks(filename):
        music = pd.read_csv(filename)
        return [(x['name'],x['artists'],x['energy']) for _, x in music.iterrows() if x['energy'] >= energy]

    return print_tracks
