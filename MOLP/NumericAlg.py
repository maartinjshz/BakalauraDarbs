import numpy as np
from qpsolvers import solve_ls
import scipy.sparse as sp

def GradProj( Molp_problem,A_q,Directions):
    P_k = np.dot(np.dot(A_q.T,  np.linalg.inv(np.dot(A_q, A_q.T))), A_q)
    P_k =   + (np.eye(P_k.shape[0]) - P_k ) 
    d = np.dot(P_k, Directions)

# Ja gradients ir 0 tiek aizstāts ar ja tā norma ir pietiekami maza
    if np.linalg.norm(d) < 10**(-16):
        lambda_k = -  np.dot(np.dot(np.linalg.inv( np.dot(A_q, A_q.T)), A_q), Directions)
        if np.amin(lambda_k) >=0:
            print(lambda_k,d)
            return [d, True]
        else:
            Id_of_MostNeg = np.argmin(lambda_k)
            GradProj(Molp_problem,np.delete(A_q, Id_of_MostNeg,axis=0),Directions)
    else:
        return [d,False]

def LineSearch(Molp_problem, y, Direction,Gradient,Fun,tol):
    alpha =   1/(np.linalg.norm(Direction) )
    c1 =  10**(-4)
    ro = 0.8
    Fun_val = Fun(y,Molp_problem)
    while Fun( y  + alpha * Direction,Molp_problem,)  <= Fun_val + c1 *alpha * np.dot( Direction,Gradient)  and alpha > tol :
            alpha = alpha * ro
    return alpha  

def LineSearch_FindAl(Molp_problem, y, Direction,Gradient,Fun,tol):

    alpha =   1/(np.linalg.norm(Direction)  )
    c1 =  10**(-4)
    ro = 0.8
    for it in range(Molp_problem.Nr_constr):
        while alpha > tol:
            if  np.dot(Molp_problem.A_ub[it],y + alpha*Direction) - Molp_problem.b[it] > 0:
                    alpha = alpha * ro
            else:
                break
    
    Fun_val = Fun(y,Molp_problem)
    while Fun( y  + alpha * Direction,Molp_problem,)  <= Fun_val + c1 *alpha * np.dot( Direction,Gradient)  and alpha > tol :
            alpha = alpha * ro

    return alpha 


def FindDirection(Molp_problem,y,Aggregation):
    Val_and_grad = []
    # Atrod funckijas vērtību un gradientu

    for x in  Molp_problem.vertices:
            gradient_i = np.zeros((Molp_problem.A_ub.shape[1],))
            P_i_x_y_value = Aggregation(x, y,Molp_problem)
            for it in range(Molp_problem.Nr_fun):
                z_x = np.dot(Molp_problem.C_ub[it],x)   
                z_y =   np.dot(Molp_problem.C_ub[it],y) 

                if z_x > z_y:
                    gradient_i+=  Molp_problem.C_ub[it]   /( Molp_problem.Fun_norm[it])
                elif z_x == z_y :
                    gradient_i+= Molp_problem.C_ub[it]/2  /(Molp_problem.Fun_norm[it])/2
# P_i gradientu normē
            if np.linalg.norm(np.linalg.norm(gradient_i)) != 0 :
                gradient_i = gradient_i/(np.linalg.norm(gradient_i))
            Val_and_grad.append({'FunVal': P_i_x_y_value, 'FunGrad': gradient_i})

# Pēc tam sarindo augošā secībā pēc funckiajs vērtības 
    Sorted_functions = sorted(Val_and_grad, key=lambda x: x['FunVal'])
# Aprēķina svaru v1 un v2
    v1 = 1
    v2 =  np.exp( - np.abs(Sorted_functions[0]['FunVal']-Sorted_functions[1]['FunVal'])**(2)  ) 
    Direction =   ((v1*Sorted_functions[0]['FunGrad']+v2*Sorted_functions[1]['FunGrad'] ))/(v1+v2)   
    Gradient = Sorted_functions[0]['FunGrad']

    # Un atgriež virzienu g_k un gradientu 
    return [Direction, Gradient]

def SmRel(Molp_problem, Fun ,x0 , tol = 10**(-9), Aggregation = None):
    
    isClose = False
    toEnd = False
    while True:

        # Atrod virzienu
        Direction,Gradient = FindDirection(Molp_problem,x0,Aggregation)

        # Atrdod soli
        if isClose:
            # Atrod matricu A_q 
            A_q= []
            for it in range(Molp_problem.Nr_constr):
                if  (np.dot(Molp_problem.A_ub[it],x0) - Molp_problem.b[it])**(2) < tol:
                    A_q.append(Molp_problem.A_ub[it])
            A_q = np.array(A_q)

# Var gadīties, ka matrica A_q ir tukša. Ja tā, tad netiek mainīts virziens.
            if A_q.shape[0] != 0:
                # TODO pielikt if/else lai Dir vietā būtu Grad 
                Direction,toEnd = GradProj( Molp_problem,A_q,Direction)
                step = LineSearch_FindAl(Molp_problem, x0, Direction,Gradient,Fun,tol)
            # Atrod soļa garumu
            else:
                step = LineSearch(Molp_problem, x0, Direction,Gradient,Fun,tol)

        else:
            step = LineSearch(Molp_problem, x0, Direction,Gradient,Fun,tol)
        
        if step < tol or toEnd:
            print("Atrisinājums saniegts punktā: ", x0)
            return [x0, Fun(x0,Molp_problem)]
        
        # veic iteraciju
        x0 = x0 + step * Direction

        # Projekcija
        for it in range(Molp_problem.Nr_constr):       
            if  np.dot(Molp_problem.A_ub[it],x0) - Molp_problem.b[it] > 0: 
                x0 = solve_ls(np.identity(x0.shape[0]), x0,Molp_problem.A_ub, Molp_problem.b, solver="daqp")
                isClose = True

# 
def brute(Molp_problem, Fun ,x0,tol = 10**(-8) ):

    fun_max = Fun(x0,Molp_problem)
    h = 1
    while True:
        
        # uztaisa augšējo un apakšējo kastes punktu
        x_lower = x0 - h
        x_upper = x0 + h

# Nav jēga apskatīt vērtības mazākas nekā 0, jo tās ir ārpus kopas. 
        x_lower = np.where(x_lower > 0, x_lower, 0)

        x_h = x0*0
        print(" ------------------------------------------------------------ ")
        print("Solis ir: " , h)
        print("Šajā iterācijā apaksā: ", x_lower, " un augša ", x_upper )
        print("un šajā iterācijā x_max: ", x0, " un fun_max: ", fun_max)
        print(" ------------------------------------------------------------ ")
        while True:

            if x_h[0] + x_lower[0]>= x_upper[0]:
                break
            else:
                for i,xi in enumerate(reversed(x_h)):

                    if  x_h[i]+x_lower[i] >= x_upper[i]:
                        x_h[i-1] += 2*h/50
                        x_h[i] = 0
                    elif (i == x0.shape[0]-1):

                        x_h[i] = x_h[i] + 2*h/50

                    fun_val = Fun(x_lower + x_h,Molp_problem)
                    if fun_val > fun_max:
                        fun_max = fun_val
                        x0 = x_lower + x_h
        h = h /10
        if h<= tol:
            break

    
    