## Bibliothèques et Fonctions
import json
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import tripy
import time
from collections import Counter

#Fct_Json
from Fct_Json import Ext_Rte
from Fct_Json import Ext_Arr
from Fct_Json import Ext_Arr_Tri
from Fct_Json import Ecrire_Json

#Fct_Exp
from Fct_Exp import Crd_Extr
from Fct_Exp import Tri_Rte_Arr_PtEx
from Fct_Exp import Trig_Arr
from Fct_Exp import Est_In
from Fct_Exp import Tri_Est_In
from Fct_Exp import Renom_Pt_Extr_Trc
from Fct_Exp import Trouv_Vois
from Fct_Exp import Div_Li_Vois
from Fct_Exp import Trc_Associe_Vois

#Fct_Graph
from Fct_Graph import G_Rte
from Fct_Graph import G_Rte_Carte
from Fct_Graph import G_Rte_Arr
from Fct_Graph import G_Rte_Arr_Beau
from Fct_Graph import G_Aff_Poubelle

#Algo_Dijkstra
from Algo_Dijkstra import Plus_Proche_Vois
from Algo_Dijkstra import Dist_Chemin_Graph
from Algo_Dijkstra import Dijkstra
from Algo_Dijkstra import Mat_Adj
from Algo_Dijkstra import dijkstra

#Algo_A_etoile
from Algo_A_etoile import A_etoile
from Algo_A_etoile import Chemin_final
from Algo_A_etoile import trace_Chem
from Algo_A_etoile import TestChmeSeul
from Algo_A_etoile import PtNonConnectes
from Algo_A_etoile import Global_A_etoile
from Algo_A_etoile import Global_Trace_Chem

#Algo_Gen
from Algo_Gen import Init_Li
from Algo_Gen import Init_Pop_Random
from Algo_Gen import Fitness_Exact
from Algo_Gen import Fitness_Approximate
from Algo_Gen import Fitness_Exact_For_Global_Gen
from Algo_Gen import Init_Weight_Pop_Exact
from Algo_Gen import Init_Weight_Pop_Approximate
from Algo_Gen import Tri_Pop
from Algo_Gen import Crussover_PMX
from Algo_Gen import Merge_Pop_Offspring_Tri
from Algo_Gen import Li_Prop_Rank
from Algo_Gen import Roulette_Parents_Choice
from Algo_Gen import Insertion_Mutation_Operator
from Algo_Gen import Swap_Mutation_Operator
from Algo_Gen import Reverse_Mutation_Operator
from Algo_Gen import New_Pop
from Algo_Gen import Mutation_Generation
from Algo_Gen import Create_Parents
from Algo_Gen import Create_i_j
from Algo_Gen import Global_Genetic_Algo

from Algo_Gen import Fitness_Exact_For_Global_Gen2
from Algo_Gen import Fitness_Exact_For_Global_Gen3
from Algo_Gen import Fitness_Exact_For_Global_Gen4
from Algo_Gen import Init_Weight_Pop_Exact_For_Global_Gen2
'''

n=7
nPop=1000
coef=10

Li=Init_Li(n)
Pop=Init_Pop_Random(Li,nPop)
print(Pop[nPop-10:])

start=time.time()
W_Pop=Init_Weight_Pop_Approximate(Pop,n,coef)
end=time.time()
print(W_Pop[nPop-10:])
print('temps','=',end-start)

start=time.time()
W_Pop=Init_Weight_Pop_Exact(Pop,n)
end=time.time()
print(W_Pop[nPop-10:])
print('temps','=',end-start)

'''

"""W_Pop=list(range(nPop-1,-1,-1))
print(W_Pop[nPop-10:])

Pop,W_Pop=Tri_Pop(Pop,W_Pop)
print(Pop[nPop-10:])
print(W_Pop[nPop-10:])

New_Pop(Pop,W_Pop,nPop)
print('len', len(Pop))
print(Pop[len(Pop)-10:])
print(W_Pop[len(Pop)-10:])"""

n = 20
nPop = 1000
nGen = 250
Li = Init_Li(n)

dist=Fitness_Exact(Li,n)
print(dist)
Global_Trace_Chem(Li,"1er",str(dist))

start=time.time()
Chem,DIST=Global_Genetic_Algo(Li,n,nPop,nGen)
end=time.time()
print("time2 =",end-start)
Global_Trace_Chem(Chem,"2eme",str(DIST))

nPop=5000
nGen=50
start=time.time()
Chem,DIST=Global_Genetic_Algo(Li,n,nPop,nGen)
end=time.time()
print("time3 =",end-start)
Global_Trace_Chem(Chem,"3eme",str(DIST))

plt.show()




#Global_Trace_Chem([455, 341, 416, 330, 304, 256, 36, 453, 389, 128, 234, 226, 317, 101, 436, 20, 336, 242, 283, 177],'a','b')
#plt.show()

