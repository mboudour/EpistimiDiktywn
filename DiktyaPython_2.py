# -*- coding: utf-8 -*-
"""
    LAST UPDATE: 12 Νοεμβρίου 2014
    
    @author: Moses Boudourides
    """


import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import scipy as sp
import random
import pylab as pt
from pylab import hist
import colorBar



G = nx.erdos_renyi_graph(20,0.5)
pos=nx.spring_layout(G)
Gd = nx.erdos_renyi_graph(10,0.5,directed=True)
posd=nx.spring_layout(Gd)


##### ΓΕΙΤΝΙΑΣΗ-ΒΑΘΜΟΙ-ΚΑΤΑΝΟΜΕΣ ΜΗ ΚΑΤΕΥΘΥΝΟΜΕΝΩΝ ΑΠΛΩΝ ΓΡΑΦΩΝ

##### Γειτνίαση κόμβων μη κατευθυνόμενων γράφων

##### Σύνολα κόμβων και ακμών

print str("THE CASE OF AN UNDIRECTED SIMPLE GRAPH G")
print str(" ")

print str("SETS OF NODES AND EDGES G.nodes(), G.edges()")
print str("The set of nodes of G is ") + str(G.nodes())
print str("The set of edges of G is ") + str(G.edges())
print str(" ")

##### Γείτονες κάποιου κόμβου

print str("SET OF NEIGHBORS OF A NODE G.neighbors(node)")
node = 4
print str("The neighbors of node ") + str(node) + str(" are:") + str(G.neighbors(node))
print str(" ")

##### Γείτονες όλων των κόμβων:

print str("SET OF NEIGHBORS OF ALL NODES")
for node in G.nodes():
    print str("The neighbors of node ") + str(node) + str(" are:") + str(G.neighbors(node))
print str(" ")

##### Πίνακας γειτνίασης

print str("ADJACENCY MATRIX nx.adjacency_matrix(G)")
A = nx.adjacency_matrix(G)
print str("The adjacency matrix of G is: ")
print(A.todense())
print str(" ")

##### Σχεδιασμός plot του γράφου και του spy plot του πίνακα γειτνίασης

# plt.figure()
# nx.draw(G,pos=pos,with_labels=True,node_color='g',alpha=0.5)
#
# adjacency_matrix = nx.to_numpy_matrix(G)
# fig = plt.figure(figsize=(5, 5))
# plt.imshow(adjacency_matrix,cmap="Greys",interpolation="none")

##### Βαθμοί κόμβων μη κατευθυνόμενων γράφων

print str("THE CASE OF AN UNDIRECTED SIMPLE GRAPH G")
print str(" ")

print str("DEGREE OF A NODE G.degree(node)")
node = 4
print str("The neighbors of node ") + str(node) + str(" are:") + str(G.neighbors(node))
print str("The degree of node ") + str(node) + str(" is: ") + str(G.degree(node))
print str(" ")

print str("CHECK THAT G.degree(4) == len(G.neighbors(4))")
print "G.degree(4) == len(G.neighbors(4)) is", G.degree(4) == len(G.neighbors(4))
print str(" ")

print str("DEGREES OF ALL NODES G.degree(node)")
for node in G.nodes():
    print str("The degree of node ") + str(node) + str(" is: ") + str(G.degree(node))
print str(" ")

print str("DEGREES OF ALL NODES AS DICTIONARY G.degree()")
print G.degree() #Το ίδιο με nx.degree(G)
print str(" ")

print str("CHECK THAT G.degree() == nx.degree(G)")
print "G.degree() == nx.degree(G) is", G.degree() == nx.degree(G)
print str(" ")

node = 4
Gn = nx.Graph()
for v in G.neighbors(node):
    Gn.add_edge(node,v)

# plt.figure()
# nx.draw(G,pos=pos,with_labels=True,node_size=500,alpha=0.5)
# nx.draw_networkx_edges(Gn,pos=pos,with_labels=False,edge_color='r',width=6.0,alpha=0.5)


###### ΓΙΑ ΣΧΕΤΙΚΑ  Μ Ι Κ Ρ Ο Υ Σ  ΓΡΑΦΟΥΣ ΜΟΝΟ!!!!!!

##### Ραβδόγραμμα βαθμών κόμβων

deg=G.degree()
deg_dic=dict()
for nd in deg:
    if deg[nd] not in deg_dic:
        deg_dic[deg[nd]]=[nd]
    else:
        deg_dic[deg[nd]].append(nd)
deg_lis=[]
nd_lis=[]
for de in sorted(deg_dic.keys(),reverse=True):
    for nn in deg_dic[de]:
        deg_lis.append(de)
        nd_lis.append(nn)

# fig, ax = plt.subplots()
#plt.hist(deg_lis,len(nd_lis), histtype='stepfilled')
index = np.arange(len(nd_lis))
bar_width = 0.35

pla=[0.47,0.47,0.47,0.47]
a=0.3

plt.figure()
plt.bar(index, deg_lis, bar_width,
                 #alpha=opacity,
                 color='g',
                 #yerr=std_men,
                 #error_kw=error_config,
                 label='Degree')
plt.ylabel("Degree")
plt.xlabel("Nodes")
plt.title('Bar Plot of Degrees of Nodes')
# plt.legend(['Ραβδόγραμμα Βαθμών'])

##### Την επόμενη εντολή την βάζετε ΜΟΝΟ όταν έχετε σχετικά μικρό αριθμό κόμβων
plt.xticks(index + bar_width/2, nd_lis)

##### Τις παρακάτω εντολές τις βάζετε αν θέλετε να βγαίνει ο γράφος στην πάνω δεξια γωνία - ΜΟΝΟ για σχετικά μικρούς γράφους

plt.axes(pla)
plt.axis('off')
nx.draw_networkx_nodes(G,pos=pos,node_size=400,node_color='g',alpha=a)
labels={}
for v in G.nodes():
    labels[v]=v
nx.draw_networkx_labels(G,pos,labels,font_size=12)
nx.draw_networkx_edges(G,pos=pos,alpha=a)

##### Ιστογράμματα κατανομής βαθμών κόμβων

deg = G.degree()

pla=[0.47,0.47,0.47,0.47]
a=0.3

plt.figure()
# hist(deg.values(),bins=len(set(G.degree().values())),normed=True,color='g')
# plt.ylabel("Percentage of nodes")
hist(deg.values(),bins=len(G.degree().values()),color='g')
plt.ylabel("Number of nodes")
plt.xlabel("Degree")
plt.title('Histogram of Degrees of Nodes')

plt.axes(pla)
plt.axis('off')

nx.draw_networkx_nodes(G,pos=pos,node_size=400,node_color='g',alpha=a)
nx.draw_networkx_edges(G,pos=pos,alpha=a)


###### ΓΙΑ ΣΧΕΤΙΚΑ  Μ Ε Γ Α Λ Ο Υ Σ  ΓΡΑΦΟΥΣ ΜΟΝΟ!!!!!!

G = nx.erdos_renyi_graph(200,0.5)

deg=G.degree()
deg_dic=dict()
for nd in deg:
    if deg[nd] not in deg_dic:
        deg_dic[deg[nd]]=[nd]
    else:
        deg_dic[deg[nd]].append(nd)
deg_lis=[]
nd_lis=[]
for de in sorted(deg_dic.keys(),reverse=True):
    for nn in deg_dic[de]:
        deg_lis.append(de)
        nd_lis.append(nn)

# fig, ax = plt.subplots()
#plt.hist(deg_lis,len(nd_lis), histtype='stepfilled')
index = np.arange(len(nd_lis))
bar_width = 0.35

pla=[0.47,0.47,0.47,0.47]
a=0.3

plt.figure()
plt.bar(index, deg_lis, bar_width,
                 #alpha=opacity,
                 color='g',
                 #yerr=std_men,
                 #error_kw=error_config,
                 label='Degree')
plt.ylabel("Degree")
plt.xlabel("Nodes")
plt.title('Bar Plot of Degrees of Nodes')

##### Ιστογράμματα κατανομής βαθμών κόμβων

deg = G.degree()

plt.figure()
# hist(deg.values(),bins=len(set(G.degree().values())),normed=True,color='g')
# plt.ylabel("Percentage of nodes")
hist(deg.values(),bins=len(set(G.degree().values())),color='g')
plt.ylabel("Number of nodes")
plt.xlabel("Degree")
plt.title('Histogram of Degrees of Nodes')

##### Ιστογράμματα σε Λογαριθμικές Κλίμακες
##### ?????????

# plt.figure()
# deg = G.degree()
# hist(deg.values(),bins=len(set(G.degree().values())),color='g') #bins=30,
# plt.ylabel("Degree")
# plt.xlabel("Number of nodes")
# plt.title('Histogram of Degrees of Nodes')
# plt.ylabel("Degree (log)")
# plt.xlabel("Number of nodes (log)")
# plt.yscale('log')
# plt.xscale('log')
# plt.title('Histogram of Degrees of Nodes (log)')

deg = G.degree()
#deg = nx.degree(G,weight='weight')
#val=set(deg.values())
#hist_deg= [deg.values().count(x) for x in val]
values = sorted(set(deg.values()))
hist = [deg.values().count(x) for x in values]

# plt.figure()
# plt.plot(values,hist,'go-')
# #plt.plot(val,hist_deg, 'b*-')
# # plt.legend(['Ιστόγραμμα Κατανομής Βαθμών'])
# plt.xlabel('Degree')
# plt.ylabel('Number of nodes')
# # plt.yscale('log') #Λογαριθμική κλίμακα άξονα y
# # plt.xscale('log') # Λογαριθμική κλίμακα άξονα x

plt.figure()
plt.xlim( min(set(deg.values())), max(set(deg.values())) )
plt.ylim( 1, max(hist) )
plt.plot(values,hist,'go-')
#plt.plot(val,hist_deg, 'b*-')
# plt.legend(['Ιστόγραμμα Κατανομής Βαθμών (log)'])
plt.xlabel('Number of nodes (log)')
plt.ylabel('Degree (log)')
plt.yscale('log')
plt.xscale('log')
plt.title('Histogram of Degrees of Nodes (log)')

print max(hist)

# plt.figure()
# plt.plot(values,hist,'go-')
# #plt.plot(val,hist_deg, 'b*-')
# # plt.legend(['Ιστόγραμμα Κατανομής Βαθμών (log)'])
# plt.xlabel('Degree')
# plt.ylabel('Number of nodes (log)')
# plt.yscale('log') #Λογαριθμική κλίμακα άξονα y
# # plt.xscale('log') # Λογαριθμική κλίμακα άξονα x
#
# plt.figure()
# plt.plot(values,hist,'go-')
# #plt.plot(val,hist_deg, 'b*-')
# # plt.legend(['Ιστόγραμμα Κατανομής Βαθμών (log)'])
# plt.xlabel('Degree (log)')
# plt.ylabel('Number of nodes')
# # plt.yscale('log') #Λογαριθμική κλίμακα άξονα y
# plt.xscale('log') # Λογαριθμική κλίμακα άξονα x





# degree_sequence=sorted(G.degree().values(),reverse=True)
# dmax=max(degree_sequence)
#
# pla=[0.47,0.47,0.47,0.47]
# a=0.3
#
# plt.figure()
# plt.plot(degree_sequence,'g-',marker='o')
# plt.ylabel("Degree")
# plt.xlabel("Nodes")
# plt.axes(pla)
# plt.axis('off')
# nx.draw_networkx_nodes(G,pos=pos,node_size=20,node_color='g',alpha=a)
# nx.draw_networkx_edges(G,pos=pos,alpha=a)

# fig,ax=plt.subplots()
# ax.loglog(degree_sequence,'g-',marker='o') #Άλλες επιλογές semilogx, semilogy
# ax.set_ylabel("Degree (log)")
# ax.set_xlabel("Nodes (log)")
# start,end=ax.get_xlim()
# t=2 #Ανα πόσα ticks να εκτυπώνεται ο αριθμός τους
# ax.xaxis.set_ticks(np.arange(start,end+2,t))
# ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
# plt.axes(pla)
# plt.axis('off')
# nx.draw_networkx_nodes(G,pos=pos,node_size=20,node_color='g',alpha=a)
# nx.draw_networkx_edges(G,pos=pos,alpha=a)







# ##### ΓΕΙΤΝΙΑΣΗ-ΒΑΘΜΟΙ-ΚΑΤΑΝΟΜΕΣ ΚΑΤΕΥΘΥΝΟΜΕΝΩΝ ΑΠΛΩΝ ΓΡΑΦΩΝ
#
# print str("THE CASE OF A DIRECTED SIMPLE GRAPH G")
# print str(" ")
#
# print str("SETS OF NODES AND EDGES G.nodes(), G.edges()")
# print str("The set of nodes of G is ") + str(Gd.nodes())
# print str("The set of edges of G is ") + str(Gd.edges())
# print str(" ")
#
# print str("SET OF OUTGOING AND INCOMING NEIGHBORS OF A NODE G.neighbors(node), G.predecessors(node)")
# node = 4
# print str("The outgoing neighbors of node ") + str(node) + str(" are:") + str(Gd.neighbors(node))
# print str("The incoming neighbors of node ") + str(node) + str(" are:") + str(Gd.predecessors(node))
# print str(" ")
#
# print str("SET OF OUTGOING NEIGHBORS OF ALL NODES")
# for node in G.nodes():
#     print str("The outgoing neighbors of node ") + str(node) + str(Gd.neighbors(node))
# print str(" ")
#
# print str("SET OF INCOMING NEIGHBORS OF ALL NODES")
# for node in G.nodes():
#     print str("The incoming neighbors of node ") + str(node) + str(Gd.predecessors(node))
# print str(" ")
#
# print str("ADJACENCY MATRIX nx.adjacency_matrix(G)")
# A = nx.adjacency_matrix(Gd)
# print str("The adjacency matrix of G is: ")
# print(A.todense())
# print str(" ")
#
# plt.figure()
# nx.draw(Gd,pos=posd,with_labels=True,node_color='g',alpha=0.5)
#
# adjacency_matrix = nx.to_numpy_matrix(Gd)
# fig = plt.figure(figsize=(5, 5))
# plt.imshow(adjacency_matrix,cmap="Greys",interpolation="none")
#
# print str("THE CASE OF A DIRECTED SIMPLE GRAPH G")
# print str(" ")
#
# print str("OUT-DEGREE, IN-DEGREE AND TOTAL DEGREE OF A NODE G.out_degree(node), G.in_degree(node), G.degree(node)")
# node = 4
# print str("The out-degree of node ") + str(node) + str(" is: ") + str(Gd.out_degree(node))
# print str("The in-degree of node ") + str(node) + str(" is: ") + str(Gd.in_degree(node))
# print str("The total degree of node ") + str(node) + str(" is: ") + str(Gd.degree(node))
# print str(" ")
#
# print str("CHECK THAT G.out_degree(4) == len(G.neighbors(4)) and G.in_degree(4) == len(G.predecessors(4)")
# print "G.out_degree(4) == len(G.neighbors(4)) is", Gd.out_degree(4) == len(Gd.neighbors(4))
# print "G.in_degree(4) == len(G.predecessors(4)) is", Gd.in_degree(4) == len(Gd.predecessors(4))
# print str("CHECK THAT G.degree(4) == G.out_degree(4) + G.in_degree(4)")
# print "G.degree(4) == G.out_degree(4) + G.in_degree(4) is", Gd.degree(4) == Gd.out_degree(4) + Gd.in_degree(4)
# print str(" ")
#
# print str("OUT-DEGREES OF ALL NODES G.out_degree(node)")
# for node in G.nodes():
#     print str("The out-degree of node ") + str(node) + str(" is: ") + str(Gd.out_degree(node))
# print str(" ")
#
# print str("IN-DEGREES OF ALL NODES G.in_degree(node)")
# for node in G.nodes():
#     print str("The in-degree of node ") + str(node) + str(" is: ") + str(Gd.in_degree(node))
# print str(" ")
#
# print str("TOTAL DEGREES OF ALL NODES AS DICTIONARY G.degree()")
# print Gd.degree() #Το ίδιο με nx.degree(G)
# print str(" ")
#
# print str("CHECK THAT G.degree() == nx.degree(G)")
# print "G.degree() == nx.degree(G) is", Gd.degree() == nx.degree(Gd)
# print str(" ")
#
# node = 4
# Gn = nx.Graph()
# for v in Gd.neighbors(node):
#     Gn.add_edge(node,v)
#
# plt.figure()
# nx.draw(Gd,pos=posd,with_labels=True,node_size=500,width=3,alpha=0.5)
# nx.draw_networkx_edges(Gn,pos=posd,with_labels=False,edge_color='r',width=3)
#
# Gm = nx.Graph()
# for v in Gd.predecessors(node):
#     Gm.add_edge(node,v)
#
# plt.figure()
# nx.draw(Gd,pos=posd,with_labels=True,node_size=500,width=3,alpha=0.5)
# nx.draw_networkx_edges(Gm,pos=posd,with_labels=False,edge_color='b',width=3)
#
# ##### Ιστογράμματα κατανομής βαθμών κόμβων
#
# indegree_sequence=sorted(Gd.in_degree().values(),reverse=True)
# outdegree_sequence=sorted(Gd.out_degree().values(),reverse=True)
# dmax=max(indegree_sequence,outdegree_sequence)
#
# pla=[0.47,0.47,0.47,0.47]
# a=0.2
#
# plt.figure()
# plt.plot(indegree_sequence,'b-',marker='o')
# plt.plot(outdegree_sequence,'r-',marker='o')
# plt.ylabel("In[blue]/Out[red] Degree")
# plt.xlabel("Nodes")
# plt.axes(pla)
# plt.axis('off')
# nx.draw_networkx_nodes(Gd,pos=posd,node_size=20,node_color='b',alpha=a)
# nx.draw_networkx_edges(Gd,pos=posd,alpha=a)
#
# fig,ax=plt.subplots()
# ax.loglog(indegree_sequence,'b-',marker='o')
# ax.loglog(outdegree_sequence,'r-',marker='o')
# ax.set_ylabel("In[blue]/Out[red] Degree (log)")
# ax.set_xlabel("Nodes (log)")
# start,end=ax.get_xlim()
# t=2 #Ανα πόσα ticks να εκτυπώνεται ο αριθμός τους
# ax.xaxis.set_ticks(np.arange(start,end+2,t))
# ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
# plt.axes(pla)
# plt.axis('off')
# nx.draw_networkx_nodes(Gd,pos=posd,node_size=20,node_color='r',alpha=a)
# nx.draw_networkx_edges(Gd,pos=posd,alpha=a)



plt.show()

