#!/usr/bin/env python
# coding: utf-8

# In[131]:


#Queen's move
m , n = input()
colums = ["a" , "b" , "c" ,"d" ,"e" , "f" , "g" , "h"]
m = colums.index(m) +1
n = int(n)
for i in range(8,0 ,-1):
    for j in range(1,9):
        if j == m and i ==n:
            print("Q" , end=" ")
            
        elif  j == m or i == n or j+i==m+n or j-i==m-n:
            print("X" , end=" ")
            
        else:
            print("." , end=" ")
    print()
        
             

