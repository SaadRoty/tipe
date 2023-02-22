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

def Trig_Arr(crd): # 2L(Fr_Arr) --> Non utilisée (methode pas finalisée)
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

def Est_In(Pt,Arr): # 1L(Pt) et 2L(Arr) > 1L(Pt) --> Bool
    x, y = Pt[0], Pt[1]
    if Pt in Arr:
        return True
    """for i in range(len(Arr)-1):
        x1, x2 = Arr[i][0], Arr[i + 1][0]
        y1, y2 = Arr[i][1], Arr[i + 1][1]

        if x2 < x1:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        if x>x1 and x<x2:
            if (y-y1)/(x-x1)==((y2-y)/(x2-x)):
                return True"""
    cp=0
    x,y=Pt[0],Pt[1]
    for i in range(len(Arr)-1):
        x1,x2=Arr[i][0],Arr[i+1][0]
        y1,y2=Arr[i][1],Arr[i+1][1]

        if x2<x1:
            x1,x2=x2,x1
            y1,y2=y2,y1

        if (x2 < x) or (y2 < y if y1 < y else y2 > y):
            continue
        if (x1==x2) or (y1==y2 and x1<x):
            return True

        if x1 > x:
            cp += 1
            continue

        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1
        Y = (y2 - y1)/(x2 - x1)*(x-x1)+y1

        if (Y < y if a < 0 else Y > y):
            continue
        cp += 1
    if cp%2==0:
        return False
    return True

def Tri_Est_In(crd,Arr,dist): # 3L(Paris) > 2L(Trc) > 1L(Pt) et 3L(ArrS) et 1L(Paris) > (dist) > 2L (Arr) > 1L(Pt) --> 4L(Paris) > 3L(Arr) > 2L(Trc) > 1L(Pt)
    N,M=0,0
    Rep=[[]for i in range(20)]
    abs=[]
    Dist=[[]for i in range(20)]

    j=-1
    for Trc in crd:
        j+=1
        verif=0
        cp=0
        while verif == 0 and cp<len(Trc):
            for i in range(20):
                if Est_In(Trc[cp],Arr[i]):
                    Rep[i].append(Trc)
                    Dist[i].append(dist[j])
                    N+=1
                    verif=1
                    break
            cp+=1
        if verif==0:
            M+=1
            abs.append(Trc)
    return Rep,(N,M),abs, Dist

def Renom_Pt_Extr_Trc(crd): # 3L(Arr) > 2L(Trc) > 1L(Pt) --> 2L(Arr) > 1L(Trc) : [Num(Start),Num(End)] et NumPt
    Rep=[[0,0]for i in range(len(crd))]
    Rep[0][1]=1
    NumPt = 2
    EquivalentCrd=[crd[0][0],crd[0][-1]]

    for Trc in range(1,len(crd)):
        St,End=0,0
        for j in range(Trc):
            if St == 0:
                if crd[Trc][0] == crd[j][0]:
                    Rep[Trc][0] = Rep[j][0]
                    St = 1
                elif crd[Trc][0] == crd[j][-1]:
                    Rep[Trc][0] = Rep[j][-1]
                    St = 1

            if End == 0:
                if crd[Trc][-1] == crd[j][0]:
                    Rep[Trc][-1] = Rep[j][0]
                    End = 1
                elif crd[Trc][-1] == crd[j][-1]:
                    Rep[Trc][-1] = Rep[j][-1]
                    End = 1

        if St==0:
            Rep[Trc][0] = NumPt
            NumPt += 1
            EquivalentCrd.append(crd[Trc][0])
        if End==0:
            Rep[Trc][-1] = NumPt
            NumPt += 1
            EquivalentCrd.append(crd[Trc][-1])
    return Rep,NumPt,EquivalentCrd

def Trouv_Vois(crd,NumPt,dist): # 2L(Arr) > 1L(Trc) et 1L(dist) : (Num(Start),Num(End)) et 1L(Dist_Trc) --> 2*3L(Arr) > 1*2L : [Pt,[Voisin1,dist],[Voisin2,dist],...]
    
    Rep=[[Pt]for Pt in range(NumPt)]

    for Pt in range(NumPt):
        for Trc in range(len(crd)):
            if crd[Trc][0]==Pt:
                Rep[Pt].append([crd[Trc][-1],dist[Trc]])
            if crd[Trc][-1]==Pt:
                Rep[Pt].append([crd[Trc][0],dist[Trc]])

    for Pt in Rep:
        for Vois in range(1,len(Pt)):
            N=Vois
            while N>1 and Pt[N][0]<Pt[N-1][0]:
                Pt[N],Pt[N - 1] = Pt[N-1],Pt[N]
                N=N-1
    return Rep

def Div_Li_Vois(Li): # 2*3L(Arr) > 1*2L : [Pt,[Voisin1,dist],[Voisin2,dist],...] --) 2L(Voisin) et 2L(distance]
                     # pour les pt d'indice croissant correspondant a l'indice dans la liste
    Voisinage=[[] for i in range(len(Li))]
    Distance=[[] for i in range(len(Li))]
    for i in range(len(Li)):
        for j in range(1,len(Li[i])):
            Voisinage[i].append(Li[i][j][0])
            Distance[i].append(Li[i][j][1])
    return Voisinage,Distance

def Trc_Associe_Vois(Voisinage,TrcRenom,TrcTri): #2L(Voisin) et 2L(TrcRenom) --> 4L(Voisinage) > 3L(Voisins) > 2L(TrcAsso) > 1L(Pt)
    Rep=[[]for Vois in range(len(Voisinage))]

    for Vois in range(len(Voisinage)):
        for NumVois in range(len(Voisinage[Vois])):

            if [Vois,Voisinage[Vois][NumVois]] in TrcRenom:

                indx = TrcRenom.index([Vois,Voisinage[Vois][NumVois]])
            else:
                indx = TrcRenom.index([Voisinage[Vois][NumVois],Vois])

            Rep[Vois].append(TrcTri[indx])

    return Rep


#brouillon

def Plus_Proche_Vois(A,Vois,Dist): # Pt de départ et Listes des Voisins ainsi que des Dist aux Voisins dans Arr --> Voisin le plus proche
    indx = 0
    dist=Dist[A][indx]
    for i in range(1,len(Dist[A])):
        if Dist[A][i]<dist:
            indx=i
            dist = Dist[A][indx]
    return Vois[A][indx]

def Dist_Chemin_Graph(Chmt,Vois,Dist): # Liste des Pt visités et liste des Dist aux Voisins dans Arr --> Distance Totale
    distT=0
    for Pt in range(len(Chmt)-1):
        indx=Vois[Chmt[Pt]].index(Chmt[Pt+1])
        distT+=Dist[Chmt[Pt]][indx]
    return distT

def Dijkstra(A,B,Vois,Dist): # pas finalisée, utilisiation d'un autre algorithme plus rapide
    if B in Vois[A]:
        return [A,B]
    V=Vois.copy()
    D=Dist.copy()
    Chemin=[A]
    DistT=0
    prev=A
    next=A

    while B not in Vois[next]:
        prev = next
        next = Plus_Proche_Vois(prev,V,D)

        print(V[prev])
        print(next)
        indx=V[prev].index(next)
        del(V[prev][indx])
        print
        del(D[prev][indx])

    return V

def Mat_Adj(Vois,Dist):
    Mat=np.zeros([len(Vois),len(Vois)])
    for i in range (len(Vois)):
        for j in range(len(Vois[i])):
            Mat[i][Vois[i][j]]=Dist[i][j]
    return Mat


# fin brouillon




