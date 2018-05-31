#!/usr/bin/env python3

import pandas as pd

def generate_list(artist="Ed Sheeran"):
    music = pd.read_csv("featuresdf.csv")
    my_gen_exp=(x['name'] for _, x in music.iterrows() if x['artists'] == artist)

    print("\n***Printing songs by", artist, "using Generator expression***")
    for x in my_gen_exp:
        print("\t",x)

def return_generator(artist="Ed Sheeran"):
    music = pd.read_csv("featuresdf.csv")
    return (x['name'] for _, x in music.iterrows() if x['artists'] == artist)


if __name__ == "__main__":
    generate_list()
