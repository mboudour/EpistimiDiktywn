# -*- coding: utf-8 -*-
"""
    LAST UPDATE: 28 Νοεμβρίου 2014

    @author: Moses Boudourides
    """


import networkx as nx
import matplotlib.pyplot as plt
import random

#### ΣΥΝΔΕΣΙΜΟΤΗΤΑ ΜΗ ΚΑΤΕΥΘΥΝΟΜΕΝΩΝ ΓΡΑΦΩΝ

G = nx.erdos_renyi_graph(20,0.04)
pos=nx.spring_layout(G)

print str(" ")

print 'Is graph G connected?', nx.is_connected(G)
print 'The number of connected components of G is:', nx.number_connected_components(G)
print str(" ")

print 'List of connected components:'
print sorted(nx.connected_components(G), key = len, reverse=True)
print str(" ")

deg=G.degree()
deg_dic=[]
for nd in deg:
    if deg[nd]>0:
        deg_dic.append(nd)
node0 = random.choice(deg_dic)
print 'The nodes in the component of graph containing the randomly chosen node ' + str(node0) + ' are:'
print nx.node_connected_component(G,node0)
print str(" ")

colors_list=['c','b','g','y','k','m']
colors_to_select=list(colors_list)
graphs =sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)
connected_component_subgraphs_edges=[]
connected_component_subgraphs_nodes=[]
nodes_color_alpha=[]
edges_color_alpha=[]
colors_of_edges=[]
edge_width_l=[]
for gr in range(len(graphs)):
    graph='G' + str(gr+1)
    print 'Nodes of connected component', graph+':', graphs[gr].nodes()
    print 'Edges of connected component', graph+':', graphs[gr].edges()
    if len(graphs[gr].nodes()) >1 and len(graphs[gr].edges())>0:
        connected_component_subgraphs_edges.append(graphs[gr].edges())
        connected_component_subgraphs_nodes.append(graphs[gr].nodes())
        if gr==0:
            colors_of_edges.append('r')
            nodes_color_alpha.append(1)
            edges_color_alpha.append(1)
            edge_width_l.append(6.0)
        else:
            if len(colors_to_select)==0:
                colors_to_select=list(colors_list)
            color=random.choice(colors_to_select)
            colors_to_select.remove(color)
            colors_of_edges.append((color))
            nodes_color_alpha.append(0.4)
            edges_color_alpha.append(0.6)
            edge_width_l.append(4.0)
print str(" ")

Gcc=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)
Ggc=Gcc[0]
graph='Ggc'
print 'Nodes of giant connected component', graph+':', Ggc.nodes()
print 'Edges of giant connected component', graph+':', Ggc.edges()
print str(" ")

print 'Isolated nodes:', nx.isolates(G)
print str(" ")

n1=list(set(G.nodes()) - set(Ggc.nodes()) - set(nx.isolates(G)))
print 'Non-isolated nodes outside the giant component:', n1

N1=G.subgraph(n1)
print 'Edges among non-isolated nodes outside the giant component:', N1.edges()



plt.figure()

for i in range(len(connected_component_subgraphs_nodes)):
    node_list=connected_component_subgraphs_nodes[i]
    edge_list=connected_component_subgraphs_edges[i]
    edge_color=colors_of_edges[i]
    node_alpha=nodes_color_alpha[i]
    edge_alpha=edges_color_alpha[i]
    edge_width=edge_width_l[i]

    nx.draw(G,pos,nodelist=node_list,with_labels=True,node_size=500,edgelist=edge_list,edge_color=edge_color,width=edge_width,alpha=node_alpha,edgealpha=edge_alpha)
    nx.draw_networkx_nodes(G,pos,nodelist=nx.isolates(G),with_labels=True,node_size=500,node_color='w')

plt.show()
