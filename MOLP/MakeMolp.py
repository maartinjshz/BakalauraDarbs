from scipy.optimize import  linprog
import numpy as np
from pypoman import compute_polytope_vertices


class MolpProblem():
    def __init__(self,C_ub,A_ub,b):
        self.C_ub = C_ub
        self.A_ub = A_ub
        self.b = b

        self.Nr_fun = C_ub.shape[0]
        self.Nr_constr = A_ub.shape[0]
        self.x0 = np.zeros((1,A_ub.shape[1]))

        self.LocalExtremum()
        self.FindVertices()


    def LocalExtremum(self):

        self.local_max = np.zeros(self.Nr_fun)
        self.local_min = np.zeros(self.Nr_fun)
        
        # Atrod lokālos ekstrēmus 
        # Takā tiek linprog piedāvā tikai minimizēt, tad maksimizējot funkciju,
        # Mērķa funkcija tiek reizināta ar -1, lai maksimizācijas problēma būtu minimizācijas.
        for i in range(self.Nr_fun):
            rez= linprog(self.C_ub[i], A_ub = self.A_ub,b_ub = self.b,method='highs')
            self.local_min[i] = rez.fun

            rez= linprog( - self.C_ub[i], A_ub = self.A_ub,b_ub = self.b,method='highs')
            self.local_max[i] = - rez.fun
            self.x0 += rez.x

        # Atrod x0, kas tiks lietots kā sākuma punkts skaitliskai optimizācijai.
        self.x0 = (self.x0 / self.Nr_fun)[0]

        # Atrod normu funckijām (max vērtība - min vērtība), lai 
        # Mērķa funkcijas būtu robežās [0,1]. 
        self.Fun_norm = self.local_max - self.local_min


    def FindVertices(self):
        # Šajā funkcijā atrod kopas D virsotnes

        # Takā matricā A neietilpst nosacījumi, ka xi >= 0 
        # matrica A tiek papildināta, lai iekļautu šos nosacījumus
        # Un pēc tam tiek atrastas kopas D virsotnes. 
        # 
        b_add = np.zeros(self.A_ub.shape[1])
        A_add = []
        for i in range(self.A_ub.shape[1]):
                    x_vec = np.zeros(self.A_ub.shape[1])
                    x_vec[i] = -1
                    A_add.append( x_vec)

        # Mainās matrica A, vektors b un nosacījumu skaits.
        self.A_ub = np.concatenate((self.A_ub,A_add))
        self.b =  np.concatenate((self.b,b_add))
        self.Nr_constr = self.A_ub.shape[0]

        # Funkcijas, lai atrastu kopas D virsotnes. 
        self.vertices = compute_polytope_vertices(self.A_ub ,self.b)


    

