# -*- coding: utf-8 -*-
"""
LAST UPDATE: 11 Νοεμβρίου 2014

@author: Moses Boudourides
"""


import networkx as nx
import matplotlib.pyplot as plt

#Εισαγωγή Απλού (Μη Κατευθυνόμενου) Γράφου
G = nx.Graph()

G.add_nodes_from([1,2,3,4,5])
#G.add_nodes_from(range(1,6)) #Το ίδιο όπως το προηγούμενο

G.add_nodes_from(['John', 'Mary'])
G.add_node('a')
G.remove_nodes_from(['John', 'Mary'])
G.remove_node('a')

G.add_edges_from([(1,2),(1,4),(2,3),(3,4),(3,5),(4,5)])

G.nodes()
G.number_of_nodes()
G.edges()
G.number_of_edges()

#Γενικές οδηγίες για τον σχεδιασμό γράφων μέσω των συναρτήσεων nx.draw:
#
#1. Αρχικά γράφουμε την εντολή:
#plt.figure()
#Σε περίπτωση που ακολουθούν περισσότερες της μιας συναρτήσεις nx.draw, για να βγαίνει άσπρο το background του σχήματος, η παραπάνω εντολή πρέπει να γραφεί με την εξής παράμετρο:
#plt.figure(facecolor='w')
#
#2. Ακολουθεί/ούν η/οι συνάτηση/εις nx.draw
#
#3. Για να εμφανισθεί το σχήμα, γράφουμε:
#plt.show()
#ή όταν κολλά plt.show(block=False)
#
#ΠΡΟΣΟΧΗ: Όταν θέλουμε να εμφανισθούν μαζί πολλοί (περισσότεροι του ενός) σχεδιασμοί, κάθε φορά στην αρχή των εντολών γράφουμε το plt.figure() (ή το plt.figure(facecolor='w')), αλλά το plt.show() το βάζουμε μόνο μια φορά στο τέλος (όπως κάνουμε σε αυτό το σκριπτ).

#Σχεδιασμός Απλού (Μη Κατευθυνόμενου) Γράφου
plt.figure()
nx.draw(G, with_labels=True)

#Ο ίδιος σχεδιασμός με κάποιες παραμετροποιήσεις:
plt.figure()
nx.draw_spring(G, node_size=500, node_color='#A0CBE2', with_labels=False)

#Ο ίδιος σχεδιασμός αλλά με δεδομένη θέση των κόμβων:
plt.figure()
pos={1:(0,0),2:(1,0),4:(0,1),3:(1,1),5:(0.5,2.0)}
nx.draw(G,pos, with_labels=True) #Το ίδιο αλλά με τους κόμβους σε συγκεκριμένες θέσεις

#Εισαγωγή Πολλαπλού (Μη Κατευθυνόμενου) Γράφου
G = nx.MultiGraph()
G.add_nodes_from(range(1,4))
G.add_edges_from([(1,2),(1,2),(1,2),(1,3),(2,2),(2,3),(2,3)])

#Εισαγωγή Απλού Κατευθυνόμενου Γράφου
G=nx.DiGraph()
G.add_nodes_from(["A","B","C","D"])
G.add_edges_from([("A","B"), ("C","A"), ("C","B"),("B","D")])

#Σχεδιασμός Απλού Κατευθυνόμενου Γράφου
plt.figure()
nx.draw(G, with_labels=True)

#Εισαγωγή Πολλαπλού Κατευθυνόμενου Γράφου
G = nx.MultiDiGraph()
G.add_nodes_from(range(1,4))
G.add_edges_from([(1,2),(1,2),(2,1),(1,3),(2,2),(2,3),(3,2)])

#Εισαγωγή Γράφου με Βάρη Ακμών
G=nx.Graph()
G.add_weighted_edges_from([('a','b',4),('a','c',8),('a','d',5),('c','d',3)])

#Σχεδιασμός Γράφου με Βάρη Ακμών, με τα βάρη παρατιθέμενα πάνω στις ακμές
plt.figure(facecolor='w')
pos=nx.spring_layout(G)
edge_labels=dict([((u,v,),d['weight'])
    for u,v,d in G.edges(data=True)])
nx.draw_networkx_nodes(G,pos,node_size=700)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos,font_size=20)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_size=20)
plt.axis('off')

#Σχεδιασμός Γράφου με Βάρη Ακμών, με το βάρος ως εύρος ακμών
plt.figure(facecolor='w')
nx.draw_networkx_nodes(G,pos,node_size=700)
edgewidth=[]
for (u,v,d) in G.edges(data=True):
    edgewidth.append(d['weight'])
nx.draw_networkx_edges(G,pos,edge_color='b', width=edgewidth)
nx.draw_networkx_labels(G,pos,font_size=20)
plt.axis('off')

#Σχεδιασμός Γράφου με Βάρη Ακμών, με φιλτράρισμα βαρών
elarge = [(u,v) for (u,v,d) in G.edges(data=True)
        if d['weight'] >4]
esmall = [(u,v) for (u,v,d) in G.edges(data=True)
        if d['weight'] <=4]
plt.figure(facecolor='w')
nx.draw_networkx_nodes(G,pos,node_size=700)
nx.draw_networkx_edges(G,pos,edgelist=elarge,edge_color='b',width=edgewidth)
nx.draw_networkx_edges(G,pos,edgelist=esmall,width=6,alpha=0.5,edge_color='g',style='dashed')
nx.draw_networkx_labels(G,pos,font_size=20)
plt.axis('off')

#Εισαγωγή Διμερών Γράφων
from networkx.algorithms import bipartite
G = nx.Graph()
G.add_nodes_from([1,2,3,4], bipartite=0)
G.add_nodes_from(['a','b','c'], bipartite=1)
G.add_edges_from([(1,'a'),(1,'b'),(2,'a'),(2,'b'),(2,'c'),(3,'c'),(4,'b'),(4,'c')])
pos={1:(0,0),
     2:(0,1),
     3:(0,2),
     4:(0,3),
     'a':(1,0.5),
     'b':(1,1.5),
     'c':(1,2.5)}

#Σχεδιασμός Διμερούς Γράφου
mode1, mode2 = bipartite.sets(G)
plt.figure(facecolor='w')
nx.draw_networkx_nodes(G,pos,nodelist=list(mode1),node_color='b',node_size=700)
nx.draw_networkx_nodes(G,pos,nodelist=list(mode2),node_color='g',node_size=700)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos,font_size=20,font_color='#FFFFFF')
plt.axis('off')

#Χαρακτηριστικά ({\textlatin{Attributes}}) Κόμβων
G = nx.Graph()
G.add_node(1, color='red')
G.add_node(2, color='blue')
G.add_node(3, color='green')
G.add_edges_from([(1,2),(1,3),(2,3)])
G.add_nodes_from([(1, {'color': 'red'}), (2, {'color': 'blue'}), (3, {'color': 'green'})]) #Το ίδιο όπως τα 3 παραπάνω
G.node[1]
G.node[1]['color']
G.nodes(data=True)

#Σχεδιασμός Απλού (Μη Κατευθυνόμενου) Γράφου με χαρακτηριστικά κόμβων
pos={1:(0,0),
     2:(1,0),
     3:(.5,1)}
custom_node_color={}
custom_node_color[1] = 'r'
custom_node_color[2] = 'b'
custom_node_color[3] = 'g'
plt.figure()
nx.draw(G,pos,node_list = custom_node_color.keys(),node_color=custom_node_color.values(),with_labels=True,font_color='#FFFFFF')
#plt.show()

#Χαρακτηριστικά ({\textlatin{Attributes}}) Ακμών
G = nx.Graph()
G.add_edge(1, 2, time='May')
G.add_edge(2, 3, time='June')
G.add_edge(3, 4, time='July')
G.add_edge(4, 1, time='August')
G.add_edges_from([(1, 2, {'time': 'May'}), (1, 4, {'time': 'August'}), (2, 3, {'time': 'June'}), (3, 4, {'time': 'July'})]) #Το ίδιο όπως τα 4 παραπάνω
G.edge[1][2]
G.edge[1][2]['time']
G.edges(data=True)

#Σχεδιασμός Απλού (Μη Κατευθυνόμενου) Γράφου με χαρακτηριστικά ακμών
edgelist = [(1,2),(2,3),(3,4),(1,4)]
colorlist =['r','b','g','k']
pos=nx.spring_layout(G)
plt.figure(facecolor='w')
nx.draw_networkx_nodes(G,pos, with_labels=True)
nx.draw_networkx_labels(G,pos,font_size=10)
nx.draw_networkx_edges(G,pos,edgelist=edgelist,edge_color=colorlist)
plt.axis('off')

#Προκατασκευασμένοι Γράφοι

#Οι προκαθορισμένοι γράφοι εισάγονται ως
#G = nx.όνομα_γράφου(παράμετροι)
#όπου το "όνομα_γράφου" και οι "παράμετροι" είναι όπως δίνονται στη συνέχεια.
#Για τον σχεδιασμό των προκαθορισμένων γράφων (χωρίς παραμετροποιήσεις) οι εντολές είναι:
#plt.figure()
#nx.draw(G, with_labels=False)
#plt.show()

#Απλοί και Γνωστοί Προκατασκευασμένοι Γράφοι
#cycle_graph(n) #Κύκλος n κόμβων
#star_graph(n) #Αστέρι n+1 κόμβων
#path_graph(n) #Διαδρομή n κόμβων
#krackhardt_kite_graph() #Γράφος αετού του Krackhardt
#florentine_families_graph() #Γράφος Φλωρεντιανών οικογενειών
#karate_club_graph() #Γράφος του καράτε κλαμπ

#Τυχαίοι Γράφοι
#erdos_renyi_graph(n,p) #Τυχαίος γράφος Erdos-Renyi για n κόμβους και πιθνότητα p
#gnp_random_graph(n,p) #Τυχαίος γράφος gnp για n κόμβους και πιθανότητα p
#gnm_random_graph(n,m) #Τυχαίος γράφος gnm για n κόμβους και m ακμές
#watts_strogatz_graph(n,k,p) #Γράφος αναδικτύωσης πλέγματος Strogatz-Watts για n κόμβους, ο καθένας με k γείτονες (σε τοπολογία δακτυλίου) και με πιθανότητα αναδικτύωσης p
#barabasi_albert_graph(n,m) #Τυχαίος γράφος Barabasi-Albert για n κόμβους και κάθε νέο κόμβο με m ακμές σε υπάρχοντες κόμβους

G1 = nx.cycle_graph(10)
G2 = nx.star_graph(6)
G3 = nx.path_graph(6)
G4 = nx.krackhardt_kite_graph()
G5 = nx.florentine_families_graph()
G6 = nx.karate_club_graph()
fig = plt.figure(figsize=(10,10))
plt.subplot(2,3,1).set_title("Cycle")
nx.draw(G1,node_size=40,with_labels=False); plt.axis("tight")
plt.subplot(2,3,2).set_title("Star")
nx.draw(G2,node_size=40,with_labels=False); plt.axis("tight")
plt.subplot(2,3,3).set_title("Path")
nx.draw(G3,node_size=40,with_labels=False); plt.axis("tight")
plt.subplot(2,3,4).set_title("Krackhardt kite")
nx.draw(G4,node_size=40,with_labels=False); plt.axis("tight")
plt.subplot(2,3,5).set_title("Florentine families")
nx.draw(G5,node_size=40,with_labels=False); plt.axis("tight")
plt.subplot(2,3,6).set_title("Karate club")
nx.draw(G6,node_size=40,with_labels=False); plt.axis("tight")

G9 = nx.erdos_renyi_graph(20,0.2)
G10 = nx.erdos_renyi_graph(20,0.1)
G11 = nx.gnp_random_graph(25,0.1)
G12 = nx.gnm_random_graph(20,15)
G13 = nx.watts_strogatz_graph(10,2,0.4)
G14 = nx.barabasi_albert_graph(40,3)
fig = plt.figure(figsize=(10,10))
plt.subplot(2,3,1).set_title("Erdos Renyi (p=0.2)")
nx.draw(G9,node_size=40,with_labels=False); plt.axis("tight")
plt.subplot(2,3,2).set_title("Erdos Renyi (p=0.1)")
nx.draw(G10,node_size=40,with_labels=False); plt.axis("tight")
plt.subplot(2,3,3).set_title("Random graph G_{n,p} ")
nx.draw(G11,node_size=40,with_labels=False); plt.axis("tight")
plt.subplot(2,3,4).set_title("Random graph G_{n,m}")
nx.draw(G12,node_size=40,with_labels=False); plt.axis("tight")
plt.subplot(2,3,5).set_title("Strogatz-Watts")
nx.draw(G13,node_size=40,with_labels=False); plt.axis("tight")
plt.subplot(2,3,6).set_title("Barabasi-Albert")
nx.draw(G14,node_size=40,with_labels=False); plt.axis("tight")

#Διεπίπεδοι Γράφοι: Κατασκευή από διάσπαση δοθέντος γράφου
p=0.2
n=60
l=25 #Χωρισμός κόμβων σε δυο ομάδες {0, 1, ...,l} και {l+1, l+2, ..., n-1}
d=1.5 #Οριζόντια διαχωριστική απόσταση μεταξύ των ομάδων στον σχεδιασμό του γράφου. Για το circular_layout αρκεί d=0.5, ενώ για το spring_layout καλύτερα d=2.
G=nx.erdos_renyi_graph(n,p)
pos=nx.spring_layout(G)
#pos=nx.circular_layout(G)
top_set=range(0,l+1)
botom_set=range(l+1,n)
for i in pos:
    npos=pos[i]
    if i in top_set:
        pos[i]=[npos[0]-d,npos[1]]
    elif i in botom_set:
        pos[i]=[npos[0]+d,npos[1]]
plt.figure()
nx.draw(G,pos, with_labels=True,nodelist=top_set,node_color='r')
nx.draw(G,pos, with_labels=True,nodelist=botom_set,node_color='b')

#Διεπίπεδοι Γράφοι: Κατασκευή από σύνθεση δυο δοθέντων γράφων
p1=0.2
p2=0.3
q=0.1
n=50
m=70
k=n
d=1 #Οριζόντια διαχωριστική απόσταση μεταξύ των ομάδων στον σχεδιασμό του γράφου. Για το circular_layout αρκεί d=0.5, ενώ για το spring_layout καλύτερα d=2.
J=nx.erdos_renyi_graph(n,p1) #Ο γράφος του πρώτου επιπέδου
F=nx.erdos_renyi_graph(m,p2) #Ο γράφος του δευτέρου επιπέδου
H=nx.bipartite_random_graph(n,m,q) #Ο διμερής γράφος που γεφυρώνει τα δυο επίπεδα
G=nx.Graph()  #Ο τελικός σύνθετος γράφος
for node in J.nodes():
    G.add_node(node,bipartite=0)
for edge in J.edges():
    G.add_edge(edge[0],edge[1])
for edge in F.edges():
    G.add_edge(edge[0]+k,edge[1]+k)
for node in F.nodes():
    G.add_node(node+k,bipartite=1)
for edge in H.edges(data=True):
    G.add_edge(edge[0],edge[1])
pos=nx.spring_layout(G)
#pos =nx.circular_layout(G)
top_set=set()
botom_set=set()
for i in pos:
    npos=pos[i]
    if G.node[i]['bipartite']==0:
        pos[i]=[npos[0],npos[1]+d]
        top_set.add(i)
    elif G.node[i]['bipartite']==1:
        pos[i]=[npos[0],npos[1]-d]
        botom_set.add(i)
plt.figure()
nx.draw(G,pos, with_labels=True,nodelist=list(top_set),node_color='r')
nx.draw(G,pos, with_labels=True,nodelist=list(botom_set),node_color='b')

#Το παράδειγμα directors-companies:
directors = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f"}
companies={0:"A",1:"B",2:"C",3:"D",4:"E"}
labels= directors.copy()
newkey=len(directors.keys())
for k in companies.keys():
    labels[k+newkey]=companies[k]
from networkx.algorithms import bipartite
J=nx.erdos_renyi_graph(6,0.8) #Directors
F=nx.erdos_renyi_graph(5,0.6) #Companies
H=nx.bipartite_random_graph(6,5,0.55) #Directors in Companies
G=nx.Graph() #Two-Level Graph
for node in J.nodes():
    G.add_node(node,bipartite=0)
for edge in J.edges():
    G.add_edge(edge[0],edge[1])
for edge in F.edges():
    G.add_edge(edge[0]+6,edge[1]+6)
for node in F.nodes():
    G.add_node(node+6,bipartite=1)
for edge in H.edges(data=True):
    G.add_edge(edge[0],edge[1])

posJ=nx.spring_layout(J)
posF=nx.spring_layout(F)
posH={0:(0,0),1:(0,2),2:(0,4),3:(0,6),4:(0,8),5:(0,10),6:(1,1),7:(1,3),8:(1,5),9:(1,7),10:(1,9)}
mode1, mode2 = bipartite.sets(H)
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
nx.draw(J,pos=posJ,node_color='r',node_size=700,font_size=20,font_color='#FFFFFF',with_labels=False)
nx.draw_networkx_labels(J,posJ,directors,font_size=20,font_color='#FFFFFF')
plt.figure()
nx.draw(F,pos=posF,node_color='b',node_size=800,font_size=20,font_color='#FFFFFF',node_shape='s',with_labels=False)
nx.draw_networkx_labels(F,posF,companies,font_size=20,font_color='#FFFFFF')
plt.figure(facecolor='w')
nx.draw_networkx_nodes(H,pos=posH,nodelist=list(mode1),node_color='r',node_size=700)
nx.draw_networkx_nodes(H,pos=posH,nodelist=list(mode2),node_color='b',node_size=800,node_shape='s')
nx.draw_networkx_edges(H,pos=posH)
nx.draw_networkx_labels(H,posH,labels,font_size=20,font_color='#FFFFFF')
plt.axis('off')
plt.figure()
nx.draw(G,pos,nodelist=list(top_set),node_color='r',node_size=700,with_labels=False)
nx.draw(G,pos,nodelist=list(botom_set),node_color='b',node_size=800,node_shape='s',with_labels=False)
nx.draw_networkx_labels(G,pos,labels,font_size=20,font_color='#FFFFFF')

fig = plt.figure(figsize=(13,13))
plt.subplot(2,2,1).set_title("Friendship Network of Directors")
nx.draw(J,pos=posJ,node_color='r',node_size=700,font_size=20,font_color='#FFFFFF',with_labels=False)
nx.draw_networkx_labels(J,posJ,directors,font_size=20,font_color='#FFFFFF')
plt.axis("tight")
plt.subplot(2,2,2).set_title("Collaboration Network of Companies")
nx.draw(F,pos=posF,node_color='b',node_size=800,font_size=20,font_color='#FFFFFF',node_shape='s',with_labels=False)
nx.draw_networkx_labels(F,posF,companies,font_size=20,font_color='#FFFFFF')
plt.axis("tight")
#plt.figure(facecolor='w')
plt.subplot(2,2,3).set_title("Two-Mode network of Directors and Companies")
nx.draw_networkx_nodes(H,pos=posH,nodelist=list(mode1),node_color='r',node_size=700)
nx.draw_networkx_nodes(H,pos=posH,nodelist=list(mode2),node_color='b',node_size=800,node_shape='s')
nx.draw_networkx_edges(H,pos=posH)
nx.draw_networkx_labels(H,posH,labels,font_size=20,font_color='#FFFFFF')
plt.axis('off')
plt.axis("tight")
plt.subplot(2,2,4).set_title("Two-Level Network of Directors and Companies")
nx.draw(G,pos,nodelist=list(top_set),node_color='r',node_size=700,with_labels=False)
nx.draw(G,pos,nodelist=list(botom_set),node_color='b',node_size=800,node_shape='s',with_labels=False)
nx.draw_networkx_labels(G,pos,labels,font_size=20,font_color='#FFFFFF')
plt.axis("tight")

#Συνθετικοί Εγωκεντρικοί Γράφοι
p=0.15
q=1
n=40
m=1
k=n
d=1.2 #Οριζόντια διαχωριστική απόσταση μεταξύ των ομάδων στον σχεδιασμό του γράφου. Για το circular_layout αρκεί d=0.5, ενώ για το spring_layout καλύτερα d=2.

J=nx.erdos_renyi_graph(n,p) #Ο γράφος του πρώτου επιπέδου
F=nx.erdos_renyi_graph(m,p) #Ο γράφος του δευτέρου επιπέδου
H=nx.bipartite_random_graph(n,m,q) #Ο διμερής γράφος που γεφυρώνει τα δυο επίπεδα
G=nx.Graph()  #Ο τελικός σύνθετος γράφος
for node in J.nodes():
    G.add_node(node,bipartite=0)
for edge in J.edges():
    G.add_edge(edge[0],edge[1])
for edge in F.edges():
    G.add_edge(edge[0]+k,edge[1]+k)
for node in F.nodes():
    G.add_node(node+k,bipartite=1)
for edge in H.edges(data=True):
    G.add_edge(edge[0],edge[1])
pos=nx.spring_layout(G)
#pos =nx.circular_layout(G)
top_set=set()
botom_set=set()
for i in pos:
    npos=pos[i]
    if G.node[i]['bipartite']==0:
        pos[i]=[npos[0],npos[1]+d]
        top_set.add(i)
    elif G.node[i]['bipartite']==1:
        pos[i]=[npos[0],npos[1]-d]
        botom_set.add(i)
plt.figure()
nx.draw(G,pos, with_labels=True,nodelist=list(top_set),node_color='r')
nx.draw(G,pos, with_labels=True,nodelist=list(botom_set),node_color='b')

plt.show()
