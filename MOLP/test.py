from MakeMolp import MolpProblem

from SolveOrder import solve_orders

import numpy as np


C_fb = np.array([[-1,2],[2,1]])
A_fb = np.array([[-1,3],[1,3],[4,3],[3,1]])
b_fb= np.array([21,27,45,30])

Molp_problem = MolpProblem(C_fb,A_fb,b_fb)



rez = solve_orders(Molp_problem, method = "sm",
                tol = 10**(-9),  constr = "GradProj" )


print(rez)