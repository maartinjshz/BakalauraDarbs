import numpy as np
from SolveMaxiMin import SolveMaximin


function_list = [] 

# Creates a list for: 
# i. function
# ii. df/dx
# iii. df/dy
# iv.  place to  store function value later on. 

# For now, this implementation works for only 2d problems.  
f = lambda x :  0.49*x[0] + 0.12*x[1] + 7.93
df_dx = lambda x :  0.49
df_dy = lambda x :  0.12

function_list.append([ f,df_dx,df_dy ,1, np.zeros((2,))])

f = lambda x :  0.3 * x[0] - 0.08*x[1]  + 8.26
df_dx = lambda x : 0.3
df_dy = lambda x : -0.08
function_list.append([ f,df_dx,df_dy ,1, np.zeros((2,))])

f = lambda x :  0.39*x[0] +  0.33*x[1] + 8.34
df_dx = lambda x : 0.39
df_dy = lambda x : 0.33
function_list.append([ f,df_dx,df_dy ,1, np.zeros((2,))])

f = lambda x : -0.3* x[0] + 0.016* x[1] + 8.448
df_dx = lambda x : -0.3
df_dy = lambda x : 0.016
function_list.append([ f,df_dx,df_dy ,1, np.zeros((2,))])

f = lambda x : -0.191*x[0]- 0.192*x[1] + 8.469 
df_dx = lambda x : -0.191
df_dy = lambda x : -0.192
function_list.append([ f,df_dx,df_dy ,1, np.zeros((2,))])

# 
# Similarity relation can be chosen from: "Exp" / "Luk" / "Ham"
# and adding power p. 

# starting point is chosen randomly  
X_start =  np.random.uniform(-4,4,2)
X_max = SolveMaximin(function_list, "E_kSubGrad" , X_start, max_iter = 250, p = 2)
            
print(" Function F reaches its maximum at: ", X_max)