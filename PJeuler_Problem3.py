#!/usr/bin/env python
# coding: utf-8

# In[3]:


num = 600851475143
i = 2
list = []
while num > 1:
    if num % i == 0:
        list.append(i)
        num = num / i
    else:
        i += 1
print(list)
print(i)


# In[ ]:




