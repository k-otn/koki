#!/usr/bin/env python
# coding: utf-8

# In[ ]:


sum = 0
max = 4000000:
a = 1
b = 2
c = a + b

while c < 4000000:
    if c % 2 == 0:
        sum += c
        a = b
        b = c
        c = a + b
        
print(sum)


# In[ ]:




