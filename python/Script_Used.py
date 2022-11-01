#Jawg.Terrain
#polyligne
#matrice d'adjacence
import json
import numpy as np
import matplotlib.pyplot as plt
import random as rd

import pandas as pd
import geopandas as gpd
import contextily as ctx
#import geoplot
import folium
import pygeoj
import contextily as ctx
import xyzservices.providers as xyz


#Enregistrer les données sous fichier json
1)Trc_et_dist_Paris.json
    T,D=Ext_Rte("../assets/input/json/troncon_voie.json")
    Li=[]
    for i in range(len(T)):
        Li.append([T[i],D[i]])
    Ecrire_Json(Li,"../assets/output/json/Trc_et_dist_Paris.json")
2)Trc_Paris.json
    T=Ext_Rte("../assets/input/json/troncon_voie.json")[0]
    Ecrire_Json(T, "../assets/output/json/Trc_Paris.json")
3)Arr_Paris.json
    Ecrire_Json(ExtraireArrTri("../assets/input/json/arrondissements.json"),"../assets/output/json/Arr_Paris.json")
4)Pt_Extr.json
    with open("../assets/output/json/Arr_Paris.json") as f:
        data = json.load(f)
    Ecrire_Json(PtEx(data), "../assets/output/json/Pt_Extr.json")

5)Trc_Paris_Tri_Meth_Est_In.json
    with open("../assets/output/json/Trc_Paris.json") as f1:
        crd = json.load(f1)

    with open("../assets/output/json/Arr_Paris.json") as f2:
        Arr = json.load(f2)
    print(len(crd))
    print(Tri_Est_In(crd,Arr)[1])

    Ecrire_Json(Tri_Est_In(crd,Arr)[0],"../assets/output/json/Trc_Paris_Tri_Meth_Est_In.json")

6)Dist_Trc_Paris.json
    D = Ext_Rte("../assets/input/json/troncon_voie.json")[1]
    Ecrire_Json(D, "../assets/output/json/Dist_Trc_Paris.json")

7)Dist_Trc_Tri_Arr.json
    with open("../assets/output/json/Dist_Trc_Paris.json") as f:
       data = json.load(f)
    with open("../assets/output/json/Trc_Paris.json") as f1:
       crd = json.load(f1)

    with open("../assets/output/json/Arr_Paris.json") as f2:
       Arr = json.load(f2)

    print(Tri_Est_In(crd,Arr,data)[-1])
    Ecrire_Json(Tri_Est_In(crd,Arr,data)[-1],"../assets/output/json/Dist_Trc_Tri_Arr.json")

#Titres des graphiques
T1=["Cartographie des voies de Paris par tronçons","Cartographie des arrondissements de Paris",
    "Cartographie des voies de Paris triées par arrondissement selon la methode des Crd_Extr",
    "Cartographie des voies de Paris nécessitant une collecte des déchets",
    "Cartographie des voies du 1er arrondissement nécessitant une collecte des déchets"]
T2=["frontière du 1er arrondissement de Paris"]

# Creation des 3 Listes associées au voisinages des point dont l'indice corespond a celui de la liste contenant respectivement Les voisins des points, les distances avec ces voisins, les troncons associé pour aller à ce voisin

with open("../assets/output/json/Trc_Paris_Tri_Meth_Est_In.json") as f:
   data= json.load(f)

crd,NumPt=Renom_Pt_Extr_Trc(data[0])

with open("../assets/output/json/Dist_Trc_Tri_Arr.json") as f2:
   dist = json.load(f2)

with open("../assets/output/json/Trc_Paris_Tri_Meth_Est_In.json") as f3:
   TrcTri=json.load(f3)
print(Trouv_Vois(crd,NumPt,dist[0]))
print('HAHA')

print(Div_Li_Vois(Trouv_Vois(crd,NumPt,dist[0]))[0])
print('HAHA')

print(Div_Li_Vois(Trouv_Vois(crd,NumPt,dist[0]))[1])
print('HAHA')

print(TrcTri[0])
print('HAHA')

print(Trc_Associe_Vois(Div_Li_Vois(Trouv_Vois(crd,NumPt,dist[0]))[0],crd,TrcTri[0]))
print('HAHA')

8)3L_Voisins_Dist_Trc_1erArr.json
    with open("../assets/output/json/Trc_Paris_Tri_Meth_Est_In.json") as f:
       data= json.load(f)

    crd,NumPt=Renom_Pt_Extr_Trc(data[0])

    with open("../assets/output/json/Dist_Trc_Tri_Arr.json") as f2:
       dist = json.load(f2)

    with open("../assets/output/json/Trc_Paris_Tri_Meth_Est_In.json") as f3:
        TrcTri=json.load(f3)

    Li=[Div_Li_Vois(Trouv_Vois(crd,NumPt,dist[0]))[0] , Div_Li_Vois(Trouv_Vois(crd,NumPt,dist[0]))[1] , Trc_Associe_Vois(Div_Li_Vois(Trouv_Vois(crd,NumPt,dist[0]))[0],crd,TrcTri[0])]
    Ecrire_Json(Li,"../assets/output/json/3L_Voisins_Dist_Trc_1erArr.json")

#
with open("../assets/output/json/3L_Voisins_Dist_Trc_1erArr.json") as f:
   data= json.load(f)

Vois,Dist,TrcAss=data[0],data[1],data[2]