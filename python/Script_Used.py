#Jawg.Terrain
#polyligne
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
    Ecrire_Json(PtEx(data),"../assets/output/json/Pt_Extr.json")

#Titres des graphiques
T1=["Cartographie des voies de Paris par tronçons","Cartographie des arrondissements de Paris","Cartographie des voies de Paris triées par arrondissement selon la methode des Crd_Extr","Cartographie des voies de Paris nécessitant une collecte des déchets","Cartographie des voies du 1er arrondissement nécessitant une collecte des déchets"]
T2=["frontière du 1er arrondissement de Paris"]

"""
poly=[(0,2),(1,1),(3,1),(1,-1),(0,-2),(-1,-1),(-1,1)]
triangles= tripy.earclip(poly)

print(triangles)

A=[]
for i in range(len(triangles)) :
    A.append([[triangles[i][0][0],triangles[i][0][1]],[triangles[i][1][0],triangles[i][1][1]],[triangles[i][2][0],triangles[i][2][1]],[triangles[i][0][0],triangles[i][0][1]]])

print(A)

G_Rte(A,"a")

with open("../assets/output/json/Arr_Paris.json") as f:
    data = json.load(f)
triangles= tripy.earclip(data[11])

print(triangles)

A=[]
for i in range(len(triangles)) :
    A.append([[triangles[i][0][0],triangles[i][0][1]],[triangles[i][1][0],triangles[i][1][1]],[triangles[i][2][0],triangles[i][2][1]],[triangles[i][0][0],triangles[i][0][1]]])

print(A)
G_Rte(A,"a")
"""
if (x2 < x and x < x1) or (y2 < y if y1 < y else y2 > y):
    continue
if y1 == y or y2 == y:
    continue

if x1 > x and x2 > x:
    cp += 1
    continue

a = (y2 - y1) / (x2 - x1)
b = y1 - a * x1
Y = a * x + b

if (Y < y if a < 0 else Y > y):
    continue

cp += 1