import json
import numpy as np
import matplotlib.pyplot as plt
import random as rd

def Ext_Rte(doc): # --> 3L(Paris) > 2L(Trc) > 1L(Pt) et 1L(longueur des Trc)
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

def Ext_Arr(doc): # --> 3L(Paris) > 2L(frontière Arr) > 1L(Pt)
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

def Ext_Arr_Tri(doc): #  --> 3L(Paris) > 2L(frontière Arr_Tri) > 1L(Pt)
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
    crd[0],crd[19],crd[15],crd[14],crd[8],crd[1],crd[3],crd[13],crd[11],crd[5],crd[4],crd[12],crd[10],crd[18],crd[17],crd[16],crd[6]=crd[19],crd[15],crd[14],crd[8],crd[1],crd[3],crd[13],crd[11],crd[5],crd[4],crd[12],crd[10],crd[18],crd[17],crd[16],crd[6],crd[0]
    crd[2],crd[9] = crd[9],crd[2]
    return crd

def Ecrire_Json(elmt,doc): # écrit elmt dans doc en écrasant tout
    with open(doc,"w") as f:
        json.dump(elmt,f)

