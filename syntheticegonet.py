# -*- coding: utf-8 -*-
"""
    LAST UPDATE: 4 Νοεμβρίου 2012
    
    @author: Moses Boudourides
    """

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

p=0.3
q=1
n=5
m=1
k=n
d=2 #Οριζόντια διαχωριστική απόσταση μεταξύ των ομάδων στον σχεδιασμό του γράφου. Για το circular_layout αρκεί d=0.5, ενώ για το spring_layout καλύτερα d=2.

J=nx.erdos_renyi_graph(n,p) #Ο γράφος του πρώτου επιπέδου
F=nx.erdos_renyi_graph(m,p) #Ο γράφος του δευτέρου επιπέδου
H=nx.bipartite_random_graph(n,m,q) #Ο διμερής γράφος που γεφυρώνει τα δυο επίπεδα
G=nx.Graph()  #Ο τελικός σύνθετος γράφος


for node in J.nodes():
    G.add_node(node,bipartite=0)
for edge in J.edges():
    G.add_edge(edge[0],edge[1])
for edge in F.edges():
    G.add_edge(edge[0]+k,edge[1]+k)
for node in F.nodes():
    G.add_node(node+k,bipartite=1)
for edge in H.edges(data=True):
    G.add_edge(edge[0],edge[1])

pos=nx.spring_layout(G)
#pos =nx.circular_layout(G)

top_set=set()
botom_set=set()
for i in pos:
    npos=pos[i]
    if G.node[i]['bipartite']==0:
        pos[i]=[npos[0],npos[1]+d]
        top_set.add(i)
    elif G.node[i]['bipartite']==1:
        pos[i]=[npos[0],npos[1]-d]
        botom_set.add(i)

plt.figure()
nx.draw(G,pos, with_labels=True,nodelist=list(top_set),node_color='r')
nx.draw(G,pos, with_labels=True,nodelist=list(botom_set),node_color='b')
plt.show()