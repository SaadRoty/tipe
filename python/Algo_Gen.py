import json
import numpy as np
import matplotlib.pyplot as plt
import random as rd

'''n= lenlist'''

#def Init_Pop():

def Fitness(chrom,n):
    dist = 0

    with open("../assets/output/json/3L_Voisins_Dist_Trc_1erArr.json") as f:
        g = json.load(f)

    def A_Etoile(r, s):

        def h(x):  #
            return np.sqrt((g[1][r][0] + g[1][x][0]) ** 2 + (g[1][r][1] + g[1][x][1]) ** 2)

        def Extraire_Min(F, dist):
            m = 0
            for j in range(1, len(F)):
                if dist[F[j]] + h(F[j]) < dist[F[m]] + h(F[m]):
                    m = j
            x = F[m];
            del F[m]
            return x

        def Relacher_E(x, y, g, p, dist, F):
            Z = g[0][x].index(y)
            if dist[y] > dist[x] + g[2][x][Z]:
                dist[y] = dist[x] + g[2][x][Z]
                p[y] = x
                if y not in F:
                    F.append(y)
        p = {x: 'NIL' for x in range(len(g[0]))}
        d = {x: float('inf') for x in range(len(g[0]))}
        d[r] = 0;
        F = [r]

        while F != []:
            x = Extraire_Min(F, d)
            if x == s:
                return d[s]
            for y in g[0][x]:
                Relacher_E(x, y, g, p, d, F)
        return False

    for i in range(n-1):
        dist+=A_Etoile(chrom[i],chrom[i+1])

    return dist

#def Choose_Parents():

def Crussover_PMX(P1,P2,n,i,j):
    E1=[0]*i;E2=[0]*i
    E1.extend(P2[i:j+1]);E2.extend(P1[i:j+1])
    E1.extend([0]*(n-j-1)),E2.extend([0]*(n-j-1))

    for k in range(i) :
        if P1[k] not in E1[i:j+1]:
            E1[k]=P1[k]
        else:
            l=k
            while P1[l] in E1[i:j+1]:
                l= i+ E1[i:j+1].index(P1[l])
            E1[k]=P1[l]

        if P2[k] not in E2[i:j+1]:
            E2[k] = P2[k]
        else:
            l = k
            while P2[l] in E2[i:j+1]:
                l = i + E2[i:j+1].index(P2[l])
            E2[k] = P2[l]

    for k in range(j+1,n):
        if P1[k] not in E1[i:j+1]:
            E1[k] = P1[k]
        else:
            l=k
            while P1[l] in E1[i:j+1]:
                l = i + E1[i:j+1].index(P1[l])
            E1[k] = P1[l]

        if P2[k] not in E2[i:j+1]:
            E2[k] = P2[k]
        else:
            l = k
            while P2[l] in E2[i:j+1]:
                l = i + E2[i:j+1].index(P2[l])
            E2[k] = P2[l]

    return E1,E2

#def Mutation_Operator():

#def New_Pop():







