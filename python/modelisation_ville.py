## Bibliothèques

import json
import numpy as np
import matplotlib.pyplot as plt
import contextily as ctx
import xyzservices.providers as xyz

from fonctions import ExtraireRte
from fonctions import ExtraireArr
from fonctions import ExtraireArrTri
from fonctions import GraphRte
from fonctions import GraphRtePlan
from fonctions import PtExtrem
from fonctions import TriRteArr
from fonctions import GraphArr
from fonctions import GraphArrBeau


#GraphRte(ExtraireRte("../assets/json/troncon_voie.json")[0])

#print(ExtraireArrTri("../assets/json/arrondissements.json")[0][0][0])

#GraphRte(ExtraireArr("../assets/json/arrondissements.json"))

#GraphRtePlan(ExtraireArrTri("../assets/json/arrondissements.json")[0])

#GraphRte(TriRteArr(ExtraireRte("../assets/json/troncon_voie.json")[0])[0][11])

#print(TriRteArr(ExtraireRte("../assets/json/troncon_voie.json")[0])[0])

#print(GraphArr(ExtraireRte("../assets/json/troncon_voie.json")[0]))

GraphArrBeau(TriRteArr(ExtraireRte("../assets/json/troncon_voie.json")[0])[0])

