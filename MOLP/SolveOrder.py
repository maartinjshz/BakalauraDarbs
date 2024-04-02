import numpy as np

from NumericAlg import SmRel,brute




# funkcija P_i(x,y)
def FuzzyOrder_i(x,y,it,Problem):
        z_x = np.dot(Problem.C_ub[it],x)   
        z_y =   np.dot(Problem.C_ub[it],y) 
        if (z_x < z_y):
            return 1
        else:
            return 1- np.abs(z_x-z_y)/ (Problem.Fun_norm[it] )


    # Takā nav nozīmes, kuru T-normu lieto lai konstruētu sakārtojumus,
    # Tiek lietota Lukasēviča t-norma (tikai).
def Aggregation(x, y,Problem):
        summa = 0 
        for it in range(Problem.Nr_fun):
            Eq_vert = FuzzyOrder_i(x,y,it,Problem) 
            summa = summa + Eq_vert 

        return     summa/Problem.Nr_fun

def P_x_y(y,Problem):

        Min_val= 2
        for x in Problem.vertices:
            Agregacija_val = Aggregation(x, y,Problem)
            Min_val = min(Min_val,Agregacija_val)
        return   Min_val
    

def solve_orders(Molp_problem, method = None,
                tol = 10**(-9), x0= None, constr = "GradProj" ):
    # Funkcijas, kas tālāk optimizēs problēmu pēc izvēlētās metodes.

    # 1. parametrs ir pati MOLP problēma (Klase no MakeMolp)
    # 2. algoritms, ar kuru risināt  
    # 3. Tolerance 
    # 4.  sākuma punkts (ja netiek norādīts, tiek lietots x0 no Molp_problem arg)
    # 5. 


    Meth = ["sm","brute"]

    Constr = ["GradProj","Proj","ChangeDir"]

    if x0 is None:
        x0 = Molp_problem.x0

    if method not in Meth or constr not in Constr:
        pass
    elif method  == "sm":
        # Risina ar algoritmu: 
        rez = SmRel(Molp_problem, P_x_y, x0, tol, Aggregation )
        return rez
    
    # Ar brute tiek veikta "pilna pārlase" punkta x0 apkārtnē. 
    # Tas ir paredzēts, lai vispirms tiktu veikta optimizačija ar citu algoritmu
    # Un pēc tam pārbaudīta tā atrisinājuma apkārtne. 

    # Ar šo brute algoritmu nav ieteicams meklēt atrisinājumu lielajam piemēram. 
    # Šim piemēram ir atsevišķs kods valodā C, kur ir samazināts parametru skaits un
    # Kurš šo darbu veic ātrāk 
    elif method == "brute":
         rez = brute(Molp_problem, P_x_y, x0 )
         return rez



