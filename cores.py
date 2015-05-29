# -*- coding: utf-8 -*-
"""
    LAST UPDATE: 20 Δεκεμβρίου 2014

    @author: Moses Boudourides & Sergios Lenis
    """


import networkx as nx
import matplotlib.pyplot as plt
import random
from networkx.algorithms import bipartite
import os

# try:
#     from networkx import graphviz_layout
#     layout=nx.graphviz_layout
# except ImportError:
#     print("PyGraphviz not found; drawing with spring layout; will be slow.")
#     layout=nx.spring_layout




#### ΠΥΡΗΝΕΣ ΣΕ ΓΡΑΦΟΥΣ

# G=nx.karate_club_graph()
G=nx.read_gml('lesmiserables.gml')
G.name='lesmiserables'

# print G.nodes()
# print 'e'
# print G.edges()
# print aaa

# G=nx.Graph()
# G.add_edges_from([(0,1),(1,2),(2,0),(3,4)])
# G.add_node(5)
# pos={0:(0,0),1:(0,1),2:(0.5,1),3:(0.5,0),4:(1,0),5:(0.75,0.5)}

# G = nx.gnp_random_graph(6,0.41)
# G = nx.erdos_renyi_graph(20,0.1)
# G = nx.gnm_random_graph(15,15)
# G = nx.gnm_random_graph(50,100)
# G = nx.gnp_random_graph(35,0.1)
# G = nx.erdos_renyi_graph(50,0.4)
# G = nx.barabasi_albert_graph(50,5)
# G = nx.newman_watts_strogatz_graph(20,2,0.9)
# G.add_node(55)
# G.add_edges_from([(50,51),(51,52),(52,50),(53,54)])

# J=nx.complete_graph(10)
# F=nx.complete_graph(5)
# G=nx.disjoint_union(J,F)
# e=(0,14)
# G.add_edge(*e)

# kmax = max(nx.core_number(G).values())

#### ΑΝΑΖΗΤΗΣΗ

# kmax=10
# # dmin=4
# counte=0
# mmin=1000
# # mmin=1000
# while True:
#     G = nx.gnp_random_graph(50,0.3)
#     # G = nx.gnm_random_graph(7,15)
#     if counte== mmin:
#         print counte,'a'
#         mmin+=1000
#         # mmin+=1000
#     # testy=max(nx.core_number(G).values())
#     mn=[]
#     for i in G.nodes():
#         if nx.core_number(G)[i]==max(nx.core_number(G).values()):
#             mn.append(i)
#     if len(G.subgraph(mn).edges())>0:
#         testy=max(nx.core_number(G).values())
#     else:
#         testy=max(nx.core_number(G).values())-1
#         # S=set(nx.core_number(G).values()) - set[max(nx.core_number(G).values())]
#         # testy=max(S)
#     # testy=nx.find_cliques(G)
#     # print testy, 'testy'
#     uu=0
#     if testy>=kmax:
#         uu+=1
#     # for g in testy:
#     #     if len(g)>=size_of_cliques:
#     #         uu+=1
#     # if uu>=number_of_cliques:
#         break
#     else:
#         counte+=1
#         continue




pos=nx.spring_layout(G,k=0.15,iterations=10)

# pos=nx.graphviz_layout(G)
# pos=layout(G)

# G.remove_nodes_from(nx.isolates(G))


print str(" ")
print 'ΠΥΡΗΝΕΣ ΣΕ ΓΡΑΦΟΥΣ'
# print 'CORES IN GRAPHS'
print str(" ")

print 'Ο γράφος είναι:'
# print 'The graph is:'
graph_name=str(G.name)+'_[k='+str(max(nx.core_number(G).values()))+']'
print graph_name
print str(" ")

degree_sequence=sorted(nx.degree(G).values(),reverse=False)
print "Ακολουθία βαθμών του G:"
# print "Degree sequence of G:"
print degree_sequence
print "Μέγιστος βαθμός:", max(degree_sequence)
print "Ελάχιστος βαθμός:", min(degree_sequence)
# print "Maximum degree of G:", max(degree_sequence)
# print "Minimum degree of G:", min(degree_sequence)
print str(" ")

# plt.figure()
# plt.title('The graph G')
# nx.draw(G,pos,with_labels=True,alpha=0.3)
# plt.show()

print 'ΟΡΙΣΜΟΣ: Ένας k-πυρήνας είναι ένας μέγιστος υπογράφος που περίέχει κόμβους βαθμού μεγαλύτερου ή ίσου με k.'
print 'Ο αριθμός πυρήνα ενός κόμβου είναι η μεγαλύτερη τιμή του k για όλους τους k-πυρήνες που περιέχουν τον κόμβο.'
# print 'DEFINITION: A k-core is a maximal subgraph that contains nodes of degree k or more.'
# print 'The core number of a node is the largest value k of a k-core containing that node.'
print str(" ")

print 'Το λεξικό των αριθμών πυρήνα κάθε κόμβου του γράφου:'
# print 'The dictionary of the core numbers for each vertex of G is:'
print nx.core_number(G)
print 'Οι τιμές των αριθμών πυρήνα κάθε κόμβου του γράφου:'
print nx.core_number(G).values()
# print 'Η τάξη του κύριου πυρήνα (που αντιστοιχεί στο μεγαλύτερο k):'
# print 'k =', max(nx.core_number(G).values())
# print str(" ")

mn=[]
for i in G.nodes():
    if nx.core_number(G)[i]==max(nx.core_number(G).values()):
        mn.append(i)
if len(G.subgraph(mn).edges())>0:
    maxk=max(nx.core_number(G).values())
else:
    S=set(nx.core_number(G).values()) - set[max(nx.core_number(G).values())]
    maxk=max(S)

print 'Η τάξη του κύριου πυρήνα (που αντιστοιχεί στο μεγαλύτερο k):'
print 'k =', maxk
print str(" ")

kcores=[]
for i in set(degree_sequence):
    if len(nx.k_core(G,k=i).nodes()) > 0:
    # print "i =", i
        kcGi=nx.k_core(G,k=i)
        print 'Οι κόμβοι του', str(i)+'-πυρήνα:'
        # print 'The nodes of the', str(i)+'-core:'
        print kcGi.nodes()
        # print 'Οι ακμές του', str(i)+'-πυρήνα:'
        # # print 'The edges of the k-core of G are:'
        # print kcGi.edges()
        # print 'Η ακολουθία βαθμών των κόμβων του', str(i)+'-πυρήνα:'
        # # print 'The degree sequence of the nodes of the', str(i)+'-core:'
        # print list(nx.degree(kcGi).values())
        # # # print 'The order of the main k-core of G is:'
        # # # print 'k =', min(list(nx.degree(kcGi).values()))
        # print str(" ")
        kcores.append(kcGi.nodes())
        # plt.figure()
        # plt.title('The %s-core of G'%i)
        # # 'Minimal Energy Configuration of %s Charges on Disc W = %s'%(N, W)
        # nx.draw(kcGi,pos,with_labels=True,node_color='g',alpha=0.3)

#### ΣΧΕΔΙΑΣΜΟΣ k-ΠΥΡΗΝΩΝ ΜΕΣΑ ΣΕ ΠΕΡΙΒΑΛΛΟΜΕΝΕΣ ΧΡΩΜΑΤΙΣΜΕΝΕΣ ΠΕΡΙΟΧΕΣ

import igraph as ig
graph_name=str(G.name)+'_[k='+str(max(nx.core_number(G).values()))+']'+'.graphml'
file_dir='temp'
try:
    os.stat(file_dir)
except:
    os.mkdir(file_dir)
graph_name=os.path.join(file_dir,graph_name)
nx.write_graphml(G, graph_name)
g = ig.read(graph_name, format="graphml")

# colors_list=["gray"]
colors_list=["gray","yellow","cyan","brown","green","red","blue"]
# colors_list=["gray","brown","yellow","green","cyan","blue","purple"]
colors_lists=[]
for i in range(len(kcores)):
    if i<len(colors_list):
        colors_lists.append(colors_list[i])
    else:
        color_to_set=(random.random(),random.random(),0.5)
        while color_to_set in colors_lists:
            color_to_set=(random.random(),random.random(),0.5)
        colors_lists.append(color_to_set)
group_markers = [(kcores[i], colors_lists[i]) for i in range(len(kcores))]
file_dir_figs='figs'
try:
    os.stat(file_dir_figs)
except:
    os.mkdir(file_dir_figs)
fig_name=os.path.join(file_dir_figs,str(G.name)+'_[k='+str(max(nx.core_number(G).values()))+']_k-cores.png')
layout=g.layout('auto')
# layout = g.layout('kk')
ig.plot(g, target=fig_name, layout=layout, vertex_size=7, vertex_color='gray', vertex_label_size=10, vertex_label_dist=2, mark_groups=group_markers) #vertex_label=None


print 'ΟΡΙΣΜΟΣ: Το k-κέλυφος είναι ο υπογράφος των κόμβων του k-πυρήνα που δεν περιέχονται στον (k+1)-πυρήνα.'
# print 'DEFINITION: The k-shell is the subgraph of nodes in the k-core but not in the (k+1)-core.'
print str(" ")

kshells=[]
for i in set(degree_sequence):
    if len(nx.k_shell(G,k=i).nodes()) > 0:
    # print "i =", i
        ksGi=nx.k_shell(G,k=i)
        print 'Οι κόμβοι του', str(i)+'-κελύφους:'
        # print 'The nodes of the', str(i)+'-shell:'
        print ksGi.nodes()
        # print 'Οι ακμές του', str(i)+'-κελύφους:'
        # # print 'The edges of the k-shell of G are:'
        # print ksGi.edges()
        # print 'Η ακολουθία βαθμών των κόμβων του', str(i)+'-κελύφους:'
        # # print 'The degree sequence of the nodes of the', str(i)+'-shell:'
        # print list(nx.degree(ksGi).values())
        # # # print 'The order of the main k-shell of G is:'
        # # # print 'k =', min(list(nx.degree(ksGi).values()))
        print str(" ")
        kshells.append(ksGi.nodes())
        # plt.figure()
        # plt.title('The %s-shell of G'%i)
        # # 'Minimal Energy Configuration of %s Charges on Disc W = %s'%(N, W)
        # nx.draw(ksGi,pos,with_labels=True,node_color='g',alpha=0.3)

#### ΣΧΕΔΙΑΣΜΟΣ k-ΚΕΛΥΦΩΝ ΜΕΣΑ ΣΕ ΠΕΡΙΒΑΛΛΟΜΕΝΕΣ ΧΡΩΜΑΤΙΣΜΕΝΕΣ ΠΕΡΙΟΧΕΣ

for i in range(len(kshells)):
    if i<len(colors_list):
        colors_lists.append(colors_list[i])
    else:
        color_to_set=(random.random(),random.random(),1)
        while color_to_set in colors_lists:
            color_to_set=(random.random(),random.random(),1)
        colors_lists.append(color_to_set)
group_markers = [(kshells[i], colors_lists[i]) for i in range(len(kshells))]
# ig.plot(g, mark_groups=group_markers)
fig_name=os.path.join(file_dir_figs,str(G.name)+'_[k='+str(max(nx.core_number(G).values()))+']_k-shells.png')
ig.plot(g, target=fig_name, layout=layout, vertex_size=7, vertex_color='gray', vertex_label_size=10, vertex_label_dist=2, mark_groups=group_markers) #vertex_label=None



# print 'ΟΡΙΣΜΟΣ: Η k-κρούστα είναι ο υπογράφος του G που μένει όταν αφαιρεθεί ο k-πυρήνας.'
# # print 'DEFINITION: The k-crust is the graph G with the k-core removed.'
# print str(" ")

kcrusts=[]
for i in set(nx.core_number(G).values()):
# for i in set(degree_sequence):
    if i > 0 and len(nx.k_crust(G,k=i-1).nodes()) > 0:
    # print "i =", i
        kcrGi=nx.k_crust(G,k=i-1)
        print 'Οι κόμβοι της', str(i)+'-κρούστας:'
        # print 'The nodes of the', str(i)+'-crust:'
        print kcrGi.nodes()
        # print 'Οι ακμές της', str(i)+'-κρούστας:'
        # # print 'The edges of the k-crust of G are:'
        # print kcrGi.edges()
        # print 'Η ακολουθία βαθμών των κόμβων της', str(i)+'-κρούστας:'
        # print 'The degree sequence of the nodes of the', str(i)+'-crust:'
        # print list(nx.degree(kcrGi).values())
        # # # print 'The order of the main k-crust of G is:'
        # # # print 'k =', min(list(nx.degree(kcrGi).values()))
        print str(" ")
        kcrusts.append(kcrGi.nodes())
        # plt.figure()
        # plt.title('The %s-crust of G'%i)
        # # 'Minimal Energy Configuration of %s Charges on Disc W = %s'%(N, W)
        # nx.draw(kcrGi,pos,with_labels=True,node_color='g',alpha=0.3)

#### ΣΧΕΔΙΑΣΜΟΣ k-ΚΡΟΥΣΤΩΝ ΜΕΣΑ ΣΕ ΠΕΡΙΒΑΛΛΟΜΕΝΕΣ ΧΡΩΜΑΤΙΣΜΕΝΕΣ ΠΕΡΙΟΧΕΣ

for i in range(len(kcrusts)):
    if i<len(colors_list):
        colors_lists.append(colors_list[i])
    else:
        color_to_set=(random.random(),random.random(),1)
        while color_to_set in colors_lists:
            color_to_set=(random.random(),random.random(),1)
        colors_lists.append(color_to_set)
group_markers = [(kcrusts[i], colors_lists[i]) for i in range(len(kcrusts))]
# ig.plot(g, mark_groups=group_markers)
fig_name=os.path.join(file_dir_figs,str(G.name)+'_[k='+str(max(nx.core_number(G).values()))+']_k-crusts.png')
ig.plot(g, target=fig_name, layout=layout, vertex_size=7, vertex_color='gray', vertex_label_size=10, vertex_label_dist=2, mark_groups=group_markers) #vertex_label=None



print 'Ορισμός: Το k-στέμμα είναι ο υπογράφος των κόμβων του k-πυρήνα, οι οποίοι κόμβοι έχουν ακριβώς k γείτονες στον k-πυρήνα.'
# print 'DEFINITION: The k-corona is the subgraph of nodes in the k-core which have exactly k neighbours in the k-core. στέμμα'
print str(" ")

kcoronas=[]
for i in set(nx.core_number(G).values()):
    if len(nx.k_corona(G,k=i).nodes()) > 0:
    # print "i =", i
        kcnGi=nx.k_corona(G,k=i)
        print 'Οι κόμβοι του', str(i)+'-στέμματος:'
        # print 'The nodes of the', str(i)+'-shell:'
        print kcnGi.nodes()
        # print 'Οι ακμές του', str(i)+'-στέμματος:'
        # # print 'The edges of the k-shell of G are:'
        # print kcnGi.edges()
        # print 'Η ακολουθία βαθμών των κόμβων του', str(i)+'-στέμματος:'
        # # print 'The degree sequence of the nodes of the', str(i)+'-shell:'
        # print list(nx.degree(ksGi).values())
        # # # print 'The order of the main k-shell of G is:'
        # # # print 'k =', min(list(nx.degree(ksGi).values()))
        print str(" ")
        kcoronas.append(kcnGi.nodes())
        # plt.figure()
        # plt.title('The %s-corona of G'%i)
        # # 'Minimal Energy Configuration of %s Charges on Disc W = %s'%(N, W)
        # nx.draw(kcnGi,pos,with_labels=True,node_color='g',alpha=0.3)

#### ΣΧΕΔΙΑΣΜΟΣ k-ΚΟΡΟΝΩΝ ΜΕΣΑ ΣΕ ΠΕΡΙΒΑΛΛΟΜΕΝΕΣ ΧΡΩΜΑΤΙΣΜΕΝΕΣ ΠΕΡΙΟΧΕΣ

for i in range(len(kcoronas)):
    if i<len(colors_list):
        colors_lists.append(colors_list[i])
    else:
        color_to_set=(random.random(),random.random(),1)
        while color_to_set in colors_lists:
            color_to_set=(random.random(),random.random(),1)
        colors_lists.append(color_to_set)
group_markers = [(kcoronas[i], colors_lists[i]) for i in range(len(kcoronas))]
# ig.plot(g, mark_groups=group_markers)
fig_name=os.path.join(file_dir_figs,str(G.name)+'_[k='+str(max(nx.core_number(G).values()))+']_k-coronas.png')
ig.plot(g, target=fig_name, layout=layout, vertex_size=7, vertex_color='gray', vertex_label_size=10, vertex_label_dist=2, mark_groups=group_markers) #vertex_label=None





# plt.show()

