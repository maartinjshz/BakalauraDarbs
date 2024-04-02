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
    x0  = Molp_problem.x0
    # Optimizes the t-norm using Nelder-Mead algorithm.  AS this is a minimization algorithm, 
    # All the t-norms return Val * -1, so that maximization problem would become a minimization problem. 
    Result_NM = (minimize( F_ekviv_Luk, x0, args=(Molp_problem),method='Nelder-Mead',
        options={'xatol': tol , 'maxiter': 1000} ))

    # Solving the same problem using the observation, that the problem can be reduced to just 
    # a sum of metrics
    Obj_fun = np.zeros(Molp_problem.A_ub.shape[1])

    for it in range(Molp_problem.Nr_fun):
        Obj_fun +=  - Molp_problem.C_ub[it]/ ( Molp_problem.Fun_norm[it] )
    
    Result = linprog(  Obj_fun, A_ub = Molp_problem.A_ub,b_ub = Molp_problem.b,method='revised simplex')
    

    print("Atrisinājums lietojor Nelder-Mead algoritmu ", Result_NM.x)

    print("Atrisinājums pārrakstot problēmu ar LP problēmu : ", Result.x)

    print("Distance starp atrisinājumiem: ", np.linalg.norm( Result_NM.x - Result.x))

    return Result.x
