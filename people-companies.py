# -*- coding: utf-8 -*-
"""
    @author: Moses Boudourides
    """


import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

J=nx.erdos_renyi_graph(5,0.75)
persons = {0:"John",1:"Mary",2:"Tom",3:"Jane",4:"Peter"}
posJ=nx.spring_layout(J)
plt.figure()
nx.draw(J,pos=posJ,node_color='r',node_size=1000,font_size=10,font_color='#FFFFFF',with_labels=False)
nx.draw_networkx_labels(J,posJ,persons,font_size=10,font_color='#FFFFFF')

F=nx.erdos_renyi_graph(6,0.6)
companies={0:"IBM",1:"McIntosh",2:"Xerox",3:"Samsung",4:"Microsoft",5:"Dell"}
posF=nx.spring_layout(F)
plt.figure()
nx.draw(F,pos=posF,node_color='b',node_size=1800,font_size=10,font_color='#FFFFFF',node_shape='s',with_labels=False)
nx.draw_networkx_labels(F,posF,companies,font_size=10,font_color='#FFFFFF')

H=nx.bipartite_random_graph(5,6,0.55)
posH={0:(0,0),1:(0,2),2:(0,4),3:(0,6),4:(0,8),5:(1,-2),6:(1,0),7:(1,2),8:(1,4),9:(1,6),10:(1,8)}
mode1, mode2 = bipartite.sets(H)
labels = {0:"John",1:"Mary",2:"Tom",3:"Jane",4:"Peter",5:"IBM",6:"McIntosh",7:"Xerox",8:"Samsung",9:"Microsoft",10:"Dell"}
plt.figure(facecolor='w')
nx.draw_networkx_nodes(H,pos=posH,nodelist=list(mode1),node_color='r',node_size=1000)
nx.draw_networkx_nodes(H,pos=posH,nodelist=list(mode2),node_color='b',node_size=1800,node_shape='s')
nx.draw_networkx_edges(H,pos=posH)
nx.draw_networkx_labels(H,posH,labels,font_size=10,font_color='#FFFFFF')
plt.axis('off')

G=nx.Graph()
for node in J.nodes():
    G.add_node(node,bipartite=0)
for edge in J.edges():
    G.add_edge(edge[0],edge[1])
for edge in F.edges():
    G.add_edge(edge[0]+5,edge[1]+5)
for node in F.nodes():
    G.add_node(node+5,bipartite=1)
for edge in H.edges(data=True):
    G.add_edge(edge[0],edge[1])
pos=nx.spring_layout(G)
top_set=set()
botom_set=set()
for i in pos:
    npos=pos[i]
    if G.node[i]['bipartite']==0:
        pos[i]=[npos[0],npos[1]+2]
        top_set.add(i)
    elif G.node[i]['bipartite']==1:
        pos[i]=[npos[0],npos[1]-2]
        botom_set.add(i)


plt.figure()
nx.draw(G,pos,nodelist=list(top_set),node_color='r',node_size=1000,with_labels=False)
nx.draw(G,pos,nodelist=list(botom_set),node_color='b',node_size=1800,node_shape='s',with_labels=False)
nx.draw_networkx_labels(G,pos,labels,font_size=10,font_color='#FFFFFF')

fig = plt.figure(figsize=(13,13))
plt.subplot(2,2,1).set_title("Graph of Persons")
nx.draw(J,pos=posJ,node_color='r',node_size=1000,font_size=10,font_color='#FFFFFF',with_labels=False)
nx.draw_networkx_labels(J,posJ,persons,font_size=10,font_color='#FFFFFF')
plt.axis("tight")
plt.subplot(2,2,2).set_title("Graph of Companies")
nx.draw(F,pos=posF,node_color='b',node_size=1800,font_size=10,font_color='#FFFFFF',node_shape='s',with_labels=False)
nx.draw_networkx_labels(F,posF,companies,font_size=10,font_color='#FFFFFF')
plt.axis("tight")
#plt.figure(facecolor='w')
plt.subplot(2,2,3).set_title("Bipartite Graph of Persons and Companies")
nx.draw_networkx_nodes(H,pos=posH,nodelist=list(mode1),node_color='r',node_size=1000)
nx.draw_networkx_nodes(H,pos=posH,nodelist=list(mode2),node_color='b',node_size=1800,node_shape='s')
nx.draw_networkx_edges(H,pos=posH)
nx.draw_networkx_labels(H,posH,labels,font_size=10,font_color='#FFFFFF')
plt.axis('off')
plt.axis("tight")
plt.subplot(2,2,4).set_title("Two-Level Graph of Persons and Companies")
nx.draw(G,pos,nodelist=list(top_set),node_color='r',node_size=1000,with_labels=False)
nx.draw(G,pos,nodelist=list(botom_set),node_color='b',node_size=1800,node_shape='s',with_labels=False)
nx.draw_networkx_labels(G,pos,labels,font_size=10,font_color='#FFFFFF')
plt.axis("tight")

plt.show()