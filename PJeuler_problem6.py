#!/usr/bin/env python
# coding: utf-8

# In[7]:


ans1 = 0
ans2 = 0

for i in range(1,101):
    ans1 += i**2
    ans2 += i
    print(ans2**2 - ans1)


# In[ ]:




