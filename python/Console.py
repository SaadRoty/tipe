## Bibliothèques et Fonctions
import json
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import tripy
import time

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
from Algo_Gen import Fitness
from Algo_Gen import Crussover_PMX

'''P1=[3,4,8,2,7,1,6,5]
P2=[4,2,5,1,6,8,3,7]
i=3
j=5
n=len(P1)

print(Crussover_PMX(P1,P2,n,i,j))'''


chrom=[1,11,111,2,22,222,3,33,333,4,44,5,55,6,66,7,77,8,88,9,99,10,20,40,50,60,70,80,90,100,110,120,130,140]

Global_Trace_Chem(chrom)
start=time.time()
Global_A_etoile(chrom)
mid=time.time()
Fitness(chrom,6)
end=time.time()

print(mid-start,end-mid)