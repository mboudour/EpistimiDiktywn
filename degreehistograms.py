# -*- coding: utf-8 -*-
"""
    LAST UPDATE: 10 Νοεμβρίου 2014
    
    @author: Moses Boudourides
    """


import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

#Βαθμοί κόμβων μη κατευθυνόμενων γράφων

G = nx.erdos_renyi_graph(100,0.5)

for node in G.nodes():
    print str("The degree of node ") + str(node) + str(" in G is:") + '  ' + str(G.degree(node))
print "G.degree(4) == len(G.neighbors(4)) is", G.degree(4) == len(G.neighbors(4))

print G.degree() #Το ίδιο με nx.degree(G)
print "G.degree() == nx.degree(G) is", G.degree() == nx.degree(G)

#Ιστόγραμμα κατανομής βαθμών κόμβων μη κατευθυνόμενων γράφων

degree_sequence=sorted(G.degree().values(),reverse=True)
dmax=max(degree_sequence)

pla=[0.47,0.47,0.47,0.47]
a=0.3
pos=nx.spring_layout(G)

plt.figure()
plt.plot(degree_sequence,'g-',marker='o')
plt.ylabel("Degree")
plt.xlabel("Number of nodes")
plt.axes(pla)
plt.axis('off')
nx.draw_networkx_nodes(G,pos=pos,node_size=20,node_color='g',alpha=a)
nx.draw_networkx_edges(G,pos=pos,alpha=a)

fig,ax=plt.subplots()
ax.loglog(degree_sequence,'g-',marker='o') #Άλλες επιλογές semilogx, semilogy
ax.set_ylabel("Degree (log)")
ax.set_xlabel("Number of nodes (log)")
start,end=ax.get_xlim()
t=10 #Ανα πόσα ticks να εκτυπώνεται ο αριθμός τους
ax.xaxis.set_ticks(np.arange(start,end+2,t))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
plt.axes(pla)
plt.axis('off')
nx.draw_networkx_nodes(G,pos=pos,node_size=20,node_color='g',alpha=a)
nx.draw_networkx_edges(G,pos=pos,alpha=a)

#Βαθμοί κόμβων κατευθυνόμενων γράφων

G = nx.erdos_renyi_graph(100,0.5,directed=True)

G.in_degree()
G.out_degree()
G.degree() #το άθροισμα των in-degrees και out-degrees. Το ίδιο με nx.degree(G)

for node in G.nodes():
    print str("The out-degree of node ") + str(node) + str(" in G is:") + '  ' + str(G.out_degree(node))
print "G.out_degree(4) == len(G.neighbors(4)) is", G.out_degree(4) == len(G.neighbors(4))
for node in G.nodes():
    print str("The in-degree of node ") + str(node) + str(" in G is:") + '  ' + str(G.in_degree(node))
print "G.in_degree(4) == len(G.predecessors(4)) is", G.in_degree(4) == len(G.predecessors(4))

print G.degree() #Το ίδιο με nx.degree(G)
print "G.degree() == nx.degree(G) is", G.degree() == nx.degree(G)
print "G.degree(4) == G.out_degree(4) + G.in_degree(4) is", G.degree(4) == G.out_degree(4) + G.in_degree(4)

#Ιστόγραμμα κατανομής βαθμών κόμβων κατευθυνόμενων γράφων

indegree_sequence=sorted(G.in_degree().values(),reverse=True)
outdegree_sequence=sorted(G.out_degree().values(),reverse=True)
dmax=max(indegree_sequence,outdegree_sequence)

pla=[0.47,0.47,0.47,0.47]
a=0.2
pos=nx.spring_layout(G)

plt.figure()
plt.plot(indegree_sequence,'b-',marker='o')
plt.plot(outdegree_sequence,'r-',marker='o')
plt.ylabel("In[blue]/Out[red] Degree")
plt.xlabel("Number of nodes")
plt.axes(pla)
plt.axis('off')
nx.draw_networkx_nodes(G,pos=pos,node_size=20,node_color='b',alpha=a)
nx.draw_networkx_edges(G,pos=pos,alpha=a)

fig,ax=plt.subplots()
ax.loglog(indegree_sequence,'b-',marker='o')
ax.loglog(outdegree_sequence,'r-',marker='o')
ax.set_ylabel("In[blue]/Out[red] Degree (log)")
ax.set_xlabel("Number of nodes (log)")
start,end=ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start,end+2,t))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
plt.axes(pla)
plt.axis('off')
nx.draw_networkx_nodes(G,pos=pos,node_size=20,node_color='r',alpha=a)
nx.draw_networkx_edges(G,pos=pos,alpha=a)

plt.show()
