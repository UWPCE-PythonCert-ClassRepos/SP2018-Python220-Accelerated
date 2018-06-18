#!/usr/bin/env python3

import generate_tracks_by_artist as my_gen
import pandas as pd
import pytest

def test_gen_input1():
    music = pd.read_csv("featuresdf.csv")
    sheeran_generator = my_gen.return_generator()
    assert next(sheeran_generator) == "Shape of You"
    assert next(sheeran_generator) == "Castle on the Hill"
    assert next(sheeran_generator) == "Galway Girl"
    assert next(sheeran_generator) == "Perfect"
    with pytest.raises(StopIteration):
        assert next(sheeran_generator)

def test_gen_input2():
    music = pd.read_csv("featuresdf.csv")
    ocean_generator = my_gen.return_generator("Danny Ocean")
    assert next(ocean_generator) == "Me Rehúso"
    with pytest.raises(StopIteration):
        assert next(ocean_generator)
