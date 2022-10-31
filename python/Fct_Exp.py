import json
import numpy as np
import matplotlib.pyplot as plt
import random as rd

def Crd_Extr(crd): # 3L(Paris) --> 2L(Arr) > 1L(les 4 crd extr)
    Rep = []
    for Arr in range(20):
        N,S,E,W=crd[Arr][0][1],crd[Arr][0][1],crd[Arr][0][0],crd[Arr][0][0]

        for pt in range(1,len(crd[Arr])):
            P=crd[Arr][pt]

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

def Tri_Rte_Arr_PtEx(doc_Rte,doc_Crd_Extr): # 1er Pt de chaque Trc dans ?Arr? selon meth Crd_Extr --> 4L(Paris) > 3L(Arr) > 2L(Trc) > 1L(Pt)

    with open(doc_Rte) as f1:
        crd=json.load(f1)
    with open(doc_Crd_Extr) as f2:
        L=json.load(f2)

    Rep=[[]for i in range(20)]

    for trc in crd:
        for Arr in range(20):
            if trc[0][1]<=L[Arr][0] and trc[0][1]>=L[Arr][1] and trc[0][0]<=L[Arr][2] and trc[0][0]>=L[Arr][3] :
                Rep[Arr].append(trc)
                break
    return Rep

def Trig_Arr(crd): # 2L-->
    Rep=[]
    Li=crd.copy()
    Li.pop(0)
    pt=-2
    n=len(Li)
    while n>3:
        vect1=[Li[pt][0]-Li[pt-1][0],Li[pt][1]-Li[pt-1][1]]
        vect2=[Li[pt+1][0]-Li[pt][0],Li[pt+1][1]-Li[pt][1]]

        if np.cross(vect1,vect2)<=0:
            print(Li[pt-1],[Li[pt],Li[pt+1]])
            Rep.append([Li[pt-1],Li.pop(pt),Li[pt],[100,-100]])
            print(Li[pt - 1],Li[pt])
            n=n-1
            pt=-2

        else:
            pt+=1
    Rep.append([Li[0], Li[1], Li[2], Li[0]])
    return [Rep[0]]

