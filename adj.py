# -*- coding: utf-8 -*-
"""
    LAST UPDATE: 5 Νοεμβρίου 2014
    
    @author: Moses Boudourides
    """


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

G = nx.erdos_renyi_graph(20,0.1)
G.nodes()
G.edges()
G.neighbors(5)

Gd = nx.erdos_renyi_graph(20,0.1,directed=True)
Gd.nodes()
Gd.edges()
Gd.neighbors(5)

A = nx.adjacency_matrix(G)
print(A.todense())

adjacency_matrix = nx.to_numpy_matrix(G)
fig = plt.figure(figsize=(5, 5))
plt.imshow(adjacency_matrix,cmap="Greys",interpolation="none")
plt.show()