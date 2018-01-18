
# coding: utf-8

# In[1]:

# get_ipython().magic('matplotlib inline')

import math
import numpy as np
import matplotlib.pyplot as plt


# In[2]:

# define a FUNCTION to compute the analytical solution
def analytical(g,m,c,t):
    return (g*m/c)*(1-math.exp((-1)*(c/m*t)))


# In[3]:

# define a FUNCTION to compute the numerical solution
def numerical(g,m,c,t,ti,vi):
    return vi+(g-c/m*vi)*(t-ti)


# In[5]:

# define our constants (apply to all cases)
g = 9.81
m = 68.1
c = 12.5
t_start = 0
t_end = 200


# In[12]:

t_step = 2

# compute a LIST of time values at which we will compute solutions
t_tick_10 = [t for t in range(t_start, t_end, t_step)]
print(t_tick_10)


# In[13]:

# compute an anlytical solution using a list generator
a_sol_10 = [analytical(g,m,c,t) for t in t_tick_10]
print(a_sol_10)


# In[14]:

# just a label for the plot legend
a_label_10 = 'a ' + str(t_step)

# create the plot
plt.plot(t_tick_10, a_sol_10, color='blue', linewidth=2, label=a_label_10)
plt.legend(loc=4)


# In[17]:

snaps = int((t_end - t_start) / t_step)
n_sol_10 = np.zeros(snaps)

#compute the numerical solution using a for loop
for i in range(snaps):
    if i == 0:
        ti = t_tick_10[0]
        vi = 0
    else:
        ti = t_tick_10[i-1]
        vi = n_sol_10[i-1]
    
    t = t_tick_10[i]   
    n_sol_10[i] = numerical(g,m,c,t,ti,vi)
    

n_label_10 = 'n ' + str(t_step)


# In[18]:

print(n_label_10)


# In[19]:

# create a plot with all solutions

plt.plot(t_tick_10, a_sol_10, color='blue', linewidth=2, label=a_label_10)
plt.plot(t_tick_10, n_sol_10, color='red', linewidth=2, label=n_label_10)
plt.legend(loc=4)


# In[ ]:



