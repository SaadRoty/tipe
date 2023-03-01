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

gestion des données : classe : DataFrame from panda

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

# Creation des 3 Listes associées au voisinages des point dont l'indice correspond a celui de la liste contenant
# respectivement Les voisins des points, les distances avec ces voisins, les troncons associé pour aller à ce voisin

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

8)3L_Voisins_Dist_Trc_1erArr.json premiere version
    with open("../assets/output/json/Trc_Paris_Tri_Meth_Est_In.json") as f:
       data= json.load(f)

    crd,NumPt=Renom_Pt_Extr_Trc(data[0])

    with open("../assets/output/json/Dist_Trc_Tri_Arr.json") as f2:
       dist = json.load(f2)

    with open("../assets/output/json/Trc_Paris_Tri_Meth_Est_In.json") as f3:
        TrcTri=json.load(f3)

    Li=[Div_Li_Vois(Trouv_Vois(crd,NumPt,dist[0])),
        Trc_Associe_Vois(Div_Li_Vois(Trouv_Vois(crd,NumPt,dist[0]))[0],crd,TrcTri[0]), crd,NumPt]
    Ecrire_Json(Li,"../assets/output/json/3L_Voisins_Dist_Trc_1erArr.json")

#
with open("../assets/output/json/3L_Voisins_Dist_Trc_1erArr.json") as f:
   data= json.load(f)

Vois,Dist,TrcAss=data[0],data[1],data[2]

9)3L_Voisins_Dist_Trc_1erArr.json avec equivalence numéro--> crd
with open("../assets/output/json/Trc_Paris_Tri_Meth_Est_In.json") as f:
    data = json.load(f)

crd, NumPt, EquivalentCrd = Renom_Pt_Extr_Trc(data[0])

with open("../assets/output/json/Dist_Trc_Tri_Arr.json") as f2:
    dist = json.load(f2)

with open("../assets/output/json/Trc_Paris_Tri_Meth_Est_In.json") as f3:
    TrcTri = json.load(f3)

Li = [Div_Li_Vois(Trouv_Vois(crd, NumPt, dist[0]))[0], EquivalentCrd, Div_Li_Vois(Trouv_Vois(crd, NumPt, dist[0]))[1],
      Trc_Associe_Vois(Div_Li_Vois(Trouv_Vois(crd, NumPt, dist[0]))[0], crd, TrcTri[0])]
Ecrire_Json(Li, "../assets/output/json/3L_Voisins_Dist_Trc_1erArr.json")

10) PtNonConnectés() -->les pt 30 et 31 de 3L_Voisins_Dist_Trc_1erArr ne sont pas connéctés avec le reste de l arrondissement on décide dont de les retirer

on cree pour cela le dossier Arr1_V_Eq_D_Trc --> 465 pt différents maintenant

with open("../assets/output/json/Trc_Paris_Tri_Meth_Est_In.json") as f:
    data = json.load(f)

crd, NumPt, EquivalentCrd = Renom_Pt_Extr_Trc(data[0])

with open("../assets/output/json/Dist_Trc_Tri_Arr.json") as f2:
    dist = json.load(f2)

with open("../assets/output/json/Trc_Paris_Tri_Meth_Est_In.json") as f3:
    TrcTri = json.load(f3)

Li = [Div_Li_Vois(Trouv_Vois(crd, NumPt, dist[0]))[0], EquivalentCrd, Div_Li_Vois(Trouv_Vois(crd, NumPt, dist[0]))[1],
      Trc_Associe_Vois(Div_Li_Vois(Trouv_Vois(crd, NumPt, dist[0]))[0], crd, TrcTri[0])]

for i in range(4):
    print(Li[i].pop(30))
    print(Li[i].pop(30))

Ecrire_Json(Li, "../assets/output/json/Arr1_V_Eq_D_Trc.json")


11) test rapidité

n=10**8
start=time.time()
L=[0]*n
mid=time.time()
P=[0 for i in range(n)]
end=time.time()
print(mid-start,end-mid)
"0.20249414443969727 ; 3.4870293140411377"

12) test rapidité 2

chrom=[1,11,111,2,22,222,3,33,333,4,44,5,55,6,66,7,77,8,88,9,99,10,20,40,50,60,70,80,90,100,110,120,130,140]

Global_Trace_Chem(chrom)
start=time.time()
Global_A_etoile(chrom)
mid=time.time()
Fitness(chrom,6)
end=time.time()

print(mid-start,end-mid)
"0.7406120300292969 ; 0.07483649253845215"