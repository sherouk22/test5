#!/usr/bin/env python
# coding: utf-8

# In[5]:


name = "sherouk"
print(name.upper()) 


# In[19]:


def change_cases(s):
  return str(s).upper()
 
chrars = {"sherouk"}
print("Original Characters:\n",chrars)
 
result = map(change_cases, chrars)
print(set(result))


# In[ ]:





# In[ ]:





# In[21]:


num = 10


if num > 1:

	for i in range(2, int(num/2)+1):

		if (num % i) == 0:
			print(num, "is not a prime number")
			break
	else:
		print(num, "is a prime number")
else:
	print(num, "is not a prime number")




# In[18]:





# In[ ]:




