import json
import numpy as np
import matplotlib.pyplot as plt

def A_etoile (r,s): # r et s:  num des pt extrem depart et arrivé

    with open("../assets/output/json/3L_Voisins_Dist_Trc_1erArr.json") as f:
        g = json.load(f)

    def h(x): #
        return np.sqrt((g[1][r][0]+g[1][x][0])**2 + (g[1][r][1]+g[1][x][1])**2)

    def Extraire_Min (F,dist):
        m=0
        for j in range (1,len(F)):
            if dist[F[j]]+h(F[j])<dist[F[m]]+h(F[m]):
                m=j
        x=F[m]; del F[m]
        return x

    def Relacher_E (x,y,g,p,dist,F):
        Z=g[0][x].index(y)
        if dist[y] > dist[x]+g[2][x][Z]:
            dist[y] = dist[x]+g[2][x][Z]
            p[y] = x
            if y not in F:
                F.append(y)

    def Chem_A_etoile(p, start, end):
        pt = end
        rep = [pt]
        while pt != start:
            pt=p[pt]
            rep.insert(0,pt)
        return rep

    p={x:'NIL' for x in range(len(g[0]))}
    d={x:float('inf') for x in range(len(g[0]))}
    d[r]=0 ; F=[r]

    while F!=[]:
        x=Extraire_Min(F,d)
        if x==s:
            return d[s],Chem_A_etoile(p,r,s)
        for y in g[0][x]:
            Relacher_E(x,y,g,p,d,F)
    return False

def Chemin_final(chem):

    with open("../assets/output/json/3L_Voisins_Dist_Trc_1erArr.json") as f:
        g = json.load(f)

    Vrai_Chem=[]
    for i in range(len(chem)-1):
        y=g[0][chem[i]].index(chem[i+1])
        Vrai_Chem.append(g[3][chem[i]][y])
    return Vrai_Chem

def trace_Chem(start,end):

    with open("../assets/output/json/Trc_Paris_Tri_Meth_Est_In.json") as f:
        data = json.load(f)

    with open("../assets/output/json/3L_Voisins_Dist_Trc_1erArr.json") as f:
        G = json.load(f)

    for trc in data[0]:
        X = []
        Y = []
        for pt in trc:
            X.append(pt[0])
            Y.append(pt[1])
        plt.plot(X, Y, 'g')

    for trc in data[0]:
        X = []
        Y = []
        for pt in trc:
            X.append(pt[0])
            Y.append(pt[1])
        plt.plot(X, Y, 'g')

    for trc in Chemin_final(A_etoile(start, end)[1]):
        X = []
        Y = []
        for pt in trc:
            X.append(pt[0])
            Y.append(pt[1])
        plt.plot(X, Y, 'r')

    plt.plot(G[1][start][0], G[1][start][1], "bo");
    plt.plot(G[1][end][0], G[1][end][1], "rX")

    plt.show()