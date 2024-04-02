from MakeMolp import MolpProblem

from SolveOrder import solve_orders
from SolveEquiv import solve_equiv
from SolveTnorm import solve_tnorm

import numpy as np



A_fb = np.array([
    [2, 3, 2, 4, 1, 3],           # Coefficients for x1
    [1, 2, 4, 0, 0, 0],           # Coefficients for x2
    [3, 1, 2, 0, 0, 0],           # Coefficients for x3
    [4, 2, 3, 5, 3, 4],           # Coefficients for x4
    [0.2, 0.4, 0.3, 0.5, 0.6, 0.4], # Coefficients for waste constraint
    [2, 3, -1, 2, 1, -1],         # Coefficients for product quality constraint
    [4, 2, 3, 0, 0, 0],           # Coefficients for energy consumption
    [2, 3, 2, 0, 0, 0],           # Additional material constraint
    [1, 1, 1, 1, 1, 1]            # Total production limit
])
b_fb =  np.array([1, 1.2, 0.8, 3.5, 0.4, 1, 2, 3, 2])
C_fb = np.array([
    [2, 3, 1, 0, 0, -1],   # Coefficients for Profit (Example: 2x1 + 3x2 + x3)
    [1, 2, 1, -2, 0, 0],   # Coefficients for Resource Utilization (Example: x1 + 2x2 + x3)
    [0, 1, 3, 0, 0, 4],   # Coefficients for Waste (Example: x2 + 3x3)
    [3, 0, 1, 4, 1, 0],   # Coefficients for Product Quality (Example: x3 + 4x4)
    [-1, 0, 0, 2, 3, 0]    # Coefficients for Energy Consumption (Example: 2x4 + 3x5)
])


'''
C_fb = np.array([[-1,2],[2,1]])
A_fb = np.array([[-1,3],[1,3],[4,3],[3,1]])
b_fb= np.array([21,27,45,30])
'''

Molp_problem = MolpProblem(C_fb,A_fb,b_fb)


#rez = solve_orders(Molp_problem, method = "brute",              tol = 10**(-1) )
#rez = solve_equiv(Molp_problem,   tol = 10**(-9))
rez = solve_tnorm(Molp_problem,   tol = 10**(-9), x0= None, tnorm = "min", param = 1)

print(rez)