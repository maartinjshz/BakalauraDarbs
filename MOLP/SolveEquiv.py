import numpy as np
from scipy.optimize import  linprog,minimize


def F_ekviv_Luk(x,Molp_problem):
    for it in range(Molp_problem.Nr_constr):
        if np.dot( x, Molp_problem.A_ub[it]) - Molp_problem.b[it] >0:
            return 0
    Ekviv = 0  
    for it in range(Molp_problem.Nr_fun):
        Ekviv += 1 - (Molp_problem.local_max[it] - np.dot(  Molp_problem.C_ub[it], x  ))/(Molp_problem.Fun_norm[it])

    return -Ekviv / Molp_problem.Nr_fun

def solve_equiv(Molp_problem,   tol = 10**(-9), x0= None):
    

    # Solving the same problem using the observation, that the problem can be reduced to just 
    # a sum of metrics
    Obj_fun = np.zeros(Molp_problem.A_ub.shape[1])

    for it in range(Molp_problem.Nr_fun):
        Obj_fun +=  - Molp_problem.C_ub[it]/ ( Molp_problem.Fun_norm[it] )
    
    Result = linprog(  Obj_fun, A_ub = Molp_problem.A_ub,b_ub = Molp_problem.b,method='revised simplex')
    
    print("Atrisinājums pārrakstot problēmu ar LP problēmu : ", Result.x)

    return Result.x
