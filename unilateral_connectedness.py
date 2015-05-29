# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import random

G = nx.gnm_random_graph(25,15,directed=True)
# G=nx.erdos_renyi_graph(4,1,directed=True)
G.remove_nodes_from(nx.isolates(G))

graphs =sorted(nx.weakly_connected_component_subgraphs(G), key = len, reverse=True)
weakly_connected_component_subgraphs_nodes=[]
weakly_connected_component_subgraphs_edges=[]
for gr in range(len(graphs)):
    graph='G' + str(gr+1)
    if len(graphs[gr].nodes()) >1 and len(graphs[gr].edges())>0:
        weakly_connected_component_subgraphs_nodes.append(graphs[gr].nodes())
        weakly_connected_component_subgraphs_edges.append(graphs[gr].edges())

# for i in range(len(graphs)):
#     print graphs[i].nodes()
#     print graphs[i].edges()
# print list(weakly_connected_component_subgraphs_nodes)
# print list(weakly_connected_component_subgraphs_edges)


for i in range(len(weakly_connected_component_subgraphs_nodes)):
    j= weakly_connected_component_subgraphs_nodes[i]
    # max_cn=[]
    for ni in j:    #range(len(j))
        for mi in j:
            if ni != mi:
                apj=nx.all_simple_paths(G,ni,mi)
                while len(list(apj))>1:
                    print str((i,(ni,mi))), list(apj)


# j= graphs[0]
# print j.nodes()
# print str((1,3)), list(nx.all_simple_paths(j,1,3))

# print j.nodes()
# print list(nx.all_simple_paths(G,j.nodes()[0],j.nodes()[1]))
# print aaa

# for ni in j.nodes():
#     for mi in j.nodes():
#         if ni != mi:
#             apj=nx.all_simple_paths(j,ni,mi)
#             print str((ni,mi)), list(apj)
