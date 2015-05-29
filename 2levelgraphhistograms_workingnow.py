# -*- coding: utf-8 -*-
"""
    LAST UPDATE: 21 Νοεμβρίου 2014

    @authors: Moses Boudourides & Sergios Lenis
    """


import networkx as nx
import matplotlib.pyplot as plt
# import numpy as np
# import random
from pylab import hist
# import colorBar
from collections import Counter

def meanstdv(x):
 from math import sqrt
 n, mean, std = len(x), 0, 0
 for a in x:
     mean = mean + a
 mean = mean / float(n)
 #for a in x:
     #std = std + (a - mean)**2
 #std = sqrt(std / float(n-1))
 return mean#, std
    
def randomBipartiteGraph(n,m,nm):
    from networkx.algorithms import bipartite
    import random
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

### Undirected Two-Level Random Graphs Erdos-Renyi
### I. Start with empty bipartite graph, q=0, and the two levels having given p1 and p2
### II. Start with empty level graphs, p1=p2=0, and the bipartite graph having given q

# p1=0.2
# p2=0.3
q=1
#qlist=[0,0.2,0.5,0.75,1]
qlist=[]
ii=0
while ii<1:
    qlist.append(ii)
    ii+=0.1
n=1
m=2
k=n
start_nm=0
end_nm=n*m
# times=100
times=5
# an = p1*n
# am = p2*m
# dif=abs(n-m)

# J=nx.cycle_graph(n)
J=nx.complete_graph(n)
# J.add_node(0)
F=nx.complete_graph(m)
# F=nx.cycle_graph(m)
# J=nx.erdos_renyi_graph(n,p1) #Ο γράφος του πρώτου επιπέδου
# F=nx.erdos_renyi_graph(m,p2) #Ο γράφος του δευτέρου επιπέδου

qstomi=dict()
dstomi=dict()
Mqstomi=dict()
mqstomi=dict()
#for q in qlist:
    #print q
    #qstomi[q]=[]
for nm in range(start_nm,end_nm+1):
    #qstomi[nm]=[]
    #dstomi[nm]=[]
    nmlist=[]
    minlist=[]
    maxlist=[]
    deglist=[]
    print nm
    for tim in range(times):
        H=randomBipartiteGraph(n,m,nm)
    

        #H=nx.bipartite_random_graph(n,m,q) #Ο διμερής γράφος που γεφυρώνει τα δυο επίπεδα
        G=nx.Graph()  #Ο τελικός σύνθετος γράφος
        Jnod=[]
        for node in J.nodes():
            G.add_node(node,bipartite=0)
            Jnod.append(node)
        for edge in J.edges():
            G.add_edge(edge[0],edge[1])

        #J1=G.subgraph(J.nodes())
        Fnod=[]
        for edge in F.edges():
            G.add_edge(edge[0]+k,edge[1]+k)
        for node in F.nodes():
            G.add_node(node+k,bipartite=1)
            Fnod.append(node+k)
        for edge in H.edges(data=True):
            G.add_edge(edge[0],edge[1])



        #J1=G.subgraph(J.nodes())

        #Jcount=Counter()
        #Jdeg=J1.degree()

        #for jj in Jdeg:
            #Jcount[Jdeg[jj]]+=1
        #Jmax=max(Jcount.values())
        #for jj in Jcount:
            #if Jcount[jj]==Jmax:
                #Jan=jj

        #Fnod=[]
        #for i in F.nodes():
            #Fnod.append(i+k)
        #F1=G.subgraph(Fnod)
        #Fcount=Counter()
        #Fdeg=F1.degree()

        #for jj in Fdeg:
            #Fcount[Fdeg[jj]]+=1
        #Fmax=max(Fcount.values())
        #for jj in Fcount:
            #if Fcount[jj]==Fmax:
                #Fan=jj

        degG=G.degree()
        #degJ1=G.degree()
        #degF1=G.degree()
        degH=H.degree()


        Jv=Jnod
        Fv=Fnod

        degJv=G.degree(Jv)
        degFv=G.degree(Fv)
        mJv = min(degJv.values())
        MJv = max(degJv.values())
        mFv = min(degFv.values())
        MFv = max(degFv.values())
        # delta=mFv - MJv
        print mJv,MJv,mFv,MFv,'mvvvv'
        rJv = range(mJv,MJv+1)#set(degJv.values())#
        rFv = range(mFv,MFv+1)#set(degFv.values())#
        print rJv,rFv,'rjv'
        tomi=set(rJv).intersection(set(rFv))
        print tomi,'tomi'
        stomi=len(tomi)
        print stomi,'stomi'
        if stomi==0:
            mtomi=0
            Mtomi=0
        else:
            mtomi=min(tomi)
            Mtomi=max(tomi)

        #rtomi=range(mtomi,Mtomi+1)
        #lrtomi=len(rtomi)

        #print stomi
        #print str(" ")

        #print "The case of an undirected simple two-level graph G with \n(n=%s, p1=%.2f), (m=%d, p2=%.2f), q=%s" %(n,p1,m,p2,q) #delta=%s
        #print str(" ")

        #print "Jv is the set of vertices in G belonging to the first level"
        #print "Fv is the set of vertices in G belonging to the second level"
        #print str(" ")
        ## print "The difference in numbers of nodes is %s" %dif
        ## print str("The two peaks are at average degrees: ") + str(an ) + str(" and ") + str(am)

        #print str("The sorted degree sequence of G") + str(" is: ") + str(sorted(set(G.degree().values())))
        #print str("The sorted degree sequence of H") + str(" is: ") + str(sorted(set(H.degree().values())))
        #print str("The sorted degree sequence of Jv") + str(" is: ") + str(sorted(set(degJv.values())))
        #print str("The sorted degree sequence of Fv") + str(" is: ") + str(sorted(set(degFv.values())))
        #print str(" ")

        #print "mJv, MJv are the minimum and maximum (resp.) degrees of vertices in the first level"
        #print "mFv, MFv are the minimum and maximum (resp.) degrees of vertices in the second level"
        #print "tomi is the intersection of rJv=(mJv,MJv) and rFv=(mFv,MFv)"
        #print "stomi is the number of elements of tomi"
        ## print "delta is a parameter indicating separation among the sets of degrees of vertices in the first and the second level"
        ## print "delta > 0 means separation"
        #print "stomi = 0 means separation between rJv=(mJv,MJv) and rFv=(mFv,MFv)"
        #print 'stomi > 0 means overlapping of rJv=(mJv,MJv) and rFv=(mFv,MFv)'
        #print 'stomi = %d' %stomi
        ## print "delta <= 0 means overlapping"

        #print str(" ")

        ##print str("(mJv, MJv), (mFv, MFv): (%s, %s), (%s, %s)" %(mJv,MJv,mFv,MFv))
        #print "rJv: %s\nrFv: %s\nstomi: %s" %(rJv,rFv,stomi)
        ## print "delta = mFv - MJv = " + str(delta)
        ## print str("rJv, rFv: %rJv  \n%rFv" %(rJv,rFv))
        #print str(" ")
        #for j in rtomi:
            #nmlist.append(j)
        # nmlist.append(rtomi)
        nmlist.append(stomi)
        minlist.append(mtomi)
        maxlist.append(Mtomi)
        #deglist.append(nx.degree_assortativity_coefficient(G))
    #print nmlist,meanstdv(nmlist)
    #print aaaa
    print nmlist, 'nml'
    qstomi[nm]=meanstdv(nmlist)
    Mqstomi[nm]=max(minlist)
    mqstomi[nm]=min(maxlist)

    #dstomi[nm]=meanstdv(deglist)
    # nqstomi = [x/(n*m) for x in qstomi]

            #print aaa

            #plt.figure()

            #plt.xlabel("Degree")
            #hist(degG.values(),bins=len(set(G.degree().values())),color='g',align='mid') #width=0.25,

            ## histtype='step',
            #plt.ylabel("Number of nodes")
            #plt.xticks([1*k for k in set(G.degree().values())])
            #stitle='Histogram of degrees of vertices of G (green) \n(n=%s, p1=%.2f), (m=%d, p2=%.2f), q=%s, stomi=%s' %(n,p1,m,p2,q,stomi)
            ## \ndif=%s, an=%s, am=%s, \n(n=%s, p1=%.2f), (m=%d, p2=%.2f), q=%s' %(dif,an,am,n,p1,m,p2,q)
            #plt.title(stitle)

            ## plt.figure()
            ##
            ## plt.xlabel("Degree")
            ## hist(degH.values(),bins=len(set(H.degree().values())),color='y',align='mid') #width=0.25,
            ## # histtype='step',
            ## plt.ylabel("Number of nodes")
            ## plt.xticks([1*k for k in set(H.degree().values())])
            ## stitle='Histogram of degrees of vertices of the bipartite graph H (yellow) \n(n=%s, p1=%.2f), (m=%d, p2=%.2f), q=%s, delta=%s' %(n,p1,m,p2,q,delta)
            ## # \ndif=%s, an=%s, am=%s, \n(n=%s, p1=%.2f), (m=%d, p2=%.2f), q=%s' %(dif,an,am,n,p1,m,p2,q)
            ## plt.title(stitle)
            ##
            ## plt.figure()
            ##
            ## plt.xlabel("Degree")
            ## hist(degJv.values(),bins=len(set(degJv.values())),color='r',width=0.3,align='mid') #width=0.25,
            ## hist(degFv.values(),bins=len(set(degFv.values())),color='b',width=0.3,align='mid') #width=0.25,
            ## # histtype='step',
            ## plt.ylabel("Number of nodes")
            ## plt.xticks([1*k for k in set(G.degree().values())])
            ## stitle='Histogram of Degrees of vertices of first level (red) and second level (blue) \n(n=%s, p1=%.2f), (m=%d, p2=%.2f), q=%s, delta=%s' %(n,p1,m,p2,q,delta)
            ## # 'Histograms of Degrees of Nodes of J and F \ndif=%s, an=%s, am=%s, \n(n=%s, p1=%.2f), (m=%d, p2=%.2f), q=%s' %(dif,an,am,n,p1,m,p2,q)
            ## plt.title(stitle)

            #plt.figure()

            #plt.xlabel("Degree")
            #hist(degH.values(),bins=len(set(H.degree().values())),color='y',width=0.3,align='mid') #width=0.25,
            ## hist(degG.values(),bins=len(set(G.degree().values())),color='g',width=0.3,align='mid') #width=0.25,
            #hist(degJv.values(),bins=len(set(degJv.values())),color='r',width=0.3,align='mid') #width=0.25,
            #hist(degFv.values(),bins=len(set(degFv.values())),color='b',width=0.3,align='mid') #width=0.25,
            ## histtype='step',
            #plt.ylabel("Number of nodes")
            #plt.xticks([1*k for k in set(G.degree().values())])
            #stitle='Histogram of Degrees of vertices of G (green), \nH (yellow), first level (red) and second level (blue) \n(n=%s, p1=%.2f), (m=%d, p2=%.2f), q=%s, stomi=%s' %(n,p1,m,p2,q,stomi)
            ## 'Histograms of Degrees of Nodes of J and F \ndif=%s, an=%s, am=%s, \n(n=%s, p1=%.2f), (m=%d, p2=%.2f), q=%s' %(dif,an,am,n,p1,m,p2,q)
            #plt.title(stitle)

            # plt.figure()
            #
            # plt.xlabel("Degree")
            # hist(degJ1.values(),bins=len(set(degJv.values())),color='r',width=0.25,align='mid')
            # # histtype='step',
            # plt.ylabel("Number of nodes")
            # plt.xticks([1*k for k in set(degJv.values())])
            # stitle='Histogram of Degrees of Nodes of J \ndif=%s, an=%s, am=%s, \n(n=%s, p1=%.2f), (m=%d, p2=%.2f), q=%s' %(dif,an,am,n,p1,m,p2,q)
            # plt.title(stitle)
            #
            # plt.figure()
            #
            # plt.xlabel("Degree")
            # hist(degF1.values(),bins=len(set(degFv.values())),color='b',width=0.25,align='mid')
            # # histtype='step',
            # plt.ylabel("Number of nodes")
            # plt.xticks([1*k for k in set(F1.degree().values())])
            # stitle='Histogram of Degrees of Nodes of F \ndif=%s, an=%s, am=%s, \n(n=%s, p1=%.2f), (m=%d, p2=%.2f), q=%s' %(dif,an,am,n,p1,m,p2,q)
            # plt.title(stitle)



            # # hist(deg.values(),bins=len(set(G.degree().values())),normed=True,color='g')
            # # plt.ylabel("Percentage of nodes")
            # # plt.title('Histogram of Degrees of Nodes (Percentages)')
            #
            # # plt.figure()
            # # plt.xlabel("Degree (log)")
            # # hist(deg.values(),bins=len(set(G.degree().values())),color='g',log=True)
            # # mindd=1000
            # # for ddd in G.degree().values():
            # #     if ddd>0 and ddd<mindd:
            # #         mindd=ddd
            # # plt.gca().set_xlim([mindd,max(set(G.degree().values()))])
            # # plt.gca().set_xscale("log")
            # # plt.ylabel("Number of nodes (log)")
            # # stitle='Histogram of Degrees of Nodes (log)\ndif=%s, an=%s, am=%s, \n(n=%s, p1=%.2f), (m=%d, p2=%.2f), q=%s' %(dif,an,am,n,p1,m,p2,q)
            # # plt.title(stitle)

itomi=[]
ival=[]
for k in sorted(qstomi.keys()):
    itomi.append(qstomi[k])
    ival.append(k)
print itomi, 'itomi'
# val=[]
mval=[]
Mval=[]
# qval=[]

# for k in sorted(qstomi.keys()):
#     val.append(qstomi[k])
#     qval.append(k)

# for k in sorted(nqstomi.keys()):
#     val.append(nqstomi[k])
#     qval.append(k)

mqval=[]

for k in sorted(mqstomi.keys()):
    mval.append(mqstomi[k])
    mqval.append(k)
print mval, 'mqval'

Mqval=[]
for k in sorted(Mqstomi.keys()):
    Mval.append(Mqstomi[k])
    Mqval.append(k)
print Mval, 'Mqval'

plt.figure()
# plt.step(mqval,mval,linewidth=2)
# plt.title('Minimum Degree Scrabbling')
# plt.ylim(ymax=2.1)

# plt.step(Mqval,Mval,linewidth=2,color='r')
# plt.title('Maximum Degree Scrabbling')

plt.step(ival,itomi,linewidth=2,color='g')
# plt.title('Maximum Degree Scrabbling')
# plt.title('Average (?) Degree Scrabbling')

plt.ylim(ymax=max(Mval)+0.1)

# plt.subplot(212)
# plt.step(sorted(Mqstomi.keys()),qval,linewidth=2,color='r')
print mqval
print Mqval
print itomi

# plt.plot(sorted(qstomi.keys()),val,'--')
# plt.step(sorted(Mqstomi.keys()),Mqval,linewidth=2,color='r')
# plt.step(sorted(mqstomi.keys()),val,linewidth=2)
# plt.step(sorted(Mqstomi.keys()),val,linewidth=2,color='r')
# plt.ylim(ymax=2.1)

#plt.show()
# val=[]
# qval=[]
# qmax=max(qstomi.keys())
# kmax=max(qstomi.values())
# #print qstomi
# for k in sorted(qstomi.keys()):
#     #print qstomi[k],kmax
#     val.append(qstomi[k]*1./kmax)
#     qval.append(k*1./qmax)
# dval=[]
# dqval=[]
# #for k in sorted(dstomi.keys()):
#
#     #dval.append(dstomi[k])
#     #dqval.append(k)
# plt.figure()
# # plt.plot(qval,val,'b*--')
# plt.step(qval,val,linewidth=2)
# plt.ylim(ymax=1.1)
# #plt.plot(qval,dval,'r*')
# plt.plot()





plt.show()
