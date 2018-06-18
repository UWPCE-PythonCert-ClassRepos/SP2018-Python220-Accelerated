#!/usr/bin/env python3

import lesson02_closure as closure
import pandas as pd

def test_closure_default():
    music = pd.read_csv("featuresdf.csv")
    test_obj = [(x['name'],x['artists'],x['energy']) for _, x in music.iterrows() if x['energy'] >= 0.8]
    myfunc = closure.high_energy_tracks()
    assert myfunc("featuresdf.csv") == test_obj

def test_closure_07():
    music = pd.read_csv("featuresdf.csv")
    test_obj = [(x['name'],x['artists'],x['energy']) for _, x in music.iterrows() if x['energy'] >= 0.7]
    myfunc = closure.high_energy_tracks(0.7)
    assert myfunc("featuresdf.csv") == test_obj

def test_closure_file_switch():
    #assert with normal file
    music = pd.read_csv("featuresdf.csv")
    test_obj = [(x['name'],x['artists'],x['energy']) for _, x in music.iterrows() if x['energy'] >= 0.7]
    myfunc = closure.high_energy_tracks(0.7)
    assert myfunc("featuresdf.csv") == test_obj

    #assert with a different file
    new_music = pd.read_csv("featuresdf_small.csv")
    test_obj = [(x['name'],x['artists'],x['energy']) for _, x in new_music.iterrows() if x['energy'] >= 0.7]
    myfunc = closure.high_energy_tracks(0.7)
    assert myfunc("featuresdf_small.csv") == test_obj
