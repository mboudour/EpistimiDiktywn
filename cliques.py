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




#### ΚΛΙΚΕΣ ΣΕ ΜΗ ΚΑΤΕΥΘΥΝΟΜΕΝΟΥΣ ΓΡΑΦΟΥΣ

# G=nx.Graph()
# G.add_edges_from([(0,1),(1,2),(2,0),(3,4)])
# G.add_node(5)
# pos={0:(0,0),1:(0,1),2:(0.5,1),3:(0.5,0),4:(1,0),5:(0.75,0.5)}

# G = nx.gnp_random_graph(30,0.3)
# G = nx.erdos_renyi_graph(15,0.06)
G = nx.gnm_random_graph(15,10)
# G = nx.gnm_random_graph(35,20)
# G = nx.gnp_random_graph(35,0.1)
# G = nx.erdos_renyi_graph(30,0.024)
# G = nx.barabasi_albert_graph(50,2)
# G = nx.newman_watts_strogatz_graph(20,2,0.9)
# G.add_node(55)
# G.add_edges_from([(50,51),(51,52),(52,50),(53,54)])

# J=nx.complete_graph(10)
# F=nx.complete_graph(5)
# G=nx.disjoint_union(J,F)
# e=(0,14)
# G.add_edge(*e)



#### ΑΝΑΖΗΤΗΣΗ

# number_of_cliques=1
# size_of_cliques=5
# # size_of_cliques1=5
# # size_of_cliques2=4
# # size_of_cliques3=3
# counte=0
# mmin=1000
# while True:
#     G = nx.gnm_random_graph(10,20)
#     G.remove_nodes_from(nx.isolates(G))
#     if counte== mmin:
#         print counte,'a'
#         mmin+=1000
#     testy=nx.find_cliques(G)
#     # print testy
#     uu=0
#     for g in testy:
#         if len(g)>=size_of_cliques:
#         # if len(g)>=size_of_cliques1 and len(g)==size_of_cliques2 and len(g)==size_of_cliques3:
#         # if len(g)>=size_of_cliques1:
#             uu+=1
#     if uu>=number_of_cliques:
#         break
#     else:
#         counte+=1
#         continue



pos=nx.spring_layout(G,k=0.15,iterations=10)
# pos=nx.graphviz_layout(G)
# pos=layout(G)

G.remove_nodes_from(nx.isolates(G))


colors_list=['c','b','g','y','k','m']
colors_to_select=list(colors_list)

graphs=sorted(nx.find_cliques(G), key = len, reverse=True)

cliques_edges=[]
cliques_nodes=[]
nodes_color_alpha=[]
edges_color_alpha=[]
colors_of_edges=[]
edge_width_l=[]
graphs_labels=dict()
graphs_labelsGcc=dict()
graphs_len=dict()
graphs_lists=dict()
for gr in range(len(graphs)):
    graph='G' + str(gr+1)
    tem='['
    ttem=[]
    gtem=0
    for nd in graphs[gr]:
        tem+='%s, ' %nd
        ttem.append(nd)
        gtem+=1
    tem =tem[:-2]+']'
    graphs_labels[gr+1]=tem
    graphs_labelsGcc[gr]=tem
    graphs_len[gr]=gtem
    graphs_lists[gr]=ttem
    graphh=G.subgraph(graphs[gr])
    if len(graphh.nodes()) >1 and len(graphh.edges())>0:
        cliques_edges.append(graphh.edges())
        cliques_nodes.append(graphh.nodes())
        if len(colors_to_select)==0:
            colors_to_select=list(colors_list)
        color=random.choice(colors_to_select)
        colors_to_select.remove(color)
        colors_of_edges.append((color))
        nodes_color_alpha.append(0.4)
        edges_color_alpha.append(0.6)
        edge_width_l.append(4.0)
lvl2=[]
for i in range(nx.graph_number_of_cliques(G)):
    lvl2.append(graphs_len[i])

print str(" ")
print 'ΚΛΙΚΕΣ ΣΕ ΜΗ ΚΑΤΕΥΘΥΝΟΜΕΝΟΥΣ ΓΡΑΦΟΥΣ'
# print 'CLIQUES IN UNDIRECTED GRAPHS'
print str(" ")

print 'Ο γράφος είναι:'
# print 'The graph is:'
graph_name=str(G.name)+str(lvl2)
print graph_name
print str(" ")

print 'Το σύνολο όλων των κλικών του γράφου G:'
# print 'The set of all maximal cliques in graph G is:'
print sorted(nx.find_cliques(G), key = len, reverse=True)
print 'Το πλήθος όλων των κλικών του G είναι:', nx.graph_number_of_cliques(G)
# print 'The number of maximal cliques of G is:', nx.graph_number_of_cliques(G)
print str(" ")

# colors_list=['c','b','g','y','k','m']
# colors_to_select=list(colors_list)
#
# graphs=sorted(nx.find_cliques(G), key = len, reverse=True)
#
# cliques_edges=[]
# cliques_nodes=[]
# nodes_color_alpha=[]
# edges_color_alpha=[]
# colors_of_edges=[]
# edge_width_l=[]
# graphs_labels=dict()
# graphs_labelsGcc=dict()
# graphs_len=dict()
# graphs_lists=dict()
# for gr in range(len(graphs)):
#     graph='G' + str(gr+1)
#     tem='['
#     ttem=[]
#     gtem=0
#     for nd in graphs[gr]:
#         tem+='%s, ' %nd
#         ttem.append(nd)
#         gtem+=1
#     tem =tem[:-2]+']'
#     graphs_labels[gr+1]=tem
#     graphs_labelsGcc[gr]=tem
#     graphs_len[gr]=gtem
#     graphs_lists[gr]=ttem
#     graphh=G.subgraph(graphs[gr])
#     if len(graphh.nodes()) >1 and len(graphh.edges())>0:
#         cliques_edges.append(graphh.edges())
#         cliques_nodes.append(graphh.nodes())
#         if len(colors_to_select)==0:
#             colors_to_select=list(colors_list)
#         color=random.choice(colors_to_select)
#         colors_to_select.remove(color)
#         colors_of_edges.append((color))
#         nodes_color_alpha.append(0.4)
#         edges_color_alpha.append(0.6)
#         edge_width_l.append(4.0)
# lvl2=[]
# for i in range(nx.graph_number_of_cliques(G)):
#     lvl2.append(graphs_len[i])


print 'Η λίστα των μεγεθών των κλικών είναι:'
# print 'The list of clique sizes is:'
print lvl2
print str(" ")

print 'Ο αριθμός κλίκας (το μέγεθος της μεγαλύτερης κλίκας) του G είναι:', nx.graph_clique_number(G)
# print 'The clique number (size of the largest clique) for G is:', nx.graph_clique_number(G)
# print sorted(nx.connected_components(G), key = len, reverse=True)
print str(" ")

print 'Το λεξικό των κλικών που περιέχουν κάθε κόμβο είναι:'
# print 'The dictionary of the lists of cliques containing each node:'
print nx.cliques_containing_node(G)
print str(" ")

print 'Το λεξικό του πλήθους κλικών που περιέχουν κάθε κόμβο είναι:'
# print 'The dictionary of the numbers of maximal cliques for each node:'
print nx.number_of_cliques(G)
print str(" ")

print 'Το λεξικό του μεγέθους των μεγαλύτερων κλικών που περιέχουν κάθε κόμβο είναι:'
# print 'The dictionary of the sizes of the largest maximal cliques containing each given node:'
print nx.node_clique_number(G)
print str(" ")

maxclique = [clq for clq in nx.find_cliques(G) if len(clq) == nx.graph_clique_number(G)]
nodes = [n for clq in maxclique for n in clq]
H = G.subgraph(nodes)
# print H.edges()


#### ΣΧΕΔΙΑΣΜΟΣ ΚΛΙΛΩΝ ΜΕΣΑ ΣΕ ΠΕΡΙΒΑΛΛΟΜΕΝΕΣ ΧΡΩΜΑΤΙΣΜΕΝΕΣ ΠΕΡΙΟΧΕΣ

import igraph as ig
file_name=str(G.name)+str(lvl2)+'.graphml'
file_dir='temp'
try:
    os.stat(file_dir)
except:
    os.mkdir(file_dir)
file_name=os.path.join(file_dir,file_name)
nx.write_graphml(G, file_name)
g = ig.read(file_name, format="graphml")

mcliques=g.maximal_cliques(0,5)
colors_list=["gray","brown","yellow","cyan","green","blue","purple"]
colors_lists=[]
for i in range(len(mcliques)):
    if i<len(colors_list):
        colors_lists.append(colors_list[i])
    else:
        color_to_set=(random.random(),random.random(),1)
        while color_to_set in colors_lists:
            color_to_set=(random.random(),random.random(),1)
        colors_lists.append(color_to_set)
group_markers = [(mcliques[i], colors_lists[i]) for i in range(len(mcliques))]
ig.plot(g, mark_groups=group_markers)


colors_list=['c','b','g','y','k','m']
colors_to_select=list(colors_list)

graphs=sorted(nx.find_cliques(G), key = len, reverse=True)

cliques_edges=[]
cliques_nodes=[]
nodes_color_alpha=[]
edges_color_alpha=[]
colors_of_edges=[]
edge_width_l=[]
graphs_labels=dict()
graphs_labelsGcc=dict()
graphs_len=dict()
graphs_lists=dict()
for gr in range(len(graphs)):
    graph='G' + str(gr+1)
    tem='['
    ttem=[]
    gtem=0
    for nd in graphs[gr]:
        tem+='%s, ' %nd
        ttem.append(nd)
        gtem+=1
    tem =tem[:-2]+']'
    graphs_labels[gr+1]=tem
    graphs_labelsGcc[gr]=tem
    graphs_len[gr]=gtem
    graphs_lists[gr]=ttem
    graphh=G.subgraph(graphs[gr])
    if len(graphh.nodes()) >1 and len(graphh.edges())>0:
        cliques_edges.append(graphh.edges())
        cliques_nodes.append(graphh.nodes())
        if len(colors_to_select)==0:
            colors_to_select=list(colors_list)
        color=random.choice(colors_to_select)
        colors_to_select.remove(color)
        colors_of_edges.append((color))
        nodes_color_alpha.append(0.4)
        edges_color_alpha.append(0.6)
        edge_width_l.append(4.0)

for i in range(len(cliques_nodes)):
    node_list=cliques_nodes[i]
    edge_list=cliques_edges[i]
    edge_color=colors_of_edges[i]
    node_alpha=nodes_color_alpha[i]
    edge_alpha=edges_color_alpha[i]
    edge_width=edge_width_l[i]

    plt.title('Cliques in graph G')
    nx.draw(G,pos,nodelist=node_list,with_labels=True,node_size=500,edgelist=edge_list,edge_color=edge_color,width=edge_width,alpha=node_alpha,edgealpha=edge_alpha)
    nx.draw_networkx_nodes(G,pos,nodelist=nx.isolates(G),with_labels=True,node_size=500,node_color='w')


plt.figure()
plt.title('The maximal cliques of graph G')
nx.draw(H,with_labels=True)



ClG=nx.make_max_clique_graph(G)

# print 'ClG nodes'
# print ClG.nodes()
# print str(" ")
#
# print 'ClG edges'
# print ClG.edges()
# print str(" ")
#
# print graphs_labels
# print type(graphs_labels)


# graphs=sorted(nx.find_cliques(G), key = len, reverse=True)
# graphs_labels_s=sorted(graphs_labels, key = len, reverse=True)

# ClG_relabeled=nx.relabel_nodes(ClG,graphs_labels,copy=True)
ClG_relabeled=nx.relabel_nodes(ClG,graphs_labels,copy=True)
posC=nx.spring_layout(ClG_relabeled)
# posC=nx.spring_layout(ClG_relabeled,k=0.15,iterations=10)


# print 'ClG_relabeled nodes'
# print ClG_relabeled.nodes()
# print str(" ")
#
# print 'ClG_relabeled edges'
# print ClG_relabeled.edges()
# print str(" ")


lvl2=[]
# print range(nx.graph_number_of_cliques(G)),nx.graph_number_of_cliques(G)
# for i in graphs_lists:
for i in range(nx.graph_number_of_cliques(G)):
    lvl2.append(graphs_len[i])
    # lvl2.append(len(ClG_relabeled.nodes()[i])) #eval
    # lvl2.append(len(eval(ClG_relabeled.nodes()[i]))) #eval

# print 'lvl2'
# print lvl2
# print str(" ")



# plt.figure()
#
# nx.draw(ClG_relabeled,pos=posC,font_size=16,with_labels=False,node_size=[v * 100 for v in lvl2],node_color='g') #node_size=[v * 100 for v in lvl2],
# for p in posC:
#         posC[p][1] += 0.04
# nx.draw_networkx_labels(ClG_relabeled,posC)







BcG=nx.make_clique_bipartite(G,fpos=True)
bottom_nodes, top_nodes = bipartite.sets(BcG)
BcG_labels=dict()
Bcg_labels=dict()
for nd in top_nodes:
    tem='['
    for cc in nx.all_neighbors(BcG,nd):
        tem+=str(cc)+', '
    tem=tem[:-2]+']'
    BcG_labels[nd]=tem
    Bcg_labels[nd]=tem
for nd in bottom_nodes:
    BcG_labels[nd]=str(nd)

# print bottom_nodes
# print top_nodes
print BcG_labels, 'BcG_labels'
#
# print list(bottom_nodes), 'bottom nodes'
# # print len(list(bottom_nodes))
# print list(top_nodes), 'top nodes'
# print len(list(top_nodes))

BcG_relabel=nx.relabel_nodes(BcG,BcG_labels,copy=True)
# pos=dict(zip(range(len(list(top_nodes))),zip(range(len(list(top_nodes))),[1]*len(list(top_nodes))))) # upper nodes
# pos.update(dict(zip(range(len(list(top_nodes)),len(list(top_nodes))+len(list(bottom_nodes))),zip(range(len(list(bottom_nodes))),[0]*len(list(bottom_nodes)))))) # lower nodes

# print BcG.pos

plt.figure(facecolor='w')
# nx.draw_networkx_edges(BcG,pos=BcG.pos)
plt.title('The bipartite graph of cliques and nodes of G')
nx.draw_networkx_nodes(BcG,pos=BcG.pos,nodelist=list(bottom_nodes),node_color='r')
# nx.draw_networkx(BcG,pos=BcG.pos,nodelist=list(bottom_nodes),with_labels=True,node_color='r')   #,node_size=300
# nx.draw_networkx(BcG,pos=BcG.pos,nodelist=list(top_nodes),with_labels=False,node_color='b',node_shape='s')    #,node_size=400
nx.draw_networkx_nodes(BcG,pos=BcG.pos,nodelist=list(top_nodes),node_color='b',node_shape='s')
nx.draw_networkx_edges(BcG,pos=BcG.pos)
BcGPos=dict()

for p in BcG.pos:  # raise text positions
    if p<0:
        BcGPos[p]=(BcG.pos[p][0],BcG.pos[p][1]+0.06)  #0.045
    else:
        BcGPos[p]=BcG.pos[p]
    # BcGPos[p][1] += 0.045 #offset 0.07
# print pos
nx.draw_networkx_labels(BcG,pos=BcGPos,labels=BcG_labels)
# nx.draw_networkx_labels(BcG,pos=BcG.pos,nodelist=list(bottom_nodes))
plt.axis('off')
plt.axis("tight")


PG=nx.projected_graph(BcG,top_nodes)

posPG=nx.spring_layout(PG,k=0.15,iterations=10)

plt.figure()
plt.title('The graph of cliques of G')
nx.draw(PG,posPG,with_labels=False,node_color='g')
for p in posPG:  # raise text positions
        posPG[p][1] += 0.045 #offset 0.07
nx.draw_networkx_labels(PG,posPG,labels=Bcg_labels)

plt.show()

# #### ΣΧΕΔΙΑΣΜΟΣ ΚΛΙΛΩΝ ΜΕΣΑ ΣΕ ΠΕΡΙΒΑΛΛΟΜΕΝΕΣ ΧΡΩΜΑΤΙΣΜΕΝΕΣ ΠΕΡΙΟΧΕΣ

# import igraph as ig
# file_name=str(G.name)+str(lvl2)+'.graphml'
# file_dir='temp'
# try:
#     os.stat(file_dir)
# except:
#     os.mkdir(file_dir)
# nx.write_graphml(G, file_name)
# # print file_name
# g = ig.read(file_name, format="graphml")
# mcliques=g.maximal_cliques(0,5)
# # print mcliques
# colors_list=["gray","brown","yellow","cyan","green","blue","purple"]
# colors_lists=[]
# for i in range(len(mcliques)):
#     if i<len(colors_list):
#         colors_lists.append(colors_list[i])
#     else:
#         color_to_set=(random.random(),random.random(),1)
#         while color_to_set in colors_lists:
#             color_to_set=(random.random(),random.random(),1)
#         colors_lists.append(color_to_set)
# group_markers = [(mcliques[i], colors_lists[i]) for i in range(len(mcliques))]
# ig.plot(g, mark_groups=group_markers)

