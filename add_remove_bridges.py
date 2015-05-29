# -*- coding: utf-8 -*-
"""
    LAST UPDATE: 24 Νοεμβρίου 2014

    @authors: Moses Boudourides & Sergios Lenis
    """


import networkx as nx
import matplotlib.pyplot as plt
from pylab import hist
import random




#### ΚΑΤΑΣΚΕΥΗ ΔΙΜΕΡΟΥΣ ΓΡΑΦΟΥ (ΓΕΦΥΡΩΝ)

def randomBipartiteGraph(n,m,nm):

    if nm>n*m:
        nm=n*m

    G=nx.Graph()
    nrange=range(n)
    mrange=range(n,m+n)
    #print nrange
    #print mrange
    #print aaa
    edg=set()
    while len(edg)<nm:
        edn=random.choice(nrange)
        edm=random.choice(mrange)
        edg.add((edn,edm))
    for ed in edg:
        G.add_edge(ed[0],ed[1])
        G.add_node(ed[0],bipartite=0)
        G.add_node(ed[1],bipartite=1)
    return G



#### Ο ΑΡΧΙΚΟΣ ΓΡΑΦΟΣ

n=7    # Πλήθος κορυφών πρώτου επιπέδου
m=70   # Πλήθος κορυφών δευτέρου επιπέδου
k=n
nm=150   # Πλήθος ακμών διμερούς γράφου (αρχικά)

p1=0.2
p2=0.3
# q=1

J=nx.erdos_renyi_graph(n,p1)
F=nx.erdos_renyi_graph(m,p2)
# J=nx.cycle_graph(n)
# F=nx.cycle_graph(m)

H=randomBipartiteGraph(n,m,nm)






#### ΠΡΟΣΘΗΚΗ-ΑΦΑΙΡΕΣΗ ΓΕΦΥΡΩΝ

#### ΣΕ ΠΟΣΟΣΤΑ

percentEdgesAdd=0.8   # Το ποσοστό (επί των αρχικών) των προστιθέμενων γεφυρών.
                    # Αν 0, καμιά γέφυρα δεν προστίθεται.
                    # Αν 1, προστίθεται το μέγιστο πλήθος γεφυρών ώστε ο διμερής γράφος να γίνει πλήρης.

if percentEdgesAdd!=None:
	edgesto=int((n*m -nm)*percentEdgesAdd)
	addEdges=edgesto

percentEdgesRemove=0.8  # Το ποσοστό (επί των αρχικών) των αφαιρούμενων γεφυρών.
                        # Αν 0, καμιά γέφυρα δεν αφαιρείται.
                        # Αν 1, αφαιρούνται όλες οι αρχικές γέφυρες ώστε ο διμερής γράφος να γίνει κενός.

if percentEdgesRemove!=None:
	edgesto=int(nm*percentEdgesRemove)
	removeEdges=edgesto

#### ΠΡΟΣΟΧΗ!!! Αν οι γέφυρες προστίθενται-αφαιρουνται σε αριθμούς, όπως στη συνέχεια, οι παραπάνω γραμμές πρέπει να είναι αδρανοποιημένες.

#### ΣΕ ΑΠΟΛΥΤΟΥΣ ΑΡΙΘΜΟΥΣ

# addEdges=15
# removeEdges=15

#### ΠΡΟΣΟΧΗ!!! Αν οι γέφυρες προστίθενται-αφαιρουνται σε ποσοστά, οι παραπάνω 2 γραμμές πρέπει να είναι αδρανοποιημένες.





print 'Number of Initial Bridges (percentage): %d (%.2f)'%(nm,float(nm*1./(n*m)))

if percentEdgesAdd!=None:
	print 'Number of Added Bridges (percentage): %d (%.2f)' %(addEdges,percentEdgesAdd)

if percentEdgesRemove!=None:
	print 'Number of Removed Bridges (percentage): %d (%.2f)'  %(removeEdges,percentEdgesRemove)






#### ΚΑΤΑΣΚΕΥΗ ΣΥΝΘΕΤΟΥ ΔΙΕΠΙΠΕΔΟΥ ΓΡΑΦΟΥ

G=nx.Graph()
Jnod=[]
G.add_nodes_from(J.nodes(),bipa=0)

Fnod=[]
Fdict=dict()
for node in F.nodes():
	Fnod.append(node+k)
	Fdict[node]=node+k
G.add_nodes_from(Fdict.values(),bipa=1)
for edge in J.edges():
	G.add_edge(edge[0],edge[1])

bipa_Edges=[]
for edge in F.edges():
	G.add_edge(Fdict[edge[0]],Fdict[edge[1]])
	
for edge in H.edges(data=True):
	G.add_edge(edge[0],edge[1])
	bipa_Edges.append((edge[0],edge[1]))

nmEdges=G.edges()

degG=G.degree()




#### ΣΧΕΔΙΑΣΜΟΣ ΙΣΤΟΓΡΑΜΜΑΤΩΝ

plt.figure()
plt.title('Initial Graph')
plt.xlabel("Degree")
hist(G.degree().values(),bins=len(set(G.degree().values())),color='g',align='mid')

hEdges=list(bipa_Edges)
aNodes=[nd[0] for nd in G.nodes(data=True) if nd[1]['bipa']==0]
bNodes=[nd[0] for nd in G.nodes(data=True) if nd[1]['bipa']==1]
while len(hEdges)<nm+addEdges:
	ed=random.choice(aNodes)
	de=random.choice(bNodes)
	if G.has_edge(ed,de):
		continue
	else:
		G.add_edge(ed,de)
		hEdges.append((ed,de))
degG=G.degree()

plt.figure()
hist(G.degree().values(),bins=len(set(G.degree().values())),color='b',align='mid')
plt.title('Graph with Added Bridges (%.2f)' %percentEdgesAdd)
plt.xlabel("Degree")

aNodes=[nd[0] for nd in G.nodes(data=True) if nd[1]['bipa']==0]
bNodes=[nd[0] for nd in G.nodes(data=True) if nd[1]['bipa']==1]
while len(G.edges())>len(nmEdges):
	ed=random.choice(aNodes)
	de=random.choice(bNodes)
	if G.has_edge(ed,de):
		G.remove_edge(ed,de)
	else:
		continue
degG=G.degree()

plt.figure()
hist(G.degree().values(),bins=len(set(G.degree().values())),color='r',align='mid')
plt.title('Graph with Removed Bridges (%.2f)' %percentEdgesRemove)
plt.xlabel("Degree")
plt.ylabel("Number of nodes")

plt.show()