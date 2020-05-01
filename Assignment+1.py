
# coding: utf-8

# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[1]:


w=[]
for i in range(2000,3200):
    if i % 7 == 0 and i % 5 == 1:
        w.append(i)
       
        
        
        
print((w),sep=",")


# 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name

# In[3]:


a=input('Enter a name:')
b=input('Enter last name:')
print(a[::-1], b[::-1],end=" ")


# 3. Write a Python program to find the volume of a sphere with diameter 12 cm. 
#   Formula = V=4/3 * π * r^3

# Given:diameter of sphere d= 12 cm
# To find:Volume of Sphere
# Solution:
# V=4/3*π r^3
# r is calculated as d/2
# 12/2 is 6cm
# 
# 
# 

# In[2]:


V=4/3*3.14*6**3
print(V)


# Note:I have used the standard value of pi so as to calculate volume without importing math library
# correct me if i am wrong
