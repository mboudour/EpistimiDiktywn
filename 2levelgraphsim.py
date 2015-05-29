# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
from pylab import hist
import colorBar
from collections import Counter


### Undirected Random Graphs Erdos-Renyi

p1=0.2
p2=0.3
q=0
n=500
m=800
k=n
#step=0.01
step=0.1
an = p1*n
am = p2*m
dif=abs(n-m)
print "The difference in numbers of nodes is %s" %dif
print str("The two peaks are at average degrees: ") + str(an ) + str(" and ") + str(am)
print
print "Q value| J1peak-F1peak"
qli=[]
absli=[]
#while q<0.9:
while q<0.5:
    J=nx.erdos_renyi_graph(n,p1) #Ο γράφος του πρώτου επιπέδου
    F=nx.erdos_renyi_graph(m,p2) #Ο γράφος του δευτέρου επιπέδου
    H=nx.bipartite_random_graph(n,m,q) #Ο διμερής γράφος που γεφυρώνει τα δυο επίπεδα
    G=nx.Graph()  #Ο τελικός σύνθετος γράφος
    for node in J.nodes():
        G.add_node(node,bipartite=0)
    for edge in J.edges():
        G.add_edge(edge[0],edge[1])

    J1=G.subgraph(J.nodes())

    for edge in F.edges():
        G.add_edge(edge[0]+k,edge[1]+k)
    for node in F.nodes():
        G.add_node(node+k,bipartite=1)
    for edge in H.edges(data=True):
        G.add_edge(edge[0],edge[1])
    J1=G.subgraph(J.nodes())
    Jcount=Counter()
    Jdeg=J1.degree()
    for jj in Jdeg:
        Jcount[Jdeg[jj]]+=1
    Jmax=max(Jcount.values())
    for jj in Jcount:
        if Jcount[jj]==Jmax:
            Jan=jj

    Fnod=[]
    for i in F.nodes():
        Fnod.append(i+k)
    F1=G.subgraph(Fnod)
    Fcount=Counter()
    Fdeg=F1.degree()
    for jj in Fdeg:
        Fcount[Fdeg[jj]]+=1
    Fmax=max(Fcount.values())
    for jj in Fcount:
        if Fcount[jj]==Fmax:
            Fan=jj

    deg=G.degree()
    qli.append(q)
    absli.append(abs(Fan-Jan))
    print "%7.3f|%7d" %(q,abs(Fan-Jan))
    q+=step
plt.figure()
plt.plot(qli,absli)
plt.show()

    
