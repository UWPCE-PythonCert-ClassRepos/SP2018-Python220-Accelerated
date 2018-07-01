
# coding: utf-8

# # Comprehensions

# Bring up an interpreter and load the data.

# In[1]:


import pandas as pd 
music = pd.read_csv('spotify.csv')


# music.head gives us the headers and the overall datashape from the csv file 

# In[2]:


music.head()


# music.describe gives us the count, mean, std, min, quartiles and max 

# In[3]:


music.describe()


# The following function gives us tracks with danceability greater than .8 

# In[4]:


[d for d in music.danceability if d > 0.8]


# Returns tracks with a loudness score under -5.0

# In[5]:


[l for l in music.loudness if l < -5.0]


# In[6]:


def shake_it_off():
    
    return(sorted([[a, n, d, l] for a, n, d, l in zip(music.artists,
                                                      music.name,
                                                      music.danceability,
                                                      music.loudness)
    if d >.8 and l < -5.0],key=lambda x: x[2],reverse =True))



# In[7]:


print(shake_it_off())


# -------------------------------------------------------------------------------------------
#
#
# The following songs below meet both the danceability and loudness constraints listed in the assignment.
#
# 1. ['Migos', 'Bad and Boujee (feat. Lil Uzi Vert)', 0.927, -5.313],
# 2. ['Drake', 'Fake Love', 0.927, -9.433],
# 3. ['Kendrick Lamar', 'HUMBLE.', 0.904, -6.8420000000000005],
# 4. ['21 Savage', 'Bank Account', 0.884, -8.228],
# 5. ['Jax Jones', "You Don't Know Me - Radio Edit", 0.8759999999999999, -6.053999999999999],
# 6. ['Liam Payne', 'Strip That Down', 0.8690000000000001, -5.595],
# 7. ['Future', 'Mask Off', 0.833, -8.795],
# 8. ['Zion & Lennox', 'Otra Vez (feat. J Balvin)', 8.0.8320000000000001, -5.428999999999999],
# 9. ['Drake', 'Passionfruit', 0.809, -11.377]]
#
# -------------------------------------------------------------------------------------------
