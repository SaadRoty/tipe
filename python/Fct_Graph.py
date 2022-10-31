import json
import numpy as np
import matplotlib.pyplot as plt
import random as rd


def G_Rte(crd,titre): # 3L --> trace les Trc pour chaque 2L indépendament

    for trc in crd:
        X=[]
        Y=[]
        for pt in trc:
            X.append(pt[0])
            Y.append(pt[1])
        plt.plot(X,Y)

    plt.title(titre)
    plt.xlabel("Longitude (°)")
    plt.ylabel("Latitude (°)")
    plt.show()

def G_Rte_Carte(crd,titre): # Carte de Paris en arriere plan de G_Rte

    for trc in crd:
        X=[]
        Y=[]
        for pt in trc:
            X.append(pt[0])
            Y.append(pt[1])
        plt.plot(X,Y)

    img = plt.imread("../assets/input/pictures/carteParis.jpg")
    plt.imshow(img, extent=[2.2205, 2.471, 48.804, 48.905])

    plt.title(titre)
    plt.xlabel("Longitude (°)")
    plt.ylabel("Latitude (°)")
    plt.show()

def G_Rte_Arr(crd,titre): # 4L(Paris) > 3L(Arr) > 2L(Trc) > 1L(Pt) --> 1 couleur par Arr
    color=["b","g","r","c","m","y","k"]
    for Arr in range(20):
        for trc in crd[Arr]:
            X = []
            Y = []
            for pt in trc:
                X.append(pt[0])
                Y.append(pt[1])
            plt.plot(X,Y,color[Arr%7])

    img = plt.imread("../assets/input/pictures/carteParis.jpg")
    plt.imshow(img, extent=[2.2205, 2.471, 48.804, 48.905])

    plt.title("Cartographie des voies de Paris par tronçons")
    plt.xlabel("Longitude (°)")
    plt.ylabel("Latitude (°)")
    plt.show()

def G_Rte_Arr_Beau(crd,titre): # répartie les couleurs pour éviter les contacts entre Arr
    color=["b","g","r","c","g","m","y","k","m","k","m","b","r","c","b","r","c","y","c","g"]
    for Arr in range(20):
        for trc in crd[Arr]:
            X = []
            Y = []
            for pt in trc:
                X.append(pt[0])
                Y.append(pt[1])
            plt.plot(X,Y,color[Arr])

    img = plt.imread("../assets/input/pictures/carteParis.jpg")
    plt.imshow(img, extent=[2.2205, 2.471, 48.804, 48.905])

    plt.title(titre)
    plt.xlabel("Longitude (°)")
    plt.ylabel("Latitude (°)")
    plt.show()

def G_Aff_Poubelle(crd,titre): # affiche en rouge les Trc nécessitant une collecte
    for trc in crd:
        for pt in range(len(trc)-1):
            poubelle = rd.randint(0,4)
            if poubelle==4:
                X=[trc[pt][0],trc[pt+1][0]]
                Y=[trc[pt][1],trc[pt+1][1]]
                plt.plot(X,Y,'r')
            else:
                X = [trc[pt][0],trc[pt + 1][0]]
                Y = [trc[pt][1],trc[pt + 1][1]]
                plt.plot(X, Y, 'g')

    plt.title(titre)
    plt.xlabel("Longitude (°)")
    plt.ylabel("Latitude (°)")
    plt.show()

#def G_Rte_Est_In(crd,titre):


