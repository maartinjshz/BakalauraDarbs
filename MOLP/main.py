from MakeMolp import MolpProblem

from SolveOrder import solve_orders
from SolveEquiv import solve_equiv
from SolveTnorm import solve_tnorm

import numpy as np


# Liels piemērs 
A_fb = np.array([
    [2, 3, 2, 4, 1, 3],       
    [1, 2, 4, 0, 0, 0],          
    [3, 1, 2, 0, 0, 0],         
    [4, 2, 3, 5, 3, 4],    
    [0.2, 0.4, 0.3, 0.5, 0.6, 0.4], 
    [2, 3, -1, 2, 1, -1],  
    [4, 2, 3, 0, 0, 0],        
    [2, 3, 2, 0, 0, 0],           
    [1, 1, 1, 1, 1, 1]           
])
b_fb =  np.array([1, 1.2, 0.8, 3.5, 0.4, 1, 2, 3, 2])
C_fb = np.array([
    [2, 3, 1, 0, 0, -1], 
    [1, 2, 1, -2, 0, 0], 
    [0, 1, 3, 0, 0, 4],   
    [3, 0, 1, 4, 1, 0],  
    [-1, 0, 0, 2, 3, 0]   
])


## Zimmermana piemērs
C_fb = np.array([
    [-1,2],       
    [2,1],          
         
])
b_fb =  np.array([21,27,45,30])
A_fb = np.array([
    [-1,3], 
    [1,3], 
    [4,3],   
    [3,1],    
])




Molp_problem = MolpProblem(C_fb,A_fb,b_fb)




rez = solve_equiv(Molp_problem,   tol = 10**(-9))
print("Risināt problēmu ar Ekvivalencēm: ", rez)

rez = solve_tnorm(Molp_problem,   tol = 10**(-15), x0= None, tnorm = "luk", param = 1)
print("Risināt problēmu ar Tnormam: ", rez)

rez = solve_orders(Molp_problem, method = "sm",tol = 10**(-9) )
print("Risināt problēmu ar Sakārtojumiem: ", rez[0])