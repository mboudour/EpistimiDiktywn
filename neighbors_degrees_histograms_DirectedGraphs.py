# -*- coding: utf-8 -*-
"""
    LAST UPDATE: 17 Νοεμβρίου 2014

    @author: Moses Boudourides
    """


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
from pylab import hist
import colorBar





n = 20
G = nx.erdos_renyi_graph(n,0.15,directed=True)
pos=nx.spring_layout(G)


##### ΤΑ ΑΜΕΣΩΣ ΠΑΡΑΚΑΤΩ ΝΑ ΜΗΝ ΣΒΗΣΘΟΥΝ!!!

odeg=G.out_degree()
odeg_dic=dict()
for nd in odeg:
    if odeg[nd] not in odeg_dic:
        odeg_dic[odeg[nd]]=[nd]
    else:
        odeg_dic[odeg[nd]].append(nd)
odeg_lis=[]
ond_lis=[]
for de in sorted(odeg_dic.keys(),reverse=True):
    for nn in odeg_dic[de]:
        odeg_lis.append(de)
        ond_lis.append(nn)

ideg=G.in_degree()
ideg_dic=dict()
for nd in ideg:
    if ideg[nd] not in ideg_dic:
        ideg_dic[ideg[nd]]=[nd]
    else:
        ideg_dic[ideg[nd]].append(nd)
ideg_lis=[]
ind_lis=[]
for de in sorted(ideg_dic.keys(),reverse=True):
    for nn in ideg_dic[de]:
        ideg_lis.append(de)
        ind_lis.append(nn)


# ##### ΓΕΙΤΝΙΑΣΗ-ΒΑΘΜΟΙ-ΚΑΤΑΝΟΜΕΣ ΚΑΤΕΥΘΥΝΟΜΕΝΩΝ ΑΠΛΩΝ ΓΡΑΦΩΝ
#
# # odeg=G.out_degree()
# deg_dic=[]
# m=8
# while True:
#     for nd in odeg:
#         if odeg[nd]>3 and odeg[nd]<m:
#             deg_dic.append(nd)
#     if len(deg_dic)>0:
#         break
#     else:
#         m+=1
# node0 = random.choice(deg_dic)
#
# ##### Γειτνίαση κόμβων κατευθυνόμενων γράφων
#
# ##### Σύνολα κόμβων και ακμών
# print str(" ")
#
# print str("THE CASE OF A DIRECTED SIMPLE GRAPH G")
# print str(" ")
#
# print str("SETS OF NODES AND EDGES G.nodes(), G.edges()")
# print str("The set of nodes of G is ") + str(G.nodes())
# print str("The set of edges of G is ") + str(G.edges())
# print str(" ")
#
# ##### Εξερχόμενοι-Εισερχόμενοι Γείτονες κάποιου κόμβου
#
# print str("A RANDOMLY SELECTED NODE WITH OUT-DEGREE IN (3,8)")
# node = node0
# print str("node0 = ") + str(node)
# print str("The out-degree of node0 is ") + str(G.out_degree(node))
# print str("The in-degree of node0 is ") + str(G.in_degree(node))
# print str(" ")
#
# print str("SET OF OUTGOING NEIGHBORS OF node0 G.neighbors(node)")
# node = node0
# print str("The outgoing neighbors of node ") + str(node) + str(" are:") + str(G.neighbors(node))
# print str(" ")
#
# print str("SET OF INCOMING NEIGHBORS OF node0 G.predecessors(node)")
# print str("The incoming neighbors of node ") + str(node) + str(" are:") + str(G.predecessors(node))
# print str(" ")
#
# ##### Εξερχόμενοι-Εισερχόμενοι Γείτονες όλων των κόμβων:
#
# print str("SET OF OUTGOING NEIGHBORS OF ALL NODES")
# for node in G.nodes():
#     print str("The outgoing neighbors of node ") + str(node) + str(" are:") + str(G.neighbors(node))
# print str(" ")
#
# print str("SET OF INCOMING NEIGHBORS OF ALL NODES")
# for node in G.nodes():
#     print str("The incoming neighbors of node ") + str(node) + str(" are:") + str(G.predecessors(node))
# print str(" ")
#
# ##### Πίνακας γειτνίασης
#
# print str("ADJACENCY MATRIX nx.adjacency_matrix(G)")
# A = nx.adjacency_matrix(G)
# print str("The adjacency matrix of G is: ")
# #print(A.todense())
# print str(" ")
#
# ##### Σχεδιασμός plot του γράφου και του spy plot του πίνακα γειτνίασης
#
# #### FIGURE 1
# plt.figure()
# nx.draw(G,pos=pos,with_labels=True,node_color='g',alpha=0.5)
#
# adjacency_matrix = nx.to_numpy_matrix(G)
#
# #### FIGURE 2
# fig = plt.figure(figsize=(5, 5))
# plt.imshow(adjacency_matrix,cmap="Greys",interpolation="none")
#
# ##### Εξερχόμενοι-Εισερχόμενοι-Ολικοί Βαθμοί κόμβων μη κατευθυνόμενων γράφων
#
# ##### Εξερχόμενοι Βαθμοί κόμβων μη κατευθυνόμενων γράφων
#
# print str("OUT-DEGREE OF node0 G.out_degree(node)")
# print str(" ")
#
# node = node0
#
# print str("The outgoing neighbors of node ") + str(node) + str(" are:") + str(G.neighbors(node))
# print str(" ")
#
# print str("The out-degree of node ") + str(node) + str(" is: ") + str(G.out_degree(node))
# print str(" ")
#
# print str("CHECK THAT G.out_degree(node) == len(G.neighbors(node))")
# print "G.out_degree(node) == len(G.neighbors(node)) is", G.out_degree(node) == len(G.neighbors(node))
# print str(" ")
#
# ##### Εισερχόμενοι Βαθμοί κόμβων μη κατευθυνόμενων γράφων
#
# print str("IN-DEGREE OF node0 G.in_degree(node)")
# print str("The in-degree of node ") + str(node) + str(" is: ") + str(G.in_degree(node))
# print str(" ")
#
# print str("CHECK THAT G.out_degree(node) == len(G.neighbors(node)) and G.in_degree(node) == len(G.predecessors(node)")
# print "G.in_degree(node) == len(G.predecessors(node)) is", G.in_degree(node) == len(G.predecessors(node))
# print str(" ")
#
# ##### Ολικοί Βαθμοί κόμβων μη κατευθυνόμενων γράφων
#
# print str("TOTAL DEGREE OF node0 G.degree(node)")
# print str("The total degree of node ") + str(node) + str(" is: ") + str(G.degree(node))
# print str(" ")
#
# print str("CHECK THAT G.degree(node) == G.out_degree(node) + G.in_degree(node)")
# print "G.degree(node) == G.out_degree(node) + G.in_degree(node) is", G.degree(node) == G.out_degree(node) + G.in_degree(node)
# print str(" ")
#
# print str("OUT-DEGREES OF ALL NODES G.out_degree(node)")
# for node in G.nodes():
#     print str("The out-degree of node ") + str(node) + str(" is: ") + str(G.out_degree(node))
# print str(" ")
#
# print str("IN-DEGREES OF ALL NODES G.in_degree(node)")
# for node in G.nodes():
#     print str("The in-degree of node ") + str(node) + str(" is: ") + str(G.in_degree(node))
# print str(" ")
#
# print str("OUT-DEGREES OF ALL NODES AS DICTIONARY G.out_degree()")
# print G.out_degree()
# print str(" ")
#
# print str("IN-DEGREES OF ALL NODES AS DICTIONARY G.in_degree()")
# print G.in_degree()
# print str(" ")
#
# print str("TOTAL DEGREES OF ALL NODES AS DICTIONARY G.degree()")
# print G.degree()
# print str(" ")
#
# print str("CHECK THAT G.degree() == nx.degree(G)")
# print "G.degree() == nx.degree(G) is", G.degree() == nx.degree(G)
# print str(" ")
#
# print str("SORTED OUT-DEGREE SEQUENCE sorted(set(G.out_degree().values()))")
# print str("The sorted out-degree sequence of the graph ") + str(" is: ") + str(sorted(set(G.out_degree().values())))
# print str(" ")
#
# print str("SORTED IN-DEGREE SEQUENCE sorted(set(G.in_degree().values()))")
# print str("The sorted in-degree sequence of the graph ") + str(" is: ") + str(sorted(set(G.in_degree().values())))
# print str(" ")
#
# print str("SORTED TOTAL DEGREE SEQUENCE sorted(set(G.degree().values()))")
# print str("The sorted total degree sequence of the graph ") + str(" is: ") + str(sorted(set(G.degree().values())))
# print str(" ")
#
# #### Σχεδιασμός Γράφου (όπου διακρίνεται ο κόμβος node0 και οι συνδέσεις του)
#
# node = node0
# Gno = nx.Graph()
# for v in G.neighbors(node0):
#     Gno.add_edge(node0,v)
# oneigh0=G.neighbors(node0)
# neigh00=[node0]
# Gni = nx.Graph()
# for v in G.predecessors(node0):
#     Gni.add_edge(node0,v)
# ineigh0=G.predecessors(node0)
# neigh1 = set(G.nodes()) - set(oneigh0) - set(ineigh0) - set(neigh00)
#
# #### FIGURE 3
# plt.figure()
# nx.draw(G,pos=pos,with_labels=True,nodelist=neigh00,node_size=500,node_color='r',alpha=0.5)
# nx.draw(G,pos=pos,with_labels=True,nodelist=oneigh0,node_size=500,node_color='r',alpha=0.5)
# nx.draw(G,pos=pos,with_labels=True,nodelist=ineigh0,node_size=500,node_color='r',alpha=0.5)
# nx.draw(G,pos=pos,with_labels=True,nodelist=neigh1,node_size=500,node_color='g',alpha=0.5)
# nx.draw_networkx_edges(Gno,pos=pos,with_labels=False,edge_color='r',width=6.0,alpha=0.5)
# nx.draw_networkx_edges(Gni,pos=pos,with_labels=False,edge_color='b',width=6.0,alpha=0.5)

# ###### ΡΑΒΔΟΓΡΑΜΜΑΤΑ ΚΑΙ ΙΣΤΟΓΡΑΜΜΑΤΑ ΓΙΑ ΣΧΕΤΙΚΑ  Μ Ι Κ Ρ Ο Υ Σ  ΓΡΑΦΟΥΣ ΜΟΝΟ!!!!!!
#
# ##### Ραβδόγραμμα εξερχόμενων βαθμών κόμβων
#
# odeg=G.out_degree()
# odeg_dic=dict()
# for nd in odeg:
#     if odeg[nd] not in odeg_dic:
#         odeg_dic[odeg[nd]]=[nd]
#     else:
#         odeg_dic[odeg[nd]].append(nd)
# odeg_lis=[]
# ond_lis=[]
# for de in sorted(odeg_dic.keys(),reverse=True):
#     for nn in odeg_dic[de]:
#         odeg_lis.append(de)
#         ond_lis.append(nn)
#
# index = np.arange(len(ond_lis))
# bar_width = 1
# # bar_width = 0.35
#
# pla=[0.47,0.47,0.47,0.47]
# a=0.3
#
# #### FIGURE 4
# plt.figure()
# plt.bar(index, odeg_lis, bar_width,color='r',label='Out-Degree')
# plt.ylabel("Out-Degree")
# plt.xlabel("Nodes")
# plt.title('Bar Plot of Out-Degrees of Nodes')
# plt.xticks(index + bar_width/2, ond_lis) #Την εντολή αυτή την βάζετε ΜΟΝΟ όταν έχετε σχετικά μικρό αριθμό κόμβων
#
# ##### Τις παρακάτω εντολές τις βάζετε αν θέλετε να βγαίνει ο γράφος στην πάνω δεξια γωνία - ΜΟΝΟ για σχετικά μικρούς γράφους
# plt.axes(pla)
# plt.axis('off')
# nx.draw_networkx_nodes(G,pos=pos,node_size=400,node_color='r',alpha=a)
# labels={}
# for v in G.nodes():
#     labels[v]=v
#
# nx.draw_networkx_labels(G,pos,labels,font_size=12)
# nx.draw_networkx_edges(G,pos=pos,alpha=a)
#
# # ##### Ραβδόγραμμα εισερχόμενων βαθμών κόμβων
#
# ideg=G.in_degree()
# ideg_dic=dict()
# for nd in ideg:
#     if ideg[nd] not in ideg_dic:
#         ideg_dic[ideg[nd]]=[nd]
#     else:
#         ideg_dic[ideg[nd]].append(nd)
# ideg_lis=[]
# ind_lis=[]
# for de in sorted(ideg_dic.keys(),reverse=True):
#     for nn in ideg_dic[de]:
#         ideg_lis.append(de)
#         ind_lis.append(nn)
#
# index = np.arange(len(ind_lis))
# bar_width = 1
# # bar_width = 0.35
#
#
# #### FIGURE 5
# plt.figure()
# plt.bar(index, ideg_lis, bar_width,color='b',label='In-Degree')
# plt.ylabel("In-Degree")
# plt.xlabel("Nodes")
# plt.title('Bar Plot of In-Degrees of Nodes')
# plt.xticks(index + bar_width/2, ind_lis) #Την εντολή αυτή την βάζετε ΜΟΝΟ όταν έχετε σχετικά μικρό αριθμό κόμβων
#
# ##### Τις παρακάτω εντολές τις βάζετε αν θέλετε να βγαίνει ο γράφος στην πάνω δεξια γωνία - ΜΟΝΟ για σχετικά μικρούς γράφους
# plt.axes(pla)
# plt.axis('off')
# nx.draw_networkx_nodes(G,pos=pos,node_size=400,node_color='b',alpha=a)
# labels={}
# for v in G.nodes():
#     labels[v]=v
#
# nx.draw_networkx_labels(G,pos,labels,font_size=12)
# nx.draw_networkx_edges(G,pos=pos,alpha=a)
#
# ##### Ιστογράμματα κατανομής εξερχόμενων βαθμών κόμβων
#
# # odeg = G.out_degree()
# #
# # pla=[0.47,0.47,0.47,0.47]
# a=0.3
#
# #### FIGURE 6
# plt.figure()
# plt.xlabel("Out-Degree")
# hist(odeg.values(),bins=len(set(G.out_degree().values())),color='r')
# # histtype='step',
# plt.ylabel("Number of nodes")
# plt.title('Histogram of Out-Degrees of Nodes')
# # hist(odeg.values(),bins=len(set(G.out_degree().values())),normed=True,color='g')
# # plt.ylabel("Percentage of nodes")
# # plt.title('Histogram of Out-Degrees of Nodes (Percentages)')
#
# ##### Τις παρακάτω εντολές τις βάζετε αν θέλετε να βγαίνει ο γράφος στην πάνω δεξια γωνία - ΜΟΝΟ για σχετικά μικρούς γράφους
# plt.axes(pla)
# plt.axis('off')
#
# nx.draw_networkx_nodes(G,pos=pos,node_size=400,node_color='g',alpha=a)
# nx.draw_networkx_edges(G,pos=pos,alpha=a)
#
# ##### Ιστογράμματα κατανομής εισερχόμενων βαθμών κόμβων
#
# # ideg = G.in_degree()
# #
# # pla=[0.47,0.47,0.47,0.47]
# # a=0.3
#
# #### FIGURE 7
# plt.figure()
# plt.xlabel("In-Degree")
# hist(ideg.values(),bins=len(set(G.in_degree().values())),color='b')
# # histtype='step',
# plt.ylabel("Number of nodes")
# plt.title('Histogram of In-Degrees of Nodes')
# # hist(ideg.values(),bins=len(set(G.in_degree().values())),normed=True,color='g')
# # plt.ylabel("Percentage of nodes")
# # plt.title('Histogram of In-Degrees of Nodes (Percentages)')
#
# ##### Τις παρακάτω εντολές τις βάζετε αν θέλετε να βγαίνει ο γράφος στην πάνω δεξια γωνία - ΜΟΝΟ για σχετικά μικρούς γράφους
# plt.axes(pla)
# plt.axis('off')
#
# nx.draw_networkx_nodes(G,pos=pos,node_size=400,node_color='g',alpha=a)
# nx.draw_networkx_edges(G,pos=pos,alpha=a)
#
# #print '7'
#
#
#
# ##### Δισδιάστατα ιστογράμματα κατανομής εξερχόμενων και εισερχόμενων βαθμών κόμβων
#
# lisa=[]
# moutd= min(odeg_dic.keys())
# Moutd = max(odeg_dic.keys())
# mind = min(ideg_dic.keys())
# Mind = max(ideg_dic.keys())
# mii=[mind,Mind]
# moo=[moutd,Moutd]
# m0=[min(mind,moutd),max(Mind,Moutd)]
# print 'mii =', mii
# print 'moo =', moo
# print 'm0 =', m0
#
# mmdd=max(max(ideg_dic.keys()),max(odeg_dic.keys()))
# for ode in range(max(max(ideg_dic.keys()),max(odeg_dic.keys()))+1):
#     lis=[]
#     for ide in range(max(max(ideg_dic.keys()),max(odeg_dic.keys()))+1):
#         mi=0
#         mo=0
#         ck=set()
#         if ide in ideg_dic and ode in odeg_dic:
#             ck=set(ideg_dic[ide]).intersection(set(odeg_dic[ode]))
#             mi=len(ideg_dic[ide])#*1./n
#             mo=len(odeg_dic[ode])
#         lis.append((len(ck))*1./n)
#     lisa.append(lis)
#
#
# #fig, ax =plt.subplots()
#
# #num_bins=int(n/3.)
# #inli,bins,pathc=plt.hist(sorted(ideg_lis),num_bins)
# #mindd=1000
# #for ddd in ideg_lis:
#     #if ddd>0 and ddd<mindd:
#         #mindd=ddd
# #plt.gca().set_xlim([ddd,max(ideg_lis)])
# #plt.gca().set_xscale('log')#.set_xlim([min(indeg_lis),max(indeg_lis)])
# #binsn=bins[:-1]+(bins[1]-bins[0])/2.
# ## plt.plot(binsn,inli,'ro-')
# #print '8'
# #plt.show()
# #print aaaa
# arra=np.array(lisa)
#
# li=[]
#
# my_cmap=colorBar.cororBar()
#
#
# #### FIGURE 8
# plt.figure()
# colorBar.drawScatInOut(arra,my_cmap,None,li)
#
# #### Figure 8.1
# plt.figure()
# colorBar.drawScatInOut(arra,my_cmap,None,li,mii,moo)  # m0,m0


###### ΡΑΒΔΟΓΡΑΜΜΑΤΑ ΚΑΙ ΙΣΤΟΓΡΑΜΜΑΤΑ ΓΙΑ ΣΧΕΤΙΚΑ  Μ Ε Γ Α Λ Ο Υ Σ  ΓΡΑΦΟΥΣ!!!!!

n = 2000
p = 0.1
G = nx.erdos_renyi_graph(n,p,directed=True)
pos=nx.spring_layout(G,k=0.15,iterations=15)


odeg=G.out_degree()
odeg_dic=dict()
for nd in odeg:
    if odeg[nd] not in odeg_dic:
        odeg_dic[odeg[nd]]=[nd]
    else:
        odeg_dic[odeg[nd]].append(nd)
odeg_lis=[]
ond_lis=[]
for de in sorted(odeg_dic.keys(),reverse=True):
    for nn in odeg_dic[de]:
        odeg_lis.append(de)
        ond_lis.append(nn)

ideg=G.in_degree()
ideg_dic=dict()
for nd in ideg:
    if ideg[nd] not in ideg_dic:
        ideg_dic[ideg[nd]]=[nd]
    else:
        ideg_dic[ideg[nd]].append(nd)
ideg_lis=[]
ind_lis=[]
for de in sorted(ideg_dic.keys(),reverse=True):
    for nn in ideg_dic[de]:
        ideg_lis.append(de)
        ind_lis.append(nn)


# print str("SORTED OUT-DEGREE SEQUENCE sorted(set(G.out_degree().values()))")
# print str("The sorted out-degree sequence of the graph ") + str(" is: ") + str(sorted(set(G.out_degree().values())))
# print str(" ")
#
# print str("SORTED IN-DEGREE SEQUENCE sorted(set(G.in_degree().values()))")
# print str("The sorted in-degree sequence of the graph ") + str(" is: ") + str(sorted(set(G.in_degree().values())))
# print str(" ")
#
# print str("SORTED TOTAL DEGREE SEQUENCE sorted(set(G.degree().values()))")
# print str("The sorted total degree sequence of the graph ") + str(" is: ") + str(sorted(set(G.degree().values())))
# print str(" ")


# #### FIGURE 9
# plt.figure(facecolor='w')
# plt.axis('off')
# nx.draw_networkx(G,pos=pos,with_labels=False,node_size=50,node_color='g',alpha=0.25)


# odeg=G.out_degree()
#
# deg_dic=[]
# m = 8
# while True:
#     for nd in odeg:
#         if odeg[nd] >=3 and odeg[nd] < m:
#             deg_dic.append(nd)
#     if len(deg_dic)==0:
#         m=m+1
#     else:
#         break
# node0 = random.choice(deg_dic)

##### Ιστογράμματα κατανομής εξερχόμενων-εισερχόμενων βαθμών κόμβων

#### FIGURE 10
plt.figure()

plt.xlabel("Out-Degree")
hist(odeg.values(),bins=len(set(G.out_degree().values())),color='r')
# histtype='step',
plt.ylabel("Number of nodes")
plt.title('Histogram of Out-Degrees of Nodes')
# hist(odeg.values(),bins=len(set(G.out_degree().values())),normed=True,color='g')
# plt.ylabel("Percentage of nodes")
# plt.title('Histogram of Out-Degrees of Nodes (Percentages)')

#### FIGURE 11
plt.figure()

plt.xlabel("In-Degree")
hist(ideg.values(),bins=len(set(G.in_degree().values())),color='b')
# histtype='step',
plt.ylabel("Number of nodes")
plt.title('Histogram of In-Degrees of Nodes')
# hist(ideg.values(),bins=len(set(G.in_degree().values())),normed=True,color='g')
# plt.ylabel("Percentage of nodes")
# plt.title('Histogram of In-Degrees of Nodes (Percentages)')

### Σχεδιασμός σε Λογαριθμικές Κλίμακες

minddo=1000
for ddd in G.out_degree().values():
    if ddd>0 and ddd<minddo:
        minddo=ddd
minddi=1000
for ddd in G.in_degree().values():
    if ddd>0 and ddd<minddi:
        minddi=ddd

#### FIGURE 12
plt.figure()

plt.xlabel("Out-Degree (log)")
plt.gca().set_xlim([minddo,max(set(G.out_degree().values()))])
plt.gca().set_xscale("log")
hist(odeg.values(),bins=len(set(G.out_degree().values())),color='r',log=True)
# histtype='step',
plt.ylabel("Number of nodes (log)")
plt.title('Histogram of Out-Degrees of Nodes (log)')
# hist(deg.values(),bins=len(set(G.out_degree().values())),normed=True,color='r',log=True)
# plt.ylabel("Percentage of nodes (log)")
# plt.title('Histogram of Out-Degrees of Nodes (Percentages) (log)')

#### FIGURE 13
plt.figure()

plt.xlabel("In-Degree (log)")
plt.gca().set_xlim([minddi,max(set(G.in_degree().values()))])
plt.gca().set_xscale("log")
hist(ideg.values(),bins=len(set(G.in_degree().values())),color='b',log=True)
# histtype='step',
plt.ylabel("Number of nodes (log)")
plt.title('Histogram of In-Degrees of Nodes (log)')
# hist(deg.values(),bins=len(set(G.in_degree().values())),normed=True,color='g',log=True)
# plt.ylabel("Percentage of nodes (log)")
# plt.title('Histogram of In-Degrees of Nodes (Percentages) (log)')


##### Δισδιάστατα ιστογράμματα κατανομής εξερχόμενων και εισερχόμενων βαθμών κόμβων

lisa=[]
moutd= min(odeg_dic.keys())
Moutd = max(odeg_dic.keys())
mind = min(ideg_dic.keys())
Mind = max(ideg_dic.keys())
mii=[mind,Mind]
moo=[moutd,Moutd]
m0=[min(mind,moutd),max(Mind,Moutd)]

mmdd=max(max(ideg_dic.keys()),max(odeg_dic.keys()))
for ode in range(max(max(ideg_dic.keys()),max(odeg_dic.keys()))+1):
    lis=[]
    for ide in range(max(max(ideg_dic.keys()),max(odeg_dic.keys()))+1):
        mi=0
        mo=0
        ck=set()
        if ide in ideg_dic and ode in odeg_dic:
            ck=set(ideg_dic[ide]).intersection(set(odeg_dic[ode]))
            mi=len(ideg_dic[ide])#*1./n
            mo=len(odeg_dic[ode])
        lis.append((len(ck))*1./n)
    lisa.append(lis)


#fig, ax =plt.subplots()

#num_bins=int(n/3.)
#inli,bins,pathc=plt.hist(sorted(ideg_lis),num_bins)
#mindd=1000
#for ddd in ideg_lis:
    #if ddd>0 and ddd<mindd:
        #mindd=ddd
#plt.gca().set_xlim([ddd,max(ideg_lis)])
#plt.gca().set_xscale('log')#.set_xlim([min(indeg_lis),max(indeg_lis)])
#binsn=bins[:-1]+(bins[1]-bins[0])/2.
## plt.plot(binsn,inli,'ro-')
#print '8'
#plt.show()
#print aaaa
arra=np.array(lisa)

li=[]

my_cmap=colorBar.cororBar()


#### FIGURE 8
# plt.figure()
# colorBar.drawScatInOut(arra,my_cmap,None,li)



#### Figure 8.1
plt.figure()
colorBar.drawScatInOut(arra,my_cmap,None,li,mii,moo) #m0

plt.show()
