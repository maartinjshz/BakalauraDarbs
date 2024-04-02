import numpy as np
from scipy.optimize import  minimize

def CheckConstraints(x,Molp_problem):
    for it in range(Molp_problem.Nr_constr):
        if np.dot(Molp_problem.A_ub[it], x) > Molp_problem.b[it]:
            return 0
        
    return 1

# Functions for all the t-norms
def T_min(x,Molp_problem):
    if CheckConstraints(x,Molp_problem) == 0:
        return 0 

    T_min =  mu_i(x,0,Molp_problem)

    for i in range(1,Molp_problem.Nr_fun):
        T_min = min( T_min , mu_i(x,i,Molp_problem)  )

    return - T_min

def T_product(x,Molp_problem):
    if CheckConstraints(x,Molp_problem) == 0:
        return 0
    
    T_prod = mu_i(x,0,Molp_problem) 

    for i in range(1, Molp_problem.Nr_fun):
        T_prod = mu_i(x,i,Molp_problem) * T_prod
    return - T_prod

def T_Lukasiewicz(x,Molp_problem):
    if CheckConstraints(x,Molp_problem) == 0:
        return 0
    
    T_Lksc = max(mu_i(x,0,Molp_problem)+ mu_i(x,1,Molp_problem)-1,0)

    for i in range(2,Molp_problem.Nr_fun):
        T_Lksc = max(mu_i(x,i,Molp_problem)+  T_Lksc-1,0)
    return -  T_Lksc

def T_Hamacher(x,Molp_problem,p = 1):
    if CheckConstraints(x,Molp_problem) == 0:
        return 0
    
    T_Ham = (mu_i(x,0,Molp_problem)*mu_i(x,1,Molp_problem))/(p + (1-p)*(mu_i(x,0,Molp_problem) + mu_i(x,1,Molp_problem) - mu_i(x,0,Molp_problem)*mu_i(x,1,Molp_problem)) )

    for i in range(2, Molp_problem.Nr_fun):
        T_Ham=(mu_i(x,i,Molp_problem)*T_Ham)/(p + (1-p)*(mu_i(x,i,Molp_problem) + T_Ham- mu_i(x,i,Molp_problem)*T_Ham) )

    return - T_Ham

def mu_i(x,i,Molp_problem):
    return ( np.dot(x, Molp_problem.C_ub[i])- Molp_problem.local_min[i])/(Molp_problem.Fun_norm[i])



def solve_tnorm(Molp_problem,   tol = 10**(-9), x0= None, tnorm = "min", param = 1):

    if x0 is None:
        x0 = Molp_problem.x0

    tnorm_functions = [{"tnorm": "min","function": T_min},
                    {"tnorm": "luk", "function": T_Lukasiewicz },
                    {"tnorm": "prod", "function": T_product },
                    {"tnorm": "ham", "function": T_Hamacher }]
    
    for Tnorm in tnorm_functions:
        if Tnorm["tnorm"] == tnorm:
            Fun = Tnorm["function"]

    if tnorm in ["t_hamacher"]:
        args = (Molp_problem,param)
    else:
        args = (Molp_problem)

    Result_NM = (minimize( Fun, x0, args=args,method='Nelder-Mead',
        options={'xatol': tol , 'maxiter': 1000} ))

    return Result_NM.x
    
