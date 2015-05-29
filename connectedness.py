# -*- coding: utf-8 -*-
"""
    LAST UPDATE: 9 Δεκεμβρίου 2014

    @author: Moses Boudourides & Sergios Lenis
    """


import networkx as nx
import matplotlib.pyplot as plt
import random
# try:
#     from networkx import graphviz_layout
#     layout=nx.graphviz_layout
# except ImportError:
#     print("PyGraphviz not found; drawing with spring layout; will be slow.")
#     layout=nx.spring_layout




#### ΣΥΝΔΕΣΙΜΟΤΗΤΑ ΜΗ ΚΑΤΕΥΘΥΝΟΜΕΝΩΝ ΓΡΑΦΩΝ

# # # G=nx.Graph()
# # # G.add_edges_from([(0,1),(1,2),(2,0),(3,4)])
# # # G.add_node(5)
# # # pos={0:(0,0),1:(0,1),2:(0.5,1),3:(0.5,0),4:(1,0),5:(0.75,0.5)}
# #
# # # G = nx.gnp_random_graph(15,0.04)
# # G = nx.gnm_random_graph(15,10)
# # # G = nx.barabasi_albert_graph(50,2)
# # # G = nx.newman_watts_strogatz_graph(20,2,0.9)
# # # G.add_node(55)
# # # G.add_edges_from([(50,51),(51,52),(52,50),(53,54)])
# #
# # # G = nx.erdos_renyi_graph(15,0.06)
# # # pos=nx.spring_layout(G,k=0.15,iterations=10)
# # # pos=nx.graphviz_layout(G)
# # # pos=layout(G)



#### ΑΝΑΖΗΤΗΣΗ

number_of_components=3
size_of_component=6
counte=0
mmin=1000
while True:
    G = nx.gnm_random_graph(35,20)
    # G = nx.gnp_random_graph(35,0.1)
    # G = nx.erdos_renyi_graph(30,0.024)
    if counte== mmin:
        print counte
        mmin+=1000
    testy=list(nx.connected_components(G))
    print testy
    uu=0
    for g in testy:
        if len(g)>=size_of_component:
            uu+=1
    if uu>=number_of_components:
        break
    else:
        counte+=1
        continue
    # print counte,'a'
        



pos=nx.spring_layout(G,k=0.15,iterations=10)

print str(" ")
print 'CONNECTEDNESS OF UNDIRECTED GRAPHS'
print str(" ")

G.remove_nodes_from(nx.isolates(G))

print str(" ")
print G.name
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
print 'Non-isolated nodes outside the giant connected component:', n1

N1=G.subgraph(n1)
print 'Edges among non-isolated nodes outside the giant connected component:', N1.edges()



plt.figure()

# plt.title('Connected components of an undirected graph')
for i in range(len(connected_component_subgraphs_nodes)):
    node_list=connected_component_subgraphs_nodes[i]
    edge_list=connected_component_subgraphs_edges[i]
    edge_color=colors_of_edges[i]
    node_alpha=nodes_color_alpha[i]
    edge_alpha=edges_color_alpha[i]
    edge_width=edge_width_l[i]

    nx.draw(G,pos,nodelist=node_list,with_labels=True,node_size=500,edgelist=edge_list,edge_color=edge_color,width=edge_width,alpha=node_alpha,edgealpha=edge_alpha)
    nx.draw_networkx_nodes(G,pos,nodelist=nx.isolates(G),with_labels=True,node_size=500,node_color='w')
# plt.savefig('foo1.png')





#### ΙΣΧΥΡΗ ΣΥΝΔΕΣΙΜΟΤΗΤΑ ΚΑΤΕΥΘΥΝΟΜΕΝΩΝ ΓΡΑΦΩΝ

# # # G=nx.DiGraph()
# # # G.add_edges_from([(0,1),(1,2),(0,2),(2,0),(3,5),(3,4)])
# # # G.add_node(5)
# # # pos={0:(0,0),1:(0,1),2:(0.5,1),3:(0.5,0),4:(1,0),5:(0.75,0.5)}
# #
# # # G = nx.erdos_renyi_graph(30,0.02,directed=True)
# # G = nx.gnm_random_graph(20,15,directed=True)
# # # G.add_node(55)
# # # G.add_edges_from([(50,51),(51,52),(52,50),(53,54)])
# # # pos=nx.spring_layout(G)
# #
# # # G = nx.erdos_renyi_graph(20,0.04,directed=True)
# # # G = nx.gnp_random_graph(20,0.1,directed=True)
# # # G = nx.gnm_random_graph(20,35,directed=True)



#### ΑΝΑΖΗΤΗΣΗ

number_of_components=5
size_of_component=3
counte=0
mmin=1000
while True:
    # G = nx.erdos_renyi_graph(20,0.07,directed=True)
    G = nx.gnm_random_graph(25,35,directed=True)
    # pos=nx.spring_layout(G,k=0.15,iterations=10)
    # print counte
    if counte== mmin:
        print counte,'a'
        mmin+=1000
    testy=nx.strongly_connected_components(G)
    # print testy
    uu=0
    for g in testy:
        if len(g)>=size_of_component:
            uu+=1
    if uu>=number_of_components:
        break
    else:
        counte+=1
        continue
    # print counte,'a'



pos=nx.spring_layout(G,k=0.15,iterations=10)
# pos=nx.graphviz_layout(G)
# pos=layout(G)

G.remove_nodes_from(nx.isolates(G))

print str(" ")
print 'STRONG CONNECTEDNESS OF DIRECTED GRAPHS'
print str(" ")

print str(" ")
print G.name
print str(" ")

print 'Is graph G strongly connected?', nx.is_strongly_connected(G)
print 'The number of strongly connected components of G is:', nx.number_strongly_connected_components(G)
print str(" ")

lc=sorted(nx.strongly_connected_components(G), key = len, reverse=True)
print 'List of strongly connected components:'
print lc
print str(" ")


deg=G.degree()
deg_dic=[]
for nd in deg:
    if deg[nd]>0:
        deg_dic.append(nd)
node0 = random.choice(deg_dic)

for i in range(nx.number_strongly_connected_components(G)):
    if node0 in lc[i] :
        print 'The nodes in the strongly connected component of graph containing the randomly chosen node ' + str(node0) + ' are: \n', lc[i]
print str(" ")

colors_list=['c','b','g','y','k','m']
colors_to_select=list(colors_list)
graphs =sorted(nx.strongly_connected_component_subgraphs(G), key = len, reverse=True)
strongly_connected_component_subgraphs_edges=[]
strongly_connected_component_subgraphs_nodes=[]
nodes_color_alpha=[]
edges_color_alpha=[]
colors_of_edges=[]
edge_width_l=[]
strongly_connected_component_subgraphs_edges_one_mode=[]
strongly_connected_component_subgraphs_nodes_one_mode=[]
nodes_color_alpha=[]
edges_color_alpha=[]
colors_of_edges=[]
edge_width_l=[]
graphs_labels=dict()
graphs_lists=dict()
for gr in range(len(graphs)):
    graph='G' + str(gr+1)
    # print 'Nodes of strongly connected component', graph+':', graphs[gr].nodes()
    # print 'Edges of strongly connected component', graph+':', graphs[gr].edges()
    tem='['
    ttem=[]
    for nd in graphs[gr].nodes():
        tem+='%s, ' %nd
        ttem.append(nd)
    tem =tem[:-2]+']'
    graphs_labels[gr]=tem
    graphs_lists[gr]=ttem
    if len(graphs[gr].nodes()) >1 and len(graphs[gr].edges())>0:
        strongly_connected_component_subgraphs_edges.append(graphs[gr].edges())
        strongly_connected_component_subgraphs_nodes.append(graphs[gr].nodes())
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
    elif len(graphs[gr].nodes()) ==1 and len(graphs[gr].edges())==0:
        # strongly_connected_component_subgraphs_edges.append(graphs[gr].edges())
        strongly_connected_component_subgraphs_nodes_one_mode.append(graphs[gr].nodes())
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
if len(strongly_connected_component_subgraphs_nodes)==0:
    strongly_connected_component_subgraphs_nodes=strongly_connected_component_subgraphs_nodes_one_mode
# print str(" ")

Gcc=sorted(nx.strongly_connected_component_subgraphs(G), key = len, reverse=True)
Ggc=Gcc[0]
graph='Ggc'
print 'Nodes of giant strongly connected component', graph+':', Ggc.nodes()
print 'Edges of giant strongly connected component', graph+':', Ggc.edges()
print str(" ")

print 'Isolated nodes:', nx.isolates(G)
print str(" ")
# l0out = [k for k,v in G.out_degree().iteritems() if v == 0]

n1=list(set(G.nodes()) - set(Ggc.nodes()) - set(nx.isolates(G)))
print 'Non-isolated nodes outside the giant strongly connected component:', n1
# print 'D-Non-isolated nodes outside the giant strongly connected component:', nD1

N1=G.subgraph(n1)
print 'Edges among non-isolated nodes outside the giant strongly connected component:', N1.edges()
print str(" ")

plt.figure()

# plt.title('Strongly connected components of a directed graph')
for i in range(len(strongly_connected_component_subgraphs_nodes)):
    node_list=strongly_connected_component_subgraphs_nodes[i]
    node_alpha=nodes_color_alpha[i]
    if len(strongly_connected_component_subgraphs_edges)<1:
        nx.draw(G,pos,nodelist=node_list,with_labels=True,node_size=500,alpha=node_alpha)
        nx.draw_networkx_nodes(G,pos,nodelist=nx.isolates(G),with_labels=True,node_size=500,node_color='w')
        nx.draw_networkx_nodes(G,pos,nodelist=l0,with_labels=True,node_size=500,node_color='w')
        nx.draw_networkx_nodes(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3)
        nx.draw(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3)
    else:
        edge_list=strongly_connected_component_subgraphs_edges[i]
        edge_color=colors_of_edges[i]

        edge_alpha=edges_color_alpha[i]
        edge_width=edge_width_l[i]

        nx.draw(G,pos,nodelist=node_list,with_labels=True,node_size=500,edgelist=edge_list,edge_color=edge_color,width=edge_width,alpha=node_alpha,edgealpha=edge_alpha)
        nx.draw_networkx_nodes(G,pos,nodelist=nx.isolates(G),with_labels=True,node_size=500,node_color='w')
        # nx.draw_networkx_nodes(G,pos,nodelist=l0,with_labels=True,node_size=500,node_color='w')
        # nx.draw_networkx_nodes(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3)
        nx.draw(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3) #edge_color='k',
        # nx.draw(G,pos,nodelist=N1,edgelist=N1.edges(),with_labels=True,node_size=500,node_color='r',alpha=0.3)
# plt.savefig('foo2.png')

S=nx.condensation(G)
condensation_graph_relabeled=nx.relabel_nodes(S,graphs_labels,copy=True)
posS=nx.spring_layout(condensation_graph_relabeled,k=0.15,iterations=10)
# posS=layout(condensation_graph_relabeled)

# lvl=[]
# print condensation_graph_relabeled.nodes(),'ssssssss'
# for i in range(len(condensation_graph_relabeled.nodes())):
#     lvl.append(len(eval(condensation_graph_relabeled.nodes()[i])))
    # lvl.append(len(condensation_graph_relabeled.nodes()[i]))

# lvl2=[]
# for i in graphs_lists:
#     lvl2.append(len(graphs_lists[i]))

# print 'condensation_graph_relabeled nodes'
# print condensation_graph_relabeled.nodes()

lvl2=[]
for i in graphs_lists:
    lvl2.append(len(eval(condensation_graph_relabeled.nodes()[i])))

# print lvl2
# print 'List of strongly connected components:'
# print lc
# print 'graphs_labels'
# print graphs_labels
# print 'Nodes of S'
# print S.nodes()
# print 'Nodes of condensation_graph_relabeled:'
# print condensation_graph_relabeled.nodes()
# print 'Print list of values lengths'
# # print lvl
# print lvl2

plt.figure()

# plt.title('Condensation graph of the strongly connected components of a directed graph')
nx.draw(condensation_graph_relabeled,pos=posS,font_size=16,with_labels=False,node_size=[v * 100 for v in lvl2],node_color='g')
for p in posS:  # raise text positions
        posS[p][1] += 0.04 #offset 0.07
nx.draw_networkx_labels(condensation_graph_relabeled,posS)
# plt.savefig('foo3.png')





#### ΑΣΘΕΝΗΣ ΣΥΝΔΕΣΙΜΟΤΗΤΑ ΚΑΤΕΥΘΥΝΟΜΕΝΩΝ ΓΡΑΦΩΝ

# # G=nx.DiGraph()
# # G.add_edges_from([(0,1),(1,2),(0,2),(2,0),(3,5),(3,4)])
# # G.add_node(5)
# # pos={0:(0,0),1:(0,1),2:(0.5,1),3:(0.5,0),4:(1,0),5:(0.75,0.5)}
# #
# # G = nx.erdos_renyi_graph(10,0.05,directed=True)
# # G = nx.erdos_renyi_graph(20,0.01,directed=True)
# # G = nx.gnp_random_graph(20,0.04,directed=True)
# G = nx.gnm_random_graph(25,5,directed=True)



#### ΑΝΑΖΗΤΗΣΗ

number_of_components=4
size_of_component=5
counte=0
mmin=1000
while True:
    # G = nx.erdos_renyi_graph(20,0.07,directed=True)
    G = nx.gnm_random_graph(30,20,directed=True)
    # pos=nx.spring_layout(G,k=0.15,iterations=10)
    if counte== mmin:
        print counte,'b'
        mmin+=1000
    testy=nx.weakly_connected_components(G)
    # print testy
    uu=0
    for g in testy:
        if len(g)>=size_of_component:
            uu+=1
    if uu>=number_of_components:
        break
    else:
        counte+=1
        continue
    # print counte,'a'



pos=nx.spring_layout(G,k=0.15,iterations=10)
# pos=nx.graphviz_layout(G)
# pos=layout(G)

G.remove_nodes_from(nx.isolates(G))

print str(" ")
print 'WEAK CONNECTEDNESS OF DIRECTED GRAPHS'
print str(" ")

print str(" ")
print G.name
print str(" ")

print 'Is graph G weakly connected?', nx.is_weakly_connected(G)
print 'The number of weakly connected components of G is:', nx.number_weakly_connected_components(G)
print str(" ")

lc=sorted(nx.weakly_connected_components(G), key = len, reverse=True)
print 'List of weakly connected components:'
# print sorted(nx.weakly_connected_components(G), key = len, reverse=True)
print lc
print str(" ")


deg=G.degree()
deg_dic=[]
for nd in deg:
    if deg[nd]>0:
        deg_dic.append(nd)
node0 = random.choice(deg_dic)

for i in range(nx.number_weakly_connected_components(G)):
    if node0 in lc[i] :
        print 'The nodes in the weakly connected component of graph containing the randomly chosen node ' + str(node0) + ' are: \n', lc[i]
print str(" ")

colors_list=['c','b','g','y','k','m']
colors_to_select=list(colors_list)
graphs =sorted(nx.weakly_connected_component_subgraphs(G), key = len, reverse=True)
weakly_connected_component_subgraphs_edges=[]
weakly_connected_component_subgraphs_nodes=[]
nodes_color_alpha=[]
edges_color_alpha=[]
colors_of_edges=[]
edge_width_l=[]
weakly_connected_component_subgraphs_edges_one_mode=[]
weakly_connected_component_subgraphs_nodes_one_mode=[]
nodes_color_alpha=[]
edges_color_alpha=[]
colors_of_edges=[]
colors_of_nodes=[]
edge_width_l=[]
for gr in range(len(graphs)):
    graph='G' + str(gr+1)
    print 'Nodes of weakly connected component', graph+':', graphs[gr].nodes()
    print 'Edges of weakly connected component', graph+':', graphs[gr].edges()
    if len(graphs[gr].nodes()) >1 and len(graphs[gr].edges())>0:
        weakly_connected_component_subgraphs_edges.append(graphs[gr].edges())
        weakly_connected_component_subgraphs_nodes.append(graphs[gr].nodes())
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
            colors_of_nodes.append((color))
            nodes_color_alpha.append(0.4)
            edges_color_alpha.append(0.6)
            edge_width_l.append(4.0)
    elif len(graphs[gr].nodes()) ==1 and len(graphs[gr].edges())==0:
        # weakly_connected_component_subgraphs_edges.append(graphs[gr].edges())
        weakly_connected_component_subgraphs_nodes_one_mode.append(graphs[gr].nodes())
        if gr==0:
            colors_of_edges.append('r')
            colors_of_nodes.append(1)
            nodes_color_alpha.append(1)
            edges_color_alpha.append(1)
            edge_width_l.append(6.0)
        else:
            if len(colors_to_select)==0:
                colors_to_select=list(colors_list)
            color=random.choice(colors_to_select)
            colors_to_select.remove(color)
            colors_of_edges.append((color))
            colors_of_nodes.append((color))
            nodes_color_alpha.append(0.4)
            edges_color_alpha.append(0.6)
            edge_width_l.append(4.0)
if len(weakly_connected_component_subgraphs_nodes)==0:
    weakly_connected_component_subgraphs_nodes=strongly_connected_component_subgraphs_nodes_one_mode
print str(" ")

Gcc=sorted(nx.weakly_connected_component_subgraphs(G), key = len, reverse=True)
Ggc=Gcc[0]
graph='Ggc'
print 'Nodes of giant weakly connected component', graph+':', Ggc.nodes()
print 'Edges of giant weakly connected component', graph+':', Ggc.edges()
print str(" ")

print 'Isolated nodes:', nx.isolates(G)
print str(" ")

n1=list(set(G.nodes()) - set(Ggc.nodes()) - set(nx.isolates(G)))
print 'Non-isolated nodes outside the giant weakly connected component:', n1

N1=G.subgraph(n1)
print 'Edges among non-isolated nodes outside the giant weakly connected component:', N1.edges()

plt.figure()

# plt.title('Weakly connected components of a directed graph')
for i in range(len(weakly_connected_component_subgraphs_nodes)):
    node_list=weakly_connected_component_subgraphs_nodes[i]
    node_alpha=nodes_color_alpha[i]
    if len(weakly_connected_component_subgraphs_edges)<1 :
        # edge_list=[]
        nx.draw(G,pos,nodelist=node_list,with_labels=True,node_size=500,alpha=node_alpha)
        nx.draw_networkx_nodes(G,pos,nodelist=nx.isolates(G),with_labels=True,node_size=500,node_color='w')
        # nx.draw_networkx_nodes(G,pos,nodelist=l0,with_labels=True,node_size=500,node_color='w')
        # nx.draw_networkx_nodes(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3)
        nx.draw(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3)

        # edge_color=colors_of_edges[i]

        # edge_alpha=edges_color_alpha[i]
        # edge_width=edge_width_l[i]
    else:
        edge_list=weakly_connected_component_subgraphs_edges[i]
        edge_color=colors_of_edges[i]
        # node_alpha=nodes_color_alpha[i]
        edge_alpha=edges_color_alpha[i]
        edge_width=edge_width_l[i]
        node_list=weakly_connected_component_subgraphs_nodes[i]


        nx.draw(G,pos,nodelist=node_list,with_labels=True,node_size=500,edgelist=edge_list,edge_color=edge_color,width=edge_width,alpha=node_alpha,edgealpha=edge_alpha)
        nx.draw_networkx_nodes(G,pos,nodelist=nx.isolates(G),with_labels=True,node_size=500,node_color='w')
        # nx.draw_networkx_nodes(G,pos,nodelist=l0,with_labels=True,node_size=500,node_color='w')
        # nx.draw_networkx_nodes(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3)
        nx.draw(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3) #edge_color='k',
        # nx.draw(G,pos,nodelist=N1,edgelist=N1.edges(),with_labels=True,node_size=500,node_color='r',alpha=0.3)
# plt.savefig('foo4.png')







# #### ΜΟΝΟΠΛΕΥΡΗ ΣΥΝΔΕΔΕΣΙΜΟΤΗΤΑ ΚΑΤΕΥΘΥΝΟΜΕΝΩΝ ΓΡΑΦΩΝ
#
# def unilaterally_connected_components(G):
#     graphs =sorted(nx.weakly_connected_component_subgraphs(G), key = len, reverse=True)
#     weakly_connected_component_subgraphs_nodes=[]
#     weakly_connected_component_subgraphs_edges=[]
#     for gr in range(len(graphs)):
#         graph='G' + str(gr+1)
#         if len(graphs[gr].nodes()) >1 and len(graphs[gr].edges())>0:
#             weakly_connected_component_subgraphs_nodes.append(graphs[gr].nodes())
#             weakly_connected_component_subgraphs_edges.append(graphs[gr].edges())
#     ucc=[]
#     ucce=[]
#     for i in range(len(weakly_connected_component_subgraphs_nodes)):
#         j= weakly_connected_component_subgraphs_nodes[i]
#         max_ccsn=[]
#         max_ccse=[]
#         for ki in j:
#             Tki = nx.dfs_tree(G,ki)
#             if len(Tki.nodes()) > len(max_ccsn):
#                 max_ccsn=Tki.nodes()
#                 max_ccse=Tki.edges()
#                 max_ki=ki
#         rkwcc=list(set(j)-set(max_ccsn))
#         if len(rkwcc)==0:
#             ucc.append(max_ccsn)
#             ucce.append(max_ccse)
#         else:
#             ucc.append(max_ccsn)
#             ucce.append(max_ccse)
#             ccsn=set()
#             ccse=set()
#             for kki in rkwcc:
#                 Tkki = nx.dfs_tree(G,kki)
#                 if Tkki.nodes() not in ucc:
#                     ucc.append(Tkki.nodes())
#                     ucce.append(Tkki.edges())
#     return ucc, ucce
#
# #### ΑΝΑΖΗΤΗΣΗ
#
# number_of_components=10
# size_of_component=10
# counte=0
# mmin=1000
# # mmin=1000
# while True:
#     # G = nx.erdos_renyi_graph(20,0.07,directed=True)
#     G = nx.gnm_random_graph(25,35,directed=True)
#     # pos=nx.spring_layout(G,k=0.15,iterations=10)
#     # print counte
#     if counte== mmin:
#         print counte,'a'
#         mmin+=1000
#         # mmin+=1000
#     ucc, ucce = unilaterally_connected_components(G)
#     testy=ucc
#     # print testy
#     uu=0
#     for g in testy:
#         if len(g)>=size_of_component:
#             uu+=1
#     if uu>=number_of_components:
#         break
#     else:
#         counte+=1
#         continue
#
# print str(" ")
# print G.name
# print str(" ")
#
# G.remove_nodes_from(nx.isolates(G))
#
# print 'Number of strongly connected components:', nx.number_strongly_connected_components(G)
# print 'Number of weakly connected components:', nx.number_weakly_connected_components(G)
# print str(" ")
#
# print 'Number of unilaterally connected components:', len(ucc)
# print str(" ")
#
# print 'Unilaterally connected components (UCC):'
# for i in range(len(ucc)):
#     print 'UCC', str(i+1)+':', ucc[i]
# print str(" ")
#
# print 'Edges in unilaterally connected components:'
# for i in range(len(ucce)):
#     print 'Edges in UCC', str(i+1)+':', ucce[i]
# print str(" ")






#### ΕΛΚΥΣΤΙΚΕΣ ΣΥΝΙΣΤΩΣΕΣ ΚΑΤΕΥΘΥΝΟΜΕΝΩΝ ΓΡΑΦΩΝ

# G = nx.erdos_renyi_graph(20,0.07,directed=True)
# G = nx.gnm_random_graph(20,25,directed=True)
# G = nx.gnp_random_graph(20,0.1,directed=True)
# G = nx.erdos_renyi_graph(50,0.1,directed=True)
# G = nx.erdos_renyi_graph(20,0.045,directed=True)



#### ΑΝΑΖΗΤΗΣΗ

number_of_components=3
size_of_component=3
counte=0
mmin=1000
while True:
    G = nx.gnm_random_graph(30,25,directed=True)
    # G = nx.erdos_renyi_graph(15,0.07,directed=True)
    # G = nx.gnp_random_graph(20,0.1,directed=True)
    # pos=nx.spring_layout(G,k=0.15,iterations=10)
    if counte== mmin:
        print counte,'c'
        mmin+=1000
    testy=nx.attracting_components(G)
    # print testy
    uu=0
    for g in testy:
        if len(g)>=size_of_component:
            uu+=1
    if uu>=number_of_components:
        break
    else:
        counte+=1
        continue



pos=nx.spring_layout(G,k=0.15,iterations=10)
# pos=nx.graphviz_layout(G)
# pos=layout(G)

G.remove_nodes_from(nx.isolates(G))

print str(" ")
print 'ATTRACTING CONNECTEDNESS OF DIRECTED GRAPHS'
print str(" ")

print str(" ")
print G.name
print str(" ")

print 'Does the graph G consist of a single attracting component?', nx.is_attracting_component(G)
print 'The number of attracting components of G is:', nx.number_attracting_components(G)
print str(" ")

print 'List of attracting components:'
print sorted(nx.attracting_components(G), key = len, reverse=True)
print str(" ")

lc=sorted(nx.strongly_connected_components(G), key = len, reverse=True)
print 'List of strongly connected components:'
print lc
print str(" ")

colors_list=['c','b','g','y','k','m']
colors_to_select=list(colors_list)
graphs =sorted(nx.attracting_component_subgraphs(G), key = len, reverse=True)
attracting_component_subgraphs_edges=[]
attracting_component_subgraphs_nodes=[]
nodes_color_alpha=[]
edges_color_alpha=[]
colors_of_edges=[]
edge_width_l=[]
attracting_component_subgraphs_edges_one_mode=[]
attracting_component_subgraphs_nodes_one_mode=[]
nodes_color_alpha=[]
edges_color_alpha=[]
colors_of_edges=[]
edge_width_l=[]
graphs_labels=dict()
graphs_lists=dict()
for gr in range(len(graphs)):
    graph='G' + str(gr+1)
    # print 'Nodes of attracting component', graph+':', graphs[gr].nodes()
    # print 'Edges of attracting component', graph+':', graphs[gr].edges()
    tem='['
    ttem=[]
    for nd in graphs[gr].nodes():
        tem+='%s, ' %nd
        ttem.append(nd)
    tem =tem[:-2]+']'
    graphs_labels[gr]=tem
    graphs_lists[gr]=ttem
    if len(graphs[gr].nodes()) >1 and len(graphs[gr].edges())>0:
        attracting_component_subgraphs_edges.append(graphs[gr].edges())
        attracting_component_subgraphs_nodes.append(graphs[gr].nodes())
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
    elif len(graphs[gr].nodes()) ==1 and len(graphs[gr].edges())==0:
        # attracting_component_subgraphs_edges.append(graphs[gr].edges())
        attracting_component_subgraphs_nodes_one_mode.append(graphs[gr].nodes())
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
if len(attracting_component_subgraphs_nodes)==0:
    attracting_component_subgraphs_nodes=attracting_component_subgraphs_nodes_one_mode
# print str(" ")

colors_list=['c','b','g','y','k','m']
colors_to_select=list(colors_list)
graphs =sorted(nx.attracting_component_subgraphs(G), key = len, reverse=True)
attracting_component_subgraphs_edges=[]
attracting_component_subgraphs_nodes=[]
nodes_color_alpha=[]
edges_color_alpha=[]
colors_of_edges=[]
edge_width_l=[]
attracting_component_subgraphs_edges_one_mode=[]
attracting_component_subgraphs_nodes_one_mode=[]
nodes_color_alpha=[]
edges_color_alpha=[]
colors_of_edges=[]
edge_width_l=[]
graphs_labels=dict()
for gr in range(len(graphs)):
    graph='G' + str(gr+1)
    print 'Nodes of attracting component', graph+':', graphs[gr].nodes()
    print 'Edges of attracting component', graph+':', graphs[gr].edges()
    tem='['
    for nd in graphs[gr].nodes():
        tem+='%s, ' %nd
    tem =tem[:-2]+']'
    graphs_labels[gr]=tem
    if len(graphs[gr].nodes()) >1 and len(graphs[gr].edges())>0:
        attracting_component_subgraphs_edges.append(graphs[gr].edges())
        attracting_component_subgraphs_nodes.append(graphs[gr].nodes())
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
    elif len(graphs[gr].nodes()) ==1 and len(graphs[gr].edges())==0:
        # strongly_connected_component_subgraphs_edges.append(graphs[gr].edges())
        attracting_component_subgraphs_nodes_one_mode.append(graphs[gr].nodes())
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
if len(attracting_component_subgraphs_nodes)==0:
    attracting_component_subgraphs_nodes=attracting_component_subgraphs_nodes_one_mode
print str(" ")

Gac=sorted(nx.attracting_component_subgraphs(G), key = len, reverse=True)
Ggac=Gac[0]
graph='Ggac'
print 'Nodes of giant attracting component', graph+':', Ggac.nodes()
print 'Edges of giant attracting component', graph+':', Ggac.edges()
print str(" ")

print 'Isolated nodes:', nx.isolates(G)
print str(" ")
# l0out = [k for k,v in G.out_degree().iteritems() if v == 0]

n1=list(set(G.nodes()) - set(Ggac.nodes()) - set(nx.isolates(G)))
print 'Non-isolated nodes outside the giant strongly connected component:', n1
# print 'D-Non-isolated nodes outside the giant strongly connected component:', nD1

N1=G.subgraph(n1)
print 'Edges among non-isolated nodes outside the giant attracting component:', N1.edges()
print str(" ")

plt.figure()

# plt.title('Attracting connected components of a directed graph')
for i in range(len(attracting_component_subgraphs_nodes)):
    node_list=attracting_component_subgraphs_nodes[i]
    node_alpha=nodes_color_alpha[i]
    if len(attracting_component_subgraphs_edges)<1 :
        # edge_list=[]
        nx.draw(G,pos,nodelist=node_list,with_labels=True,node_size=500,alpha=node_alpha)
        nx.draw_networkx_nodes(G,pos,nodelist=nx.isolates(G),with_labels=True,node_size=500,node_color='w')
        # nx.draw_networkx_nodes(G,pos,nodelist=l0,with_labels=True,node_size=500,node_color='w')
        # nx.draw_networkx_nodes(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3)
        nx.draw(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3)

        # edge_color=colors_of_edges[i]

        # edge_alpha=edges_color_alpha[i]
        # edge_width=edge_width_l[i]
    else:
        edge_list=attracting_component_subgraphs_edges[i]
        edge_color=colors_of_edges[i]
        # node_alpha=nodes_color_alpha[i]
        edge_alpha=edges_color_alpha[i]
        edge_width=edge_width_l[i]
        node_list=attracting_component_subgraphs_nodes[i]


        nx.draw(G,pos,nodelist=node_list,with_labels=True,node_size=500,edgelist=edge_list,edge_color=edge_color,width=edge_width,alpha=node_alpha,edgealpha=edge_alpha)
        nx.draw_networkx_nodes(G,pos,nodelist=nx.isolates(G),with_labels=True,node_size=500,node_color='w')
        # nx.draw_networkx_nodes(G,pos,nodelist=l0,with_labels=True,node_size=500,node_color='w')
        # nx.draw_networkx_nodes(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3)
        nx.draw(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3) #edge_color='k',
        # nx.draw(G,pos,nodelist=N1,edgelist=N1.edges(),with_labels=True,node_size=500,node_color='r',alpha=0.3)
# plt.savefig('foo5.png



colors_list=['c','b','g','y','k','m']
colors_to_select=list(colors_list)
graphs =sorted(nx.strongly_connected_component_subgraphs(G), key = len, reverse=True)
strongly_connected_component_subgraphs_edges=[]
strongly_connected_component_subgraphs_nodes=[]
nodes_color_alpha=[]
edges_color_alpha=[]
colors_of_edges=[]
edge_width_l=[]
strongly_connected_component_subgraphs_edges_one_mode=[]
strongly_connected_component_subgraphs_nodes_one_mode=[]
nodes_color_alpha=[]
edges_color_alpha=[]
colors_of_edges=[]
edge_width_l=[]
graphs_labels=dict()
graphs_lists=dict()
for gr in range(len(graphs)):
    graph='G' + str(gr+1)
    # print 'Nodes of strongly connected component', graph+':', graphs[gr].nodes()
    # print 'Edges of strongly connected component', graph+':', graphs[gr].edges()
    tem='['
    ttem=[]
    for nd in graphs[gr].nodes():
        tem+='%s, ' %nd
        ttem.append(nd)
    tem =tem[:-2]+']'
    graphs_labels[gr]=tem
    graphs_lists[gr]=ttem
    if len(graphs[gr].nodes()) >1 and len(graphs[gr].edges())>0:
        strongly_connected_component_subgraphs_edges.append(graphs[gr].edges())
        strongly_connected_component_subgraphs_nodes.append(graphs[gr].nodes())
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
    elif len(graphs[gr].nodes()) ==1 and len(graphs[gr].edges())==0:
        # strongly_connected_component_subgraphs_edges.append(graphs[gr].edges())
        strongly_connected_component_subgraphs_nodes_one_mode.append(graphs[gr].nodes())
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
if len(strongly_connected_component_subgraphs_nodes)==0:
    strongly_connected_component_subgraphs_nodes=strongly_connected_component_subgraphs_nodes_one_mode
# print str(" ")

Gcc=sorted(nx.strongly_connected_component_subgraphs(G), key = len, reverse=True)
Ggc=Gcc[0]
graph='Ggc'
print 'Nodes of giant strongly connected component', graph+':', Ggc.nodes()
print 'Edges of giant strongly connected component', graph+':', Ggc.edges()
print str(" ")

print 'Isolated nodes:', nx.isolates(G)
print str(" ")
# l0out = [k for k,v in G.out_degree().iteritems() if v == 0]

n1=list(set(G.nodes()) - set(Ggc.nodes()) - set(nx.isolates(G)))
print 'Non-isolated nodes outside the giant strongly connected component:', n1
# print 'D-Non-isolated nodes outside the giant strongly connected component:', nD1

N1=G.subgraph(n1)
print 'Edges among non-isolated nodes outside the giant strongly connected component:', N1.edges()
print str(" ")

plt.figure()

# plt.title('Strongly connected components of a directed graph')
for i in range(len(strongly_connected_component_subgraphs_nodes)):
    node_list=strongly_connected_component_subgraphs_nodes[i]
    node_alpha=nodes_color_alpha[i]
    if len(strongly_connected_component_subgraphs_edges)<1:
        nx.draw(G,pos,nodelist=node_list,with_labels=True,node_size=500,alpha=node_alpha)
        nx.draw_networkx_nodes(G,pos,nodelist=nx.isolates(G),with_labels=True,node_size=500,node_color='w')
        nx.draw_networkx_nodes(G,pos,nodelist=l0,with_labels=True,node_size=500,node_color='w')
        nx.draw_networkx_nodes(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3)
        nx.draw(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3)
    else:
        edge_list=strongly_connected_component_subgraphs_edges[i]
        edge_color=colors_of_edges[i]

        edge_alpha=edges_color_alpha[i]
        edge_width=edge_width_l[i]

        nx.draw(G,pos,nodelist=node_list,with_labels=True,node_size=500,edgelist=edge_list,edge_color=edge_color,width=edge_width,alpha=node_alpha,edgealpha=edge_alpha)
        nx.draw_networkx_nodes(G,pos,nodelist=nx.isolates(G),with_labels=True,node_size=500,node_color='w')
        # nx.draw_networkx_nodes(G,pos,nodelist=l0,with_labels=True,node_size=500,node_color='w')
        # nx.draw_networkx_nodes(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3)
        nx.draw(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3) #edge_color='k',
        # nx.draw(G,pos,nodelist=N1,edgelist=N1.edges(),with_labels=True,node_size=500,node_color='r',alpha=0.3)
# plt.savefig('foo2.png')

S=nx.condensation(G)
condensation_graph_relabeled=nx.relabel_nodes(S,graphs_labels,copy=True)
posS=nx.spring_layout(condensation_graph_relabeled,k=0.15,iterations=10)
# posS=layout(condensation_graph_relabeled)

# lvl=[]
# print condensation_graph_relabeled.nodes(),'ssssssss'
# for i in range(len(condensation_graph_relabeled.nodes())):
#     lvl.append(len(eval(condensation_graph_relabeled.nodes()[i])))
    # lvl.append(len(condensation_graph_relabeled.nodes()[i]))

# lvl2=[]
# for i in graphs_lists:
#     lvl2.append(len(graphs_lists[i]))

# print 'condensation_graph_relabeled nodes'
# print condensation_graph_relabeled.nodes()

lvl2=[]
for i in graphs_lists:
    # lvl2.append(len(condensation_graph_relabeled.nodes()[i]))
    lvl2.append(len(eval(condensation_graph_relabeled.nodes()[i])))

# print lvl2
# print 'List of strongly connected components:'
# print lc
# print 'graphs_labels'
# print graphs_labels
# print 'Nodes of S'
# print S.nodes()
# print 'Nodes of condensation_graph_relabeled:'
# print condensation_graph_relabeled.nodes()
# print 'Print list of values lengths'
# # print lvl
# print lvl2

plt.figure()

# plt.title('Condensation graph of the strongly connected components of a directed graph')
nx.draw(condensation_graph_relabeled,pos=posS,font_size=16,with_labels=False,node_size=[v * 100 for v in lvl2],node_color='g')
for p in posS:  # raise text positions
        posS[p][1] += 0.04 #offset 0.07
nx.draw_networkx_labels(condensation_graph_relabeled,posS)
# plt.savefig('foo3.png')









### ΔΙΣΥΝΔΕΣΙΜΟΤΗΤΑ ΜΗ ΚΑΤΕΥΘΥΝΟΜΕΝΩΝ ΓΡΑΦΩΝ

# G = nx.barbell_graph(4,2)
#
#
# # G=nx.Graph()
# # G.add_edges_from([(0,1),(1,2),(2,0),(3,4)])
# # G.add_node(5)
# # pos={0:(0,0),1:(0,1),2:(0.5,1),3:(0.5,0),4:(1,0),5:(0.75,0.5)}
#
#
G = nx.gnp_random_graph(20,0.1)
# G = nx.gnp_random_graph(15,0.04)
# G = nx.gnm_random_graph(15,10)
# # G = nx.barabasi_albert_graph(50,2)
# # G = nx.newman_watts_strogatz_graph(20,2,0.9)
# # G.add_node(55)
# # G.add_edges_from([(50,51),(51,52),(52,50),(53,54)])
#
# # G = nx.erdos_renyi_graph(15,0.06)
# pos=nx.spring_layout(G,k=0.15,iterations=10)
# # pos=nx.graphviz_layout(G)
# # pos=layout(G)



##### ΑΝΑΖΗΤΗΣΗ

number_of_biconnected_components=2
size_of_component=3
counte=0
mmin=1000
while True:
    # G = nx.erdos_renyi_graph(30,0.024)
    G = nx.gnp_random_graph(30,0.15)
    # G = nx.gnp_random_graph(15,0.04)
    if counte== mmin:
        print counte
        mmin+=1000
    # print nx.is_biconnected(G)
    # if nx.is_biconnected(G)==False:
    #     continue
    testy=sorted(nx.biconnected_components(G), key = len, reverse=True)
    # print testy
    uu=0
    for g in testy:
        if len(g)>=size_of_component:
            uu+=1
    if uu>=number_of_biconnected_components:
        break
    else:
        counte+=1
        continue
    # print counte,'a'



pos=nx.spring_layout(G,k=0.15,iterations=10)

print str(" ")
print 'BICONNECTEDNESS OF UNDIRECTED GRAPHS'
print str(" ")

G.remove_nodes_from(nx.isolates(G))
lc=sorted(nx.biconnected_components(G), key = len, reverse=True)

print str(" ")
print G.name
print str(" ")

print 'Is graph G biconnected?', nx.is_biconnected(G)
print 'Is graph G connected?', nx.is_connected(G)
print 'The number of biconnected components of G is:', len(lc)
print 'The number of connected components of G is:', nx.number_connected_components(G)
print str(" ")

print 'List of biconnected components:'
print lc
print str(" ")

deg=G.degree()
deg_dic=[]
for nd in deg:
    if deg[nd]>0:
        deg_dic.append(nd)
node0 = random.choice(deg_dic)

for i in range(len(lc)):
    if node0 in lc[i] :
        print 'The nodes in the biconnected component of graph containing the randomly chosen node ' + str(node0) + ' are: \n', lc[i]
        # break
print str(" ")

colors_list=['c','b','g','y','k','m']
colors_to_select=list(colors_list)
graphs =sorted(nx.biconnected_component_subgraphs(G), key = len, reverse=True)
biconnected_component_subgraphs_edges=[]
biconnected_component_subgraphs_nodes=[]
nodes_color_alpha=[]
edges_color_alpha=[]
colors_of_edges=[]
edge_width_l=[]
for gr in range(len(graphs)):
    graph='G' + str(gr+1)
    # print 'Nodes of biconnected component', graph+':', graphs[gr].nodes()
    # print 'Edges of biconnected component', graph+':', graphs[gr].edges()
    if len(graphs[gr].nodes()) >1 and len(graphs[gr].edges())>0:
        biconnected_component_subgraphs_edges.append(graphs[gr].edges())
        biconnected_component_subgraphs_nodes.append(graphs[gr].nodes())
        if len(colors_to_select)==0:
            colors_to_select=list(colors_list)
        color=random.choice(colors_to_select)
        colors_to_select.remove(color)
        colors_of_edges.append((color))
        nodes_color_alpha.append(0.4)
        edges_color_alpha.append(0.6)
        edge_width_l.append(4.0)
        # if gr==0:
        #     colors_of_edges.append('r')
        #     nodes_color_alpha.append(1)
        #     edges_color_alpha.append(1)
        #     edge_width_l.append(6.0)
        # else:
        #     if len(colors_to_select)==0:
        #         colors_to_select=list(colors_list)
        #     color=random.choice(colors_to_select)
        #     colors_to_select.remove(color)
        #     colors_of_edges.append((color))
        #     nodes_color_alpha.append(0.4)
        #     edges_color_alpha.append(0.6)
        #     edge_width_l.append(4.0)
# print str(" ")

# Gcc=sorted(nx.biconnected_connected_component_subgraphs(G), key = len, reverse=True)
# Ggc=Gcc[0]
# graph='Ggc'
# print 'Nodes of giant connected component', graph+':', Ggc.nodes()
# print 'Edges of giant connected component', graph+':', Ggc.edges()
# print str(" ")

print 'The biconnected component edges of G are:', list(nx.biconnected_component_edges(G))
print str(" ")

print 'The articulation points of G are:', set(nx.articulation_points(G))
print str(" ")

print 'Isolated nodes:', nx.isolates(G)
print str(" ")

# n1=list(set(G.nodes()) - set(Ggc.nodes()) - set(nx.isolates(G)))
# print 'Non-isolated nodes outside the giant connected component:', n1

# N1=G.subgraph(n1)
# print 'Edges among non-isolated nodes outside the giant connected component:', N1.edges()


plt.figure()

# plt.title('Biconnected components of an undirected graph')
for i in range(len(biconnected_component_subgraphs_nodes)):
    node_list=biconnected_component_subgraphs_nodes[i]
    edge_list=biconnected_component_subgraphs_edges[i]
    edge_color=colors_of_edges[i]
    node_alpha=nodes_color_alpha[i]
    edge_alpha=edges_color_alpha[i]
    edge_width=edge_width_l[i]

    nx.draw(G,pos,nodelist=node_list,with_labels=True,node_size=500,edgelist=edge_list,edge_color=edge_color,width=edge_width,alpha=node_alpha,edgealpha=edge_alpha)
    nx.draw_networkx_nodes(G,pos,nodelist=nx.isolates(G),with_labels=True,node_size=500,node_color='w')
# plt.savefig('foo1.png')


plt.show()
