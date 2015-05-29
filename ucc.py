# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import random

# G=nx.DiGraph()
# G.add_edges_from([(1,2),(2,3),(4,5),(5,6),(7,6),(3,10),(10,1),(2,11),(11,9),(9,11)])
# G = nx.gnm_random_graph(25,35,directed=True)
# G = nx.erdos_renyi_graph(30,0.02,directed=True)

# pos=nx.spring_layout(G,k=0.15,iterations=10)


def unilaterally_connected_components(G):
    graphs =sorted(nx.weakly_connected_component_subgraphs(G), key = len, reverse=True)
    weakly_connected_component_subgraphs_nodes=[]
    weakly_connected_component_subgraphs_edges=[]
    for gr in range(len(graphs)):
        graph='G' + str(gr+1)
        if len(graphs[gr].nodes()) >1 and len(graphs[gr].edges())>0:
            weakly_connected_component_subgraphs_nodes.append(graphs[gr].nodes())
            weakly_connected_component_subgraphs_edges.append(graphs[gr].edges())
    ucc=[]
    ucce=[]
    for i in range(len(weakly_connected_component_subgraphs_nodes)):
        j= weakly_connected_component_subgraphs_nodes[i]
        max_ccsn=[]
        max_ccse=[]
        for ki in j:
            Tki = nx.dfs_tree(G,ki)
            if len(Tki.nodes()) > len(max_ccsn):
                max_ccsn=Tki.nodes()
                max_ccse=Tki.edges()
                max_ki=ki
        rkwcc=list(set(j)-set(max_ccsn))
        if len(rkwcc)==0:
            ucc.append(max_ccsn)
            ucce.append(max_ccse)
        else:
            ucc.append(max_ccsn)
            ucce.append(max_ccse)
            ccsn=set()
            ccse=set()
            for kki in rkwcc:
                Tkki = nx.dfs_tree(G,kki)
                if Tkki.nodes() not in ucc:
                    ucc.append(Tkki.nodes())
                    ucce.append(Tkki.edges())
    return ucc, ucce



# graphs =sorted(nx.weakly_connected_component_subgraphs(G), key = len, reverse=True)
# weakly_connected_component_subgraphs_nodes=[]
# weakly_connected_component_subgraphs_edges=[]
# for gr in range(len(graphs)):
#     graph='G' + str(gr+1)
#     if len(graphs[gr].nodes()) >1 and len(graphs[gr].edges())>0:
#         weakly_connected_component_subgraphs_nodes.append(graphs[gr].nodes())
#         weakly_connected_component_subgraphs_edges.append(graphs[gr].edges())
#
# # print 'Weakly connected components:'
# # print list(weakly_connected_component_subgraphs_nodes)
# # print str(" ")
#
# # print 'Graph edges:'
# # for i in range(len(G.edges())):
# #     print G.edges()[i]
# # print str(" ")
#
# ucc=[]
# ucce=[]
#
# for i in range(len(weakly_connected_component_subgraphs_nodes)):
#     j= weakly_connected_component_subgraphs_nodes[i]
#     max_ccsn=[]
#     max_ccse=[]
#     for ki in j:
#         Tki = nx.dfs_tree(G,ki)
#         if len(Tki.nodes()) > len(max_ccsn):
#             max_ccsn=Tki.nodes()
#             max_ccse=Tki.edges()
#             max_ki=ki
#     rkwcc=list(set(j)-set(max_ccsn))
#     if len(rkwcc)==0:
#         ucc.append(max_ccsn)
#         ucce.append(max_ccse)
#     else:
#         ucc.append(max_ccsn)
#         ucce.append(max_ccse)
#         ccsn=set()
#         ccse=set()
#         for kki in rkwcc:
#             Tkki = nx.dfs_tree(G,kki)
#             if Tkki.nodes() not in ucc:
#                 ucc.append(Tkki.nodes())
#                 ucce.append(Tkki.edges())


#### ΑΝΑΖΗΤΗΣΗ

number_of_components=3
size_of_component=3
counte=0
mmin=1000
# mmin=1000
while True:
    # G = nx.erdos_renyi_graph(20,0.07,directed=True)
    G = nx.gnm_random_graph(8,5,directed=True)
    # pos=nx.spring_layout(G,k=0.15,iterations=10)
    # print counte
    if counte== mmin:
        print counte,'a'
        mmin+=1000
        # mmin+=1000
    ucc, ucce = unilaterally_connected_components(G)
    testy=ucc
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

print str(" ")
print G.name
print str(" ")

G.remove_nodes_from(nx.isolates(G))

print 'Number of strongly connected components:', nx.number_strongly_connected_components(G)
print 'Number of weakly connected components:', nx.number_weakly_connected_components(G)
print str(" ")

print 'Number of unilaterally connected components:', len(ucc)
print str(" ")

print 'Unilaterally connected components (UCC):'
for i in range(len(ucc)):
    print 'UCC', str(i+1)+':', ucc[i]
print str(" ")

print 'Edges in unilaterally connected components:'
for i in range(len(ucce)):
    print 'Edges in UCC', str(i+1)+':', ucce[i]
print str(" ")

colors_list=['c','b','g','y','k','m']
colors_to_select=list(colors_list)
ucc_colors=[]
ucc_edges=[]
for ndd in ucce:
    if len(colors_to_select)==0:
        colors_to_select=list(colors_list)
    color=random.choice(colors_to_select)
    colors_to_select.remove(color)
    for nd in ndd:
        ucc_colors.append(color)
        ucc_edges.append(nd)
print ucc_edges,ucc_colors
colors_to_select=list(colors_list)
# graphs =sorted(nx.weakly_connected_component_subgraphs(G), key = len, reverse=True)
ucc_subgraphs_edges=[]
ucc_subgraphs_nodes=[]
nodes_color_alpha=[]
edges_color_alpha=[]
colors_of_edges=[]
edge_width_l=[]
ucc_subgraphs_edges_one_mode=[]
ucc_component_subgraphs_nodes_one_mode=[]
nodes_color_alpha=[]
edges_color_alpha=[]
colors_of_edges=[]
colors_of_nodes=[]
edge_width_l=[]
azero=None

# for gr in range(len(graphs)):
for gr in range(len(ucce)):
    graph='G' + str(gr+1)
    # print len(weakly_connected_component_subgraphs_edges),len(weakly_connected_component_subgraphs_nodes),'aaaaa',weakly_connected_component_subgraphs_nodes,weakly_connected_component_subgraphs_edges
    # if len(graphs[gr].nodes()) >1 and len(graphs[gr].edges())>0:
    #     ucc_subgraphs_edges.append(graphs[gr].edges())
    #     ucc_subgraphs_nodes.append(graphs[gr].nodes())
    if len(ucc[gr]) >1 and len(ucce[gr])>0:
        ucc_subgraphs_edges.append(ucce[gr])
        ucc_subgraphs_nodes.append(ucc[gr])
        if gr==azero:
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
        ucc_subgraphs_edges.append([])
        ucc_subgraphs_nodes_one_mode.append(graphs[gr].nodes())
        if gr==azero:
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
# if len(ucc_subgraphs_nodes)==0:
#     ucc_subgraphs_nodes=ucc_subgraphs_nodes_one_mode
# print str(" ")

# print len(ucc_subgraphs_edges),len(ucc_subgraphs_nodes)

# Gcc=sorted(nx.ucc_subgraphs(G), key = len, reverse=True)
# Ggc=Gcc[0]
# graph='Ggc'

# print 'Nodes of giant weakly connected component', graph+':', Ggc.nodes()
# print 'Edges of giant weakly connected component', graph+':', Ggc.edges()
# print str(" ")

# print 'Isolated nodes:', nx.isolates(G)
# print str(" ")

# n1=list(set(G.nodes()) - set(Ggc.nodes()) - set(nx.isolates(G)))
# print 'Non-isolated nodes outside the giant weakly connected component:', n1

# N1=G.subgraph(n1)
# print 'Edges among non-isolated nodes outside the giant weakly connected component:', N1.edges()

pos=nx.spring_layout(G,k=0.15,iterations=10)

plt.figure()

# plt.title('Weakly connected components of a directed graph')
# print len(weakly_connected_component_subgraphs_nodes)
for i in range(len(ucc_subgraphs_nodes)):
# for i in range(len(ucc)):
    # print i,len(nodes_color_alpha)
    node_list=ucc_subgraphs_nodes[i]
    node_alpha=nodes_color_alpha[i]
    # if i==0:
    #     node_alpha=nodes_color_alpha[0]
    # else:
    #     node_alpha=nodes_color_alpha[1]

    if len(ucc_subgraphs_edges)<1 :
        # edge_list=[]
        # nx.draw(G,pos,nodelist=node_list,with_labels=True,node_size=500,alpha=node_alpha)
        nx.draw_networkx_nodes(G,pos,nodelist=nx.isolates(G),with_labels=True,node_size=500,node_color='w')
        nx.draw_networkx_nodes(G,pos,edgelist=ucc_edges,with_labels=True,node_size=500,edge_color=ucc_colors)
        # nx.draw_networkx_nodes(G,pos,nodelist=l0,with_labels=True,node_size=500,node_color='w')
        # nx.draw_networkx_nodes(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3)

        # nx.draw(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3)

        # edge_color=colors_of_edges[i]

        # edge_alpha=edges_color_alpha[i]
        # edge_width=edge_width_l[i]
    # elif len(ucc)>0:

    else:
        # print i,len(weakly_connected_component_subgraphs_edges)
        edge_list=ucc_subgraphs_edges[i]
        edge_color=colors_of_edges[i]
        # node_alpha=nodes_color_alpha[i]
        edge_alpha=edges_color_alpha[i]
        edge_width=edge_width_l[i]
        node_list=ucc_subgraphs_nodes[i]


        nx.draw(G,pos,nodelist=node_list,with_labels=True,node_size=500,edgelist=edge_list,edge_color=edge_color,width=edge_width,alpha=node_alpha,edgealpha=edge_alpha)
        nx.draw_networkx_nodes(G,pos,edgelist=ucc_edges,with_labels=True,node_size=500,edge_color=ucc_colors)
        nx.draw_networkx_nodes(G,pos,nodelist=nx.isolates(G),with_labels=True,node_size=500,node_color='w')
        # nx.draw_networkx_nodes(G,pos,nodelist=l0,with_labels=True,node_size=500,node_color='w')
        # nx.draw_networkx_nodes(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3)

        # nx.draw(G,pos,nodelist=N1,with_labels=True,node_size=500,node_color='r',alpha=0.3) #edge_color='k',

        # nx.draw(G,pos,nodelist=N1,edgelist=N1.edges(),with_labels=True,node_size=500,node_color='r',alpha=0.3)
# # plt.savefig('foo4.png')

plt.show()