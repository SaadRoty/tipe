import json
import numpy as np
import matplotlib.pyplot as plt
import random as rd



def Fitness_Exact(chrom,n):
    with open("../assets/output/json/3L_Voisins_Dist_Trc_1erArr.json") as f:
        g = json.load(f)

    dist = 0
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

def Fitness_Approximate(chrom,n,coef):
    with open("../assets/output/json/3L_Voisins_Dist_Trc_1erArr.json") as f:
        g = json.load(f)

    dist = 0
    def A_Etoile(r, s):

        def h(x):  #
            return coef * np.sqrt((g[1][r][0] + g[1][x][0]) ** 2 + (g[1][r][1] + g[1][x][1]) ** 2)

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

def Init_Weight_Pop_Exact(Pop,n):
    W=[]
    for elmnt in Pop:
        W.append(Fitness_Exact(elmnt,n))
    return W

def Init_Weight_Pop_Approximate(Pop,n,coef):
    W=[]
    for elmnt in Pop:
        W.append(Fitness_Approximate(elmnt,n,coef))
    return W

def Tri_Pop(Pop,W_Pop):
    C=sorted(zip(W_Pop,Pop))
    return [i for _,i in C],[i[0] for i in C]

def Merge_Pop_Offspring_Tri(Pop,W_Pop,Off,W_Off): # on a préalablement trié les offspring avec Tri_Pop
    Population=[]
    Weight=[]
    i=len(Pop)
    j=len(Off)
    while i>0 and j>0:
        if W_Pop[0]<W_Off[0]:
            Population.append(Pop.pop(0))
            Weight.append(W_Pop.pop(0))
            i-=1
        else:
            Population.append(Off.pop(0))
            Weight.append(W_Off.pop(0))
            j-=1
    if i==0:
        Population.extend(Off)
        Weight.extend(W_Off)
    else:
        Population.extend(Pop)
        Weight.extend(W_Pop)

    return Population,Weight

def Li_Prop_Rank(nPop):
    Sum=(nPop+1)*nPop/2

    return [i/Sum for i in range(nPop,0,-1)]

def Roulette_Parents_Choice(Pop,Li_Prop):
    return rd.choices(Pop, weights=Li_Prop,k=1)[0]

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

def Insertion_Mutation_Operator(chrom,n):
    chrom.insert(rd.randrange(0,n),chrom.pop(rd.randrange(0,n)))

def Swap_Mutation_Operator(chrom,n):
    a=rd.randrange(0,n)
    b=rd.randrange(0,n)
    chrom[a],chrom[b]=chrom[b],chrom[a]

def Reverse_Mutation_Operator(chrom,n):
    a = rd.randrange(0, n)
    b = rd.randrange(0, n)
    if a<b:
        chrom[a:b] = list(reversed(chrom[a:b]))
    else:
        chrom[b:a] = list(reversed(chrom[b:a]))

def New_Pop(Pop,W_Pop,nPop): # on a combiné la Pop et W_Pop de la gen d'avant avec les enfants créés hormis les mutés que l'on rajoutera apres
                   # on a créer 10% de nPop enfants, muté 3% de tout le monde et que l'on a sorti de la liste,
                   # on supprime ici les pires sol à partir de l'indice nPop -3% de nPop (que l'on rajoutera après c'est les mutés)
    ind = nPop - 3*int(nPop/100)
    del Pop[ind:]
    del W_Pop[ind:]

def Mutation_Generation(Pop,nPop,n):
    Mut=[]
    for i in range(3*int(nPop/100),0,-3):
        j=randrange(0,nPop+i)
        Mut.append(Insertion_Mutation_Operator(Pop.pop(j),n))

        j = randrange(0,nPop+i-1)
        Mut.append(Swap_Mutation_Operator(Pop.pop(j),n))

        j = randrange(0,nPop+i-2)
        Mut.append(Reverse_Mutation_Operator(Pop.pop(j),n))
    return Mut

def Global_Genetic_Algo(Li,n,nPop):

    with open("../assets/output/json/3L_Voisins_Dist_Trc_1erArr.json") as f:
        g = json.load(f)

    def Init_Pop_Random():
        L = Li.copy()
        Pop = [Li]
        i = 1
        while i < nPop:
            rd.shuffle(L)
            if L not in Pop:
                Pop.append(L.copy())
                i += 1
        return Pop