
import json
import numpy as np
import matplotlib.pyplot as plt
import contextily as ctx
import xyzservices.providers as xyz

"""
import pandas as pd
import geopandas as gpd
import contextily as ctx
#import geoplot
import folium

import json
import pygeoj
"""

#Jawg.Terrain

def ExtraireRte(doc): # donne la 3Liste des 2Listes des troncons et la distance des deuxlistes
    crd = []
    longueur = []
    with open(doc) as f:
        data = json.load(f)
    for route in data:
        for param in route:
            if param == "fields":
                for c in route[param]:
                    if c == "length":
                     longueur.append(route[param][c])
                    elif c == "geom":
                        for d in route[param][c]:
                            if d == "coordinates":
                                crd.append(route[param][c][d])
    return crd,longueur

def ExtraireArr(doc): #donne la 3Liste des 2Listes des frontières des arrondissements
    crd = []
    with open(doc) as f:
        data = json.load(f)
    for route in data:
        for param in route:
            if param == "fields":
                for c in route[param]:
                    if c == "geom":
                        for d in route[param][c]:
                            if d == "coordinates":
                                crd.append(route[param][c][d][0])
                                break
    return crd

def ExtraireArrTri(doc): # donne la 4Liste des 3Listes(composees d'une seule 2Liste mais pour faire marcher GraphRte avec [n°Arr (-1)]) des frontières de chaque arrondissement
    crd = []
    with open(doc) as f:
        data = json.load(f)
    for route in data:
        for param in route:
            if param == "fields":
                for c in route[param]:
                    if c == "geom":
                        for d in route[param][c]:
                            if d == "coordinates":
                                crd.append(route[param][c][d])
    crd[0],crd[19],crd[15],crd[14],crd[8],crd[1],crd[3],crd[13],crd[11],crd[5],crd[4],crd[12],crd[10],crd[18],crd[17],crd[16],crd[6]=crd[19],crd[15],crd[14],crd[8],crd[1],crd[3],crd[13],crd[11],crd[5],crd[4],crd[12],crd[10],crd[18],crd[17],crd[16],crd[6],crd[0]
    crd[2],crd[9] = crd[9],crd[2]
    return crd

def GraphRte(crd): #prend en charge une 3Liste et trace les troncons de chaque 2Liste indépendament

    for trc in crd:
        X=[]
        Y=[]
        for pt in trc:
            X.append(pt[0])
            Y.append(pt[1])
        plt.plot(X,Y)

    plt.title("Cartographie des voies de Paris par tronçons")
    plt.xlabel("Longitude (°)")
    plt.ylabel("Latitude (°)")
    plt.show()

def GraphRtePlan(crd): # plan de Paris en arrière plan de GraphRte

    for trc in crd:
        X=[]
        Y=[]
        for pt in trc:
            X.append(pt[0])
            Y.append(pt[1])
        plt.plot(X,Y)

    img = plt.imread("../assets/pictures/carteParis.jpg")
    plt.imshow(img, extent=[2.2205, 2.471, 48.804, 48.905])

    plt.title("Cartographie des voies de Paris par tronçons")
    plt.xlabel("Longitude (°)")
    plt.ylabel("Latitude (°)")
    plt.show()

def PtExtrem(crd): #prend en argument une 4Liste et renvoie la 2Liste des Listes composees des 4 crd extremes des pts classees par arrondissement

    Rep = []

    for Arr in range(20):

        N,S,E,W=crd[Arr][0][0][1],crd[Arr][0][0][1],crd[Arr][0][0][0],crd[Arr][0][0][0]

        for pt in range(1,len(crd[Arr][0])):

            P=crd[Arr][0][pt]

            if P[0]>E:
                E=P[0]

            if P[0]<W:
                W = P[0]

            if P[1]>N:
                N = P[1]

            if P[1]<S:
                S = P[1]
        Rep.append([N,S,E,W])
    return Rep

def TriRteArr(crd): # prend en arg une 3Liste renvoie une 4liste composée de 3Listes contenant les 2listes des trc tries par Arr
    L=PtExtrem(ExtraireArrTri("../assets/json/arrondissements.json"))

    Rep=[[]for i in range(20)]

    verif=0
    for trc in crd:
        verif=+1
        for Arr in range(20):
            if trc[0][1]<=L[Arr][0] and trc[0][1]>=L[Arr][1] and trc[0][0]<=L[Arr][2] and trc[0][0]>=L[Arr][3] :
                Rep[Arr].append(trc)
                verif-=1
                break

    return Rep,("nb de trc abs = ",verif)

def GraphArr(crd):
    color=["b","g","r","c","m","y","k"]
    for Arr in range(20):
        for trc in crd[Arr]:
            X = []
            Y = []
            for pt in trc:
                X.append(pt[0])
                Y.append(pt[1])
            plt.plot(X,Y,color[Arr%7])

    img = plt.imread("../assets/pictures/carteParis.jpg")
    plt.imshow(img, extent=[2.2205, 2.471, 48.804, 48.905])

    plt.title("Cartographie des voies de Paris par tronçons")
    plt.xlabel("Longitude (°)")
    plt.ylabel("Latitude (°)")
    plt.show()

def GraphArrBeau(crd):
    color=["b","g","r","c","g","m","y","k","m","k","m","b","r","c","b","r","c","y","c","g"]
    for Arr in range(20):
        for trc in crd[Arr]:
            X = []
            Y = []
            for pt in trc:
                X.append(pt[0])
                Y.append(pt[1])
            plt.plot(X,Y,color[Arr])

    img = plt.imread("../assets/pictures/carteParis.jpg")
    plt.imshow(img, extent=[2.2205, 2.471, 48.804, 48.905])

    plt.title("Cartographie des voies de Paris par tronçons")
    plt.xlabel("Longitude (°)")
    plt.ylabel("Latitude (°)")
    plt.show()





