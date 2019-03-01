#!/usr/bin/env python
# coding: utf-8

# In[26]:


x=[]
for i in range(100,1000):
    for k in range(i, 1000):
        answer = i*k
        answer_str = str(answer)
        if (answer_str[::-1]) == answer_str:
            x.append(answer_str)
            x=[int(i) for i in x]
print(max(x))


# In[ ]:




