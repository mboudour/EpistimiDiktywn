# -*- coding: utf-8 -*-
"""
    LAST UPDATE: 25 Νοεμβρίου 2014

    @author: Moses Boudourides
    """


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
from pylab import hist


# G = nx.erdos_renyi_graph(20,0.5)
# pos=nx.spring_layout(G)
#
# # ### O grafos tou HW tis Roxanis
# #
# # J=nx.Graph()
# # J.add_nodes_from([0,1,2,3,4,5,6,7,8,9,10,11])
# # J.add_edges_from([(0,1),(1,2),(0,3),(2,5),(1,4),(3,4),(4,5),(1,5),(3,6),(4,7),(5,8),(6,7),(7,8),(3,7),(5,7),(6,9),(7,10),(8,11),(9,10),(10,11),(6,10)])
# # pos={0:(-0.5,0),1:(0.5,0),2:(1.5,0),3:(0,1),4:(1,1),5:(2,1),6:(0.5,2),7:(1.5,2),8:(2.5,2),9:(1,3),10:(2,3),11:(3,3)}
# # F=nx.erdos_renyi_graph(6,0.7)
# # H=nx.bipartite_random_graph(12,6,0.12)
# # G=nx.Graph()
# # for node in J.nodes():
# #      G.add_node(node,bipartite=0)
# # for edge in J.edges():
# #      G.add_edge(edge[0],edge[1])
# # for edge in F.edges():
# #      G.add_edge(edge[0]+12,edge[1]+12)
# # for node in F.nodes():
# #      G.add_node(node+12,bipartite=1)
# # for edge in H.edges(data=True):
# #      G.add_edge(edge[0],edge[1])
# # posF=nx.spring_layout(F,k=0.35,iterations=20)
# # pos={0:(-0.5,0),1:(0.5,0),2:(1.5,0),3:(0,1),4:(1,1),5:(2,1),6:(0.5,2),7:(1.5,2),8:(2.5,2),9:(1,3),10:(2,3),11:(3,3),12:(0.5,0.3),13:(1,0.5),14:(1.5,0.8),15:(2.5,1.8),16:(3.5,1),17:(4.5,0.1)}
#
#
# deg=G.degree()
# deg_dic=[]
# for nd in deg:
#     if deg[nd]>3 and deg[nd]<8:
#         deg_dic.append(nd)
# node0 = random.choice(deg_dic)
#
# # top_set=set()
# # botom_set=set()
# # for i in pos:
# #     npos=pos[i]
# #     if G.node[i]['bipartite']==0:
# #          pos[i]=[npos[0],npos[1]+3]
# #          top_set.add(i)
# #     elif G.node[i]['bipartite']==1:
# #          pos[i]=[npos[0],npos[1]-3]
# #          botom_set.add(i)
# #
# # deg=G.degree(top_set)
# # deg_dic=[]
# # for nd in deg:
# #     if deg[nd]>1 and deg[nd]<8:
# #         deg_dic.append(nd)
# # node1 = random.choice(deg_dic) # To node1 einai o tyxaios kombos me bathmo >3
# # # print node1
# #
# #
# # deg=G.degree(botom_set)
# # deg_dic=[]
# # for nd in deg:
# #     if deg[nd]>1 and deg[nd]<8:
# #         deg_dic.append(nd)
# # node2 = random.choice(deg_dic) # To node2 einai o tyxaios kombos me bathmo >1
# # # print node2
#
# ##### ΓΕΙΤΝΙΑΣΗ-ΒΑΘΜΟΙ-ΚΑΤΑΝΟΜΕΣ ΜΗ ΚΑΤΕΥΘΥΝΟΜΕΝΩΝ ΑΠΛΩΝ ΓΡΑΦΩΝ
#
# ##### Γειτνίαση κόμβων μη κατευθυνόμενων γράφων
#
# ##### Σύνολα κόμβων και ακμών
# print str(" ")
#
# print str("THE CASE OF AN UNDIRECTED SIMPLE GRAPH G")
# print str(" ")
#
# print str("SETS OF NODES AND EDGES G.nodes(), G.edges()")
# print str("The set of nodes of G is ") + str(G.nodes())
# print str("The set of edges of G is ") + str(G.edges())
# print str(" ")
#
# ##### Γείτονες κάποιου κόμβου
#
# print str("TWO RANDOMLY SELECTED NODES WITH DEGREES IN (1,8)")
# node = node0
# print str("node0 = ") + str(node)
# print str("The degree of node0 is ") + str(G.degree(node))
# print str(" ")
# # node = node1
# # print str("node1 = ") + str(node)
# # print str("The degree of node1 is ") + str(G.degree(node))
# # print str(" ")
# #
# # node = node2
# # print str("node2 = ") + str(node)
# # print str("The degree of node2 is ") + str(G.degree(node))
# # print str(" ")
#
# print str("SET OF NEIGHBORS OF node0 G.neighbors(node)")
# node = node0
# print str("The neighbors of node ") + str(node) + str(" are:") + str(G.neighbors(node))
# print str(" ")
#
# # print str("SET OF NEIGHBORS OF node1 G.neighbors(node)")
# # node = node1
# # print str("The neighbors of node ") + str(node) + str(" are:") + str(G.neighbors(node))
# # print str(" ")
# #
# # print str("SET OF NEIGHBORS OF node2 G.neighbors(node)")
# # node = node2
# # print str("The neighbors of node ") + str(node) + str(" are:") + str(G.neighbors(node))
# # print str(" ")
#
# ##### Γείτονες όλων των κόμβων:
#
# print str("SET OF NEIGHBORS OF ALL NODES")
# for node in G.nodes():
#     print str("The neighbors of node ") + str(node) + str(" are:") + str(G.neighbors(node))
# print str(" ")
#
# ##### Πίνακας γειτνίασης
#
# print str("ADJACENCY MATRIX nx.adjacency_matrix(G)")
# A = nx.adjacency_matrix(G)
# print str("The adjacency matrix of G is: ")
# print(A.todense())
# print str(" ")
#
# ##### Σχεδιασμός plot του γράφου και του spy plot του πίνακα γειτνίασης
#
# plt.figure()
# nx.draw(G,pos=pos,with_labels=True,node_color='g',alpha=0.5)
#
# adjacency_matrix = nx.to_numpy_matrix(G)
# fig = plt.figure(figsize=(5, 5))
# plt.imshow(adjacency_matrix,cmap="Greys",interpolation="none")
#
# ##### Βαθμοί κόμβων μη κατευθυνόμενων γράφων
#
# print str("DEGREE OF node0 G.degree(node)")
# print str(" ")
#
# # node=node1
# # print str("DEGREE OF node1 G.degree(node)")
# # print str(" ")
# #
# # node=node2
# # print str("DEGREE OF node2 G.degree(node)")
# # print str(" ")
#
# node = node0
# print str("The neighbors of node ") + str(node) + str(" are:") + str(G.neighbors(node))
# print str(" ")
#
# # node = node1
# # print str("The neighbors of node ") + str(node) + str(" are:") + str(G.neighbors(node))
# # print str(" ")
# #
# # node = node2
# # print str("The neighbors of node ") + str(node) + str(" are:") + str(G.neighbors(node))
# # print str(" ")
#
# print str("The degree of node ") + str(node) + str(" is: ") + str(G.degree(node))
# print str(" ")
#
# # node = node1
# # print str("The degree of node ") + str(node) + str(" is: ") + str(G.degree(node))
# # print str(" ")
# #
# # node=node2
# # print str("The degree of node ") + str(node) + str(" is: ") + str(G.degree(node))
# # print str(" ")
#
# print str("CHECK THAT G.degree(node0) == len(G.neighbors(node0))")
# print "G.degree(node0) == len(G.neighbors(node0)) is", G.degree(node) == len(G.neighbors(node))
# print str(" ")
#
# # print str("CHECK THAT G.degree(node2) == len(G.neighbors(node2))")
# # print "G.degree(node2) == len(G.neighbors(node2)) is", G.degree(node) == len(G.neighbors(node))
# # print str(" ")
#
# print str("DEGREES OF ALL NODES G.degree(node)")
# for node in G.nodes():
#     print str("The degree of node ") + str(node) + str(" is: ") + str(G.degree(node))
# print str(" ")
#
# print str("DEGREES OF ALL NODES AS DICTIONARY G.degree()")
# print G.degree() #Το ίδιο με nx.degree(G)
# print str(" ")
#
# print str("CHECK THAT G.degree() == nx.degree(G)")
# print "G.degree() == nx.degree(G) is", G.degree() == nx.degree(G)
# print str(" ")
#
# print str("SORTED DEGREE SEQUENCE sorted(set(G.degree().values()))")
# print str("The sorted degree sequence of the graph ") + str(" is: ") + str(sorted(set(G.degree().values())))
# print str(" ")
#
# #### Σχεδιασμός Γράφου (όπου διακρίνεται ο κόμβος node0 και οι συνδέσεις του)
#
# node = node0
# Gn = nx.Graph()
# for v in G.neighbors(node0):
#     Gn.add_edge(node0,v)
# neigh0=G.neighbors(node0)
# #neigh0.append(node0)
# neigh00=[node0]
# neigh1 = set(G.nodes()) - set(neigh0) - set(neigh00)
#
# # node = node1
# # Gn1 = nx.Graph()
# # for v in G.neighbors(node1):
# #     Gn1.add_edge(node1,v)
# # neigh01=G.neighbors(node1)
# # #neigh0.append(node0)
# # neigh001=[node1]
# # neigh11 = set(G.nodes()) - set(neigh01) - set(neigh001)
# #
# # node = node2
# # Gn2 = nx.Graph()
# # for v in G.neighbors(node2):
# #     Gn2.add_edge(node2,v)
# # neigh02=G.neighbors(node2)
# # #neigh0.append(node0)
# # neigh002=[node2]
# # neigh12 = set(G.nodes()) - set(neigh02) - set(neigh002)
#
#
# plt.figure()
# nx.draw(G,pos=pos,with_labels=True,nodelist=neigh00,node_size=500,node_color='r',alpha=0.5)
# nx.draw(G,pos=pos,with_labels=True,nodelist=neigh0,node_size=500,node_color='r',alpha=0.5)
# nx.draw(G,pos=pos,with_labels=True,nodelist=neigh1,node_size=500,node_color='g',alpha=0.5)
# nx.draw_networkx_edges(Gn,pos=pos,with_labels=False,edge_color='r',width=6.0,alpha=0.5)
#
# # nx.draw(G,pos=pos,with_labels=True,nodelist=neigh001,node_size=500,node_color='r',alpha=0.5)
# # nx.draw(G,pos=pos,with_labels=True,nodelist=neigh01,node_size=500,node_color='r',alpha=0.5)
# # nx.draw(G,pos=pos,with_labels=True,nodelist=neigh11,node_size=500,node_color='g',alpha=0.5)
# # nx.draw(G,pos=pos,with_labels=True,nodelist=neigh002,node_size=500,node_color='r',alpha=0.5)
# # nx.draw(G,pos=pos,with_labels=True,nodelist=neigh02,node_size=500,node_color='r',alpha=0.5)
# # nx.draw(G,pos=pos,with_labels=True,nodelist=neigh12,node_size=500,node_color='g',alpha=0.5)
# # nx.draw_networkx_edges(Gn1,pos=pos,with_labels=False,edge_color='r',width=6.0,alpha=0.5)
# # nx.draw_networkx_edges(Gn2,pos=pos,with_labels=False,edge_color='r',width=6.0,alpha=0.5)
#
# ###### ΡΑΒΔΟΓΡΑΜΜΑΤΑ ΚΑΙ ΙΣΤΟΓΡΑΜΜΑΤΑ ΓΙΑ ΣΧΕΤΙΚΑ  Μ Ι Κ Ρ Ο Υ Σ  ΓΡΑΦΟΥΣ ΜΟΝΟ!!!!!!
#
# ##### Ραβδόγραμμα βαθμών κόμβων
#
# deg=G.degree()
# deg_dic=dict()
# for nd in deg:
#     if deg[nd] not in deg_dic:
#         deg_dic[deg[nd]]=[nd]
#     else:
#         deg_dic[deg[nd]].append(nd)
# deg_lis=[]
# nd_lis=[]
# for de in sorted(deg_dic.keys(),reverse=True):
#     for nn in deg_dic[de]:
#         deg_lis.append(de)
#         nd_lis.append(nn)
#
# index = np.arange(len(nd_lis))
# bar_width = 1
# # bar_width = 0.35
#
# pla=[0.47,0.47,0.47,0.47]
# a=0.3
#
# plt.figure()
# plt.bar(index, deg_lis, bar_width,color='g') #,label='Degree'
# plt.ylabel("Degree")
# plt.xlabel("Nodes")
# plt.title('Bar Plot of Degrees of Nodes')
# plt.xticks(index + bar_width/2, nd_lis) #Την εντολή αυτή την βάζετε ΜΟΝΟ όταν έχετε σχετικά μικρό αριθμό κόμβων
#
# ##### Τις παρακάτω εντολές τις βάζετε αν θέλετε να βγαίνει ο γράφος στην πάνω δεξια γωνία - ΜΟΝΟ για σχετικά μικρούς γράφους
#
# plt.axes(pla)
# plt.axis('off')
# nx.draw_networkx_nodes(G,pos=pos,node_size=400,node_color='g',alpha=a)
# labels={}
# for v in G.nodes():
#     labels[v]=v
# nx.draw_networkx_labels(G,pos,labels,font_size=12)
# nx.draw_networkx_edges(G,pos=pos,alpha=a)
#
# ##### Ιστογράμματα κατανομής βαθμών κόμβων
#
# deg = G.degree()
#
# pla=[0.47,0.47,0.47,0.47]
# a=0.3
#
# plt.figure()
# plt.xlabel("Degree")
# hist(deg.values(),bins=len(set(G.degree().values())),color='g')
# # histtype='step', histtype='stepfilled'
# #plt.gca().set_xscale("log")
# plt.ylabel("Number of nodes")
# plt.title('Histogram of Degrees of Nodes')
# # hist(deg.values(),bins=len(set(G.degree().values())),normed=True,color='g')
# # plt.ylabel("Percentage of nodes")
# # plt.title('Histogram of Degrees of Nodes (Percentages)')
#
# plt.axes(pla)
# plt.axis('off')
#
# nx.draw_networkx_nodes(G,pos=pos,node_size=400,node_color='g',alpha=a)
# nx.draw_networkx_edges(G,pos=pos,alpha=a)



###### ΡΑΒΔΟΓΡΑΜΜΑΤΑ ΚΑΙ ΙΣΤΟΓΡΑΜΜΑΤΑ ΓΙΑ ΣΧΕΤΙΚΑ  Μ Ε Γ Α Λ Ο Υ Σ  ΓΡΑΦΟΥΣ!!!!!

G = nx.erdos_renyi_graph(5000,0.25)
# G = nx.barabasi_albert_graph(5000,3)
pos=nx.spring_layout(G,k=0.15,iterations=10)


deg=G.degree()

deg_dic=[]
m = 8
while True:
    for nd in deg:
        if deg[nd] >=3 and deg[nd] < m:
            deg_dic.append(nd)
    if len(deg_dic)==0:
        m=m+1
    else:
        break

deg_lis=[]
for de in sorted(deg_dic,reverse=True):
        deg_lis.append(de)

# plt.figure(facecolor='w')
# plt.axis('off')
# nx.draw_networkx(G,pos=pos,with_labels=False,node_size=50,node_color='g',alpha=0.25)
# # nx.draw_networkx_edges(Gn,pos=pos,with_labels=False,edge_color='r',width=6.0,alpha=0.5)
# # nx.draw(G0,pos=pos,with_labels=False,node_size=50)
# # nx.draw(Gn0,pos=pos,with_labels=False,node_size=50,node_color='r',alpha=0.5)
# # nx.draw(Gn1,pos=pos,with_labels=False,node_size=50,node_color='g',alpha=0.5)

##### Ιστογράμματα κατανομής βαθμών κόμβων

# plt.figure()
#
# plt.xlabel("Degree")
# hist(deg.values(),bins=len(set(G.degree().values())),color='g')
# # histtype='step',
# plt.ylabel("Number of nodes")
# plt.title('Histogram of Degrees of Nodes')

plt.figure()

plt.xlabel("Degree")
hist(deg.values(),bins=len(set(G.degree().values())),normed=True,color='g')
plt.ylabel("Percentage of nodes")
plt.title('Histogram of Degrees of Nodes (Percentages)')

### Σχεδιασμός σε Λογαριθμικές Κλίμακες

mindd=1000
for ddd in G.degree().values():
    if ddd>0 and ddd<mindd:
        mindd=ddd

# plt.figure()
#
# plt.xlabel("Degree (log)")
# plt.gca().set_xlim([mindd,max(set(G.degree().values()))])
# plt.gca().set_xscale("log")
# hist(deg.values(),bins=len(set(G.degree().values())),color='g',log=True)
# # histtype='step',
# plt.ylabel("Number of nodes (log)")
# plt.title('Histogram of Degrees of Nodes (log)')
#
plt.figure()

hist(deg.values(),bins=len(set(G.degree().values())),normed=True,color='g',log=True)
plt.xlabel("Degree (log)")
plt.gca().set_xlim([mindd,max(set(G.degree().values()))])
plt.gca().set_xscale("log")
plt.ylabel("Percentage of nodes (log)")
plt.title('Histogram of Degrees of Nodes (Percentages) (log)')

plt.show()