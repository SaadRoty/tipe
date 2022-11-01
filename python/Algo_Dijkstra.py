import json
import numpy as np
import matplotlib.pyplot as plt
import random as rd

"""def printSolution(V,graph, dist):
    print("Vertex \t Distance from Source")
    for node in range(V):
        print(node, "\t\t", dist[node])"""

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

