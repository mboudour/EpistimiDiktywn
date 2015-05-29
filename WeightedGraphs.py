# encoding: utf-8

'''
Created by Sergios Lenis & Moses Boudourides
sergioslenis@gmail.com & Moses.Boudourides@gmail.com
'''

import networkx as nx
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.colors as colors
import colorBar

n=30
p=0.15
G = nx.erdos_renyi_graph(n,p)
pos=nx.spring_layout(G)
#pos =nx.circular_layout(G)

####### Integer Vertex Weights
barInt=20
barRange=range(barInt)
nod_dic=dict()
my_cmap=cm.get_cmap(name='hsv')
norm = mpl.colors.Normalize(barRange)
scalarMap = cm.ScalarMappable(norm=norm,cmap=my_cmap)
for i in G.nodes():
    G.node[i]['barKor']=random.randrange(0,barInt)
    nod_dic[i]=G.node[i]['barKor']

'''
    barKorifes=True
    nod_dic=dict()
    barArxi=0.
    barTel=50.
    my_cmap=colorBar.cororBar()
    norm = mpl.colors.Normalize(barArxi,barTel)
    scalarMap = cm.ScalarMappable(norm=norm, cmap=my_cmap)
    
    for i in G.nodes():
    G.node[i]['barKor']=random.uniform(barArxi,barTel)
    nod_dic[i]=G.node[i]['barKor']
'''

plt.figure()
plt.axes([0.1,0.1,.8,.8])
nx.draw(G,pos, with_labels=True,nodelist=nod_dic.keys(),node_color=nod_dic.values(),cmap=my_cmap)
ax=plt.axes([0.05, 0.10, 0.9, 0.02])
mpl.colorbar.ColorbarBase(ax,norm=norm,cmap=my_cmap,orientation='horizontal')
plt.show()

###### Arithmitika bari akmes

#For integer values of edge weights, activate the following 10 lines
'''
barAkmes=True
edge_dic=dict()
barInt=4
barRange=range(barInt)
my_cmap=cm.get_cmap(name='hsv')
for edg in G.edges():
    ed=edg[0]
    de=edg[1]
    G.edge[ed][de]['barAkm']=random.randrange(0,barInt)
    edge_dic[(ed,de)]=G.edge[ed][de]['barAkm']
'''

### Eisagogi pragmatikoy apo diastima

#For real numerical values of edge weights, activate the following 9 lines:
'''
barArxi=1.
barTel=2.

#my_cmap=colorBar.cororBar()
#my_cmap = mpl.cm.cool
#colors = range(barArxi,barTel)

my_cmap = plt.get_cmap('jet')
norm = mpl.colors.Normalize(vmin=barArxi, vmax=barTel)
scalarMap = cm.ScalarMappable(norm=norm, cmap=my_cmap)

edge_dic=dict()
for edg in G.edges():
    ed=edg[0]
    de=edg[1]
    G.edge[ed][de]['barAkm']=random.uniform(barArxi,barTel)
    edge_dic[(ed,de)]=G.edge[ed][de]['barAkm']

#To plot the edge-weighted graphs activate the following 3 lines:

plt.figure()
plt.axes([0.1,0.1,.8,.8])

edges = nx.draw(G,pos, with_labels=True,edgelist=edge_dic.keys(),edge_color=edge_dic.values(),cmap=my_cmap, width=3, alpha=0.65)

ax=plt.axes([0.05, 0.10, 0.9, 0.02])
mpl.colorbar.ColorbarBase(ax,cmap=my_cmap,norm=norm,orientation='horizontal')

plt.show()

#plt.subplot(2, 1, 1)
#[0.1,0.1,.8,.8]
#nx.draw(G,pos, with_labels=True,nodelist=nod_dic.keys(),node_color=nod_dic.values(),cmap=my_cmap)
#edges = nx.draw(G,pos, with_labels=True,edgelist=edge_dic.keys(),edge_color=colors)
#plt.subplot(2, 1, 2)
#fig=plt.figure(figsize=(8,3))
#ax = fig.add_axes([0.05, 0.80, 0.9, 0.15])

#plt.colorbar(edges)
#plt.axis('off')
'''


#*************************+++++++++++****************
#den exo kataferei na doulepsei akoma
#atr_list=nx.attr_matrix(G,edge_attr='barAkm')#,normalized=True,rc_order=sorted(G.nodes()))
#print atr_list[0]
#colorBar.drawScat(atr_list[0],my_cmap)

