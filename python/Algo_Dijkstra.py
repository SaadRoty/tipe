import json
import numpy as np
import matplotlib.pyplot as plt
import random as rd

"""def printSolution(V,graph, dist):
    print("Vertex \t Distance from Source")
    for node in range(V):
        print(node, "\t\t", dist[node])"""

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

def minDistance(V,graph, dist, sptSet):
    min = 1e5
    min_index=0
    for v in range(V):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v
    return min_index

def dijkstra(V,graph, src):
    dist = [1e5] * V
    dist[src] = 0
    sptSet = [False] * V
    for cout in range(V):
        u = minDistance(V,graph,dist,sptSet)
        sptSet[u] = True
        for v in range(V):
            if (graph[u][v] > 0 and
                    sptSet[v] == False and
                    dist[v] > dist[u] + graph[u][v]):
                dist[v] = dist[u] + graph[u][v]
    print(len(dist))
    return(dist)

