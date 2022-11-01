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

#Fct_Graph
from Fct_Graph import G_Rte
from Fct_Graph import G_Rte_Carte
from Fct_Graph import G_Rte_Arr
from Fct_Graph import G_Rte_Arr_Beau
from Fct_Graph import G_Aff_Poubelle



#G_Rte(crd[11],"Cartographie des voies du 1er arrondissement")
#G_Rte_Arr_Beau(crd,"Cartographie des voies de Paris triées par arrondissement selon la methode Est_In")

#print(crd[0])
#print(Renom_Pt_Extr_Trc(crd[0]))
#print(len(Renom_Pt_Extr_Trc(crd[0])))

with open("../assets/output/json/3L_Voisins_Dist_Trc_1erArr.json") as f:
   data= json.load(f)

Vois,Dist,TrcAss=data[0],data[1],data[2]

print(Vois)
print('haha')
print(Dist)
print("haha")
print(TrcAss)