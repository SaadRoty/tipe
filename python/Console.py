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

#Fct_Graph
from Fct_Graph import G_Rte
from Fct_Graph import G_Rte_Carte
from Fct_Graph import G_Rte_Arr
from Fct_Graph import G_Rte_Arr_Beau
from Fct_Graph import G_Aff_Poubelle

with open("../assets/output/json/Trc_Paris.json") as f1:
    crd = json.load(f1)

with open("../assets/output/json/Arr_Paris.json") as f2:
    Arr = json.load(f2)
print(len(crd))
print(Tri_Est_In(crd,Arr)[1])


"""G_Rte(Tri_Est_In(crd,Arr)[2],"abs")"""
G_Rte_Arr_Beau(Tri_Est_In(crd,Arr)[0],"Cartographie des voies de Paris triées par arrondissement selon la methode Est_In")

