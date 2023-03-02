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

13) au total il y a 467 pt dans le 1er arr

14)test Init_Tri_Pop()

A=['c','d','b','a']
B=[3,4,2,1]
print("test",Tri_Pop(A,B))

'test (['a', 'b', 'c', 'd'], [1, 2, 3, 4])'

15)test Merge_Pop_Offspring_Tri

A=['a','c','d','g']
B=['b','e','f']

W_A=[1,3,4,7]
W_B=[2,5,6]

print("test",Merge_Pop_Offspring_Tri(A,W_A,B,W_B))

'test (['a', 'b', 'c', 'd', 'e', 'f', 'g'], [1, 2, 3, 4, 5, 6, 7])'

16)test Li_Prop_Rank
L=Li_Prop_Rank(10)
print(L)

a=0
for elmnt in L:
    a+=elmnt
print(a)
'[0.18181818181818182, 0.16363636363636364, 0.14545454545454545, 0.12727272727272726, 0.10909090909090909, ' \
'0.09090909090909091, 0.07272727272727272, 0.05454545454545454, 0.03636363636363636, 0.01818181818181818]'

'1.0'

17) test Roulette_Parents_Choice

n=5000

Pop=[[0,1,2,3,4],[1,0,2,3,4],[2,0,1,3,4],[3,0,1,2,4]]
L=Li_Prop_Rank(4)
print(L)

a=0
for elmnt in L:
    a+=elmnt
print(a)

Nb=[0,0,0,0]

for i in range (n):
    b=Roulette_Parents_Choice(Pop,L)
    c=Pop.index(b)
    Nb[c]=Nb[c]+1
for elmnt in Nb:
    elmnt=elmnt/n

print(Nb)

'''[0.4, 0.3, 0.2, 0.1]
0.9999999999999999
[1955, 1477, 1014, 554]'''

18) test Insertion_Mutation_Operator
for i in range(10):
    chrom = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    Insertion_Mutation_Operator(chrom,10)
    print(chrom)

'''[0, 1, 2, 3, 8, 4, 5, 6, 7, 9]
[0, 1, 2, 3, 7, 4, 5, 6, 8, 9]
[2, 0, 1, 3, 4, 5, 6, 7, 8, 9]
[0, 9, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 5, 6, 7, 4, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 2, 3, 4, 5, 6, 7, 1, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 8, 9, 7]
[0, 1, 2, 3, 5, 4, 6, 7, 8, 9]
[9, 0, 1, 2, 3, 4, 5, 6, 7, 8]'''

19) test Swap_Mutation_Operator
for i in range(10):
    chrom = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    Swap_Mutation_Operator(chrom,10)
    print(chrom)

'''[0, 5, 2, 3, 4, 1, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 6, 5, 7, 8, 9]
[0, 1, 9, 3, 4, 5, 6, 7, 8, 2]
[8, 1, 2, 3, 4, 5, 6, 7, 0, 9]
[0, 1, 2, 3, 6, 5, 4, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 5, 4, 6, 7, 8, 9]
[0, 1, 2, 3, 8, 5, 6, 7, 4, 9]
[0, 1, 2, 5, 4, 3, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 8, 7, 6, 9]'''

20) test Reverse_Mutation_Operator
for i in range(10):
    chrom = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    Reverse_Mutation_Operator(chrom,10)
    print(chrom)

'''[0, 1, 8, 7, 6, 5, 4, 3, 2, 9]
[0, 1, 2, 3, 4, 5, 6, 8, 7, 9]
[3, 2, 1, 0, 4, 5, 6, 7, 8, 9]
[0, 1, 4, 3, 2, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 3, 2, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 4, 3, 2, 1, 5, 6, 7, 8, 9]'''

21) test NewPop
n=10
nPop=1000
Li=Init_Li(n)
Pop=Init_Pop_Random(Li,nPop)
print(Pop[nPop-10:])

#W_Pop=Init_Weight_Pop_Exact(Pop,n)

W_Pop=list(range(nPop-1,-1,-1))
print(W_Pop[nPop-10:])

Pop,W_Pop=Tri_Pop(Pop,W_Pop)
print(Pop[nPop-10:])
print(W_Pop[nPop-10:])

New_Pop(Pop,W_Pop,nPop)
print('len', len(Pop))
print(Pop[len(Pop)-10:])
print(W_Pop[len(Pop)-10:])

'''
[[466, 454, 109, 149, 45, 336, 309, 462, 162, 18], [109, 462, 18, 309, 466, 336, 45, 454, 162, 149], [149, 466, 109, 454, 45, 462, 162, 18, 336, 309], 
[109, 162, 149, 45, 309, 18, 462, 454, 336, 466], [45, 454, 336, 162, 309, 18, 466, 109, 149, 462], [454, 462, 45, 466, 149, 18, 162, 336, 309, 109], 
[149, 45, 162, 466, 18, 336, 462, 454, 309, 109], [309, 466, 454, 336, 462, 162, 18, 45, 149, 109], [336, 466, 109, 149, 45, 18, 462, 454, 162, 309], 
[336, 18, 162, 109, 454, 309, 466, 462, 149, 45]]

[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

[[466, 462, 18, 162, 454, 45, 309, 149, 336, 109], [454, 466, 149, 109, 162, 45, 18, 309, 462, 336], [309, 18, 149, 454, 162, 462, 45, 109, 466, 336], 
[462, 162, 466, 336, 18, 309, 109, 454, 149, 45], [462, 454, 109, 309, 45, 336, 18, 162, 466, 149], [45, 18, 466, 309, 336, 149, 454, 162, 109, 462], 
[336, 18, 149, 454, 466, 45, 309, 162, 109, 462], [18, 149, 45, 162, 309, 336, 109, 454, 466, 462], [149, 162, 336, 454, 45, 18, 109, 462, 309, 466], 
[162, 454, 462, 18, 45, 466, 109, 336, 309, 149]]

[990, 991, 992, 993, 994, 995, 996, 997, 998, 999]

1000
970
len 970

[[454, 462, 336, 149, 18, 45, 309, 162, 109, 466], [18, 454, 466, 462, 109, 336, 162, 149, 309, 45], [309, 45, 462, 466, 162, 149, 336, 109, 18, 454], 
[162, 109, 45, 462, 309, 18, 149, 454, 466, 336], [309, 162, 109, 336, 45, 466, 462, 454, 149, 18], [336, 45, 109, 18, 466, 454, 462, 309, 162, 149], 
[462, 18, 336, 162, 149, 309, 454, 45, 466, 109], [336, 45, 149, 454, 162, 462, 309, 466, 109, 18], [336, 18, 45, 462, 149, 466, 109, 309, 162, 454], 
[462, 45, 109, 336, 149, 454, 18, 466, 162, 309]]

[960, 961, 962, 963, 964, 965, 966, 967, 968, 969]
'''

22)