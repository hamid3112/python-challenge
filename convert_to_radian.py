#!/usr/bin/env python
# coding: utf-8

# In[56]:


from math import pi
digree = float(input())
if digree>=0 and digree<=360:
    radian = (digree*pi)/180
    print(f"{radian:.10}")

    

