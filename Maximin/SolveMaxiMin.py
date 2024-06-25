import numpy as np

def weight_2(function_list,iter,  p = 1, fun = "Exp", epsilon =  10**(-6) ):
    if fun == "Exp":
        return np.exp( -  (np.abs(function_list[0][3]-function_list[1][3])  ) **(p) )
    
    if fun == "Luk":
        return max(0, 1-    (np.abs(function_list[0][3]-function_list[1][3])   )**(p) )
    
    if fun== "Ham":
        return 1/(1 +  (np.abs(function_list[0][3]-function_list[1][3])  )**(p) )
    
    if fun == "E_kSubGrad":
        if np.abs(function_list[0][3]-function_list[1][3]) <= 1/iter:
            return 1
        else:
            return 0 
        
    if fun == "ESubGrad":
        if np.abs(function_list[0][3]-function_list[1][3]) <= epsilon:
            return 1
        else:
            return 0 
    
    if fun == "SubGrad":
        if np.abs(function_list[0][3]-function_list[1][3]) ==  0:
            return 1
        else:
            return 0 
    


def fun_val(y,function_list):
    fun_val = []
    for fun in function_list:
        fun_val.append(fun[0](y))
    return min(fun_val)

def direction(y, function_list,sim_fun,p,iter,epsilon):
    AG_fun = ["Ham","Luk","Exp"]
    for idx, fun in enumerate(function_list):
        # Fun val
        fun[3]= fun[0](y)

        # df_dx
        fun[4][0] = fun[1](y)

        # df_dy
        fun[4][1] = fun[2](y)
    function_list = sorted(function_list, key=lambda x: x[3])

    v1 = 1
    v2 =  weight_2(function_list,  iter, p,sim_fun,epsilon)

    # Adds epsilon to denominator in case the gradient is zero. 
    
    if sim_fun in AG_fun:
        direction = v1* function_list[0][4]/ (np.linalg.norm(function_list[0][4])+ 10**(-12)) + v2* function_list[1][4]/ (np.linalg.norm(function_list[1][4])+ 10**(-12))
    else:
        direction = v1* function_list[0][4] + v2* function_list[1][4]
    grad = function_list[0][4]
    return  direction/(v1+v2), grad
    
def line_search(y,Dir,Grad,function_list):
        alpha = 1/np.linalg.norm(Dir)
        c1 = 10**(-4)
        ro = 0.9
        while fun_val(y  + alpha * Dir,function_list) <= fun_val(y,function_list) + c1 *alpha * np.dot( Dir,Grad )  and alpha > 10**(-9):
            alpha = alpha * ro

        return alpha


def SolveMaximin(function_list,sim_fun,y_sol,max_iter = 1000, p = 2,tol = 10**(-9),epsilon = 10**(-6)):
    iter = 1
    while True:
        # Finds direction and gradient. Gradient is needed for Backtracking Line search algorithm. 
        dir,grad =direction(y_sol,function_list,sim_fun,p,iter,epsilon)
        step_size = line_search(y_sol,dir,grad,function_list)
        # returns y if step size is too small (tolerance small) or it has reached its maximum number of iterations.
        if step_size < tol or iter >= max_iter:
            return y_sol
        y_sol += step_size * dir
        iter +=1

    
