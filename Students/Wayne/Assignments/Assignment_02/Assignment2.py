
# coding: utf-8

# In[28]:


import pandas as pd
music = pd.read_csv('spotify.csv')


# In[16]:


music.head()


# # Ed Sheerhan Generator

# Write a generator to find and print all of your favorite artist’s tracks 
# from the data set. Your favorite artist isn’t represented in that set? 
# In that case, find Ed Sheeran’s tracks.
#
# Load the data set following the instructions from last week. Submit 
# your generator expression and the titles of Ed’s tracks.


# In[176]:


def thinking_outloud_generator():
    track = []
    for track in ([a, n] for a, n in zip(music.artists,
                                         music.name)
    if a == 'Ed Sheeran'):
        yield track

# # Get Amped Closures 

# Using the same data set, write a closure to capture high energy tracks.
# We will define high energy tracks as anything over 8.0. Submit your code
# and the tracks it finds, artist name, track name and energy value.

# In[140]:


def get_amped():
    energy = music.energy
    he = .8 < energy

    def high_energy():
        nonlocal he
        return([[a, n, he] for a, n, he in zip(music.artists,
                                               music.name,
                                               music.energy,
                                               he)])

    return ([[a, n, e, he] for a, n, e, he in zip(music.artists,
                                                  music.name,
                                                  music.energy,
                                                  he
                                                  )if he==True])

# In[141]:


if __name__ == "__main__":

    list(get_amped())
    print(thinking_outloud_generator())
    list(thinking_outloud_generator())
