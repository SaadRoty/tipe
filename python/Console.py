## Bibliothèques et Fonctions
import json
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import tripy

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
from Fct_Exp import Plus_Proche_Vois
from Fct_Exp import Dist_Chemin_Graph
from Fct_Exp import Dijkstra
from Fct_Exp import Mat_Adj

#Fct_Graph
from Fct_Graph import G_Rte
from Fct_Graph import G_Rte_Carte
from Fct_Graph import G_Rte_Arr
from Fct_Graph import G_Rte_Arr_Beau
from Fct_Graph import G_Aff_Poubelle

#Algo_Dijkstra
from Algo_Dijkstra import dijkstra

#Algo_A_etoile
from Algo_A_etoile import A_etoile
from Algo_A_etoile import Chemin_final
from Algo_A_etoile import trace_Chem

#G_Rte(crd[11],"Cartographie des voies du 1er arrondissement")
#G_Rte_Arr_Beau(crd,"Cartographie des voies de Paris triées par arrondissement selon la methode Est_In")

"""with open("../assets/output/json/Trc_Paris_Tri_Meth_Est_In.json") as f:
    data = json.load(f)

with open("../assets/output/json/3L_Voisins_Dist_Trc_1erArr.json") as f:
    G = json.load(f)

start=360
end=2

for trc in data[0]:
    X=[]
    Y=[]
    for pt in trc:
        X.append(pt[0])
        Y.append(pt[1])
    plt.plot(X,Y,'g')

plt.plot(G[1][start][0],G[1][start][1],"bo") ; plt.plot(G[1][end][0],G[1][end][1],"ro")

plt.show()

for trc in data[0]:
    X=[]
    Y=[]
    for pt in trc:
        X.append(pt[0])
        Y.append(pt[1])
    plt.plot(X,Y,'g')

for trc in Chemin_final(A_etoile(start,end)[3]):
    X=[]
    Y=[]
    for pt in trc:
        X.append(pt[0])
        Y.append(pt[1])
    plt.plot(X,Y,'r')

plt.plot(G[1][start][0],G[1][start][1],"bo")
plt.plot(G[1][end][0],G[1][end][1],"r3")

plt.show()"""

trace_Chem(0,2)