
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('load_ext', 'Cython')


# In[4]:


get_ipython().run_cell_magic('cython', '', '# purely about speed\ncdef int a = 0\nfor i in range(10):\n    a += 1\nprint(a)')


# In[6]:


#tells you what cython is up to
%%cython --annotate

cdef int a = 0
for i in range(10):
    a += 1
print(a)

