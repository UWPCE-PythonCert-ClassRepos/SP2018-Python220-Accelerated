
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


music = pd.read_csv("featuresdf.csv")


# In[4]:


music.head()


# In[5]:


music.describe()


# In[6]:


[x for x in music.danceability if x > 0.8]


# #### Your job, now, is to get artists and song names for tracks with danceability scores over 0.8 and loudness scores below -5.0.
# #### Also, these tracks should be sorted in descending order by danceability so that the most danceable tracks are up top.

# In[28]:


# zip the artists, songs, danceability and loudness
songlist = zip(music.name, music.artists, music.danceability, music.loudness)


# In[29]:


filteredsongs = [(name, artists, danceability, loudness) for name, artists, danceability, loudness in songlist if danceability > 0.8 and loudness < -5.0]


# In[42]:


topfive = pd.DataFrame(sorted(filteredsongs, key=(lambda x: x[2]), reverse=True), columns=['name', 'artists', 'danceability', 'loudness'])


# In[45]:
topfive.head(5)

if __name__ == '__main__':
    print(topfive.head(5))


