##adjacency_matrix
import networkx as nx
import numpy as np
from matplotlib import pyplot, patches
import pylab
import scipy
import community

def assLabNode(graph,name,pa):
    if pa==0:
        graph.node[name]['label']='a'
    elif pa==1:
        graph.node[name]['label']='b'
    else:
        for node in graph.nodes():
            graph.node[node]['label']=name

def assBiNode(graph):
    for node in graph.nodes():

        q=random.random()
        if q<.5:
            graph.add_node(node,bipartite=0)
            assLabNode(graph,node,0)

        else:
            graph.add_node(node,bipartite=1)
            assLabNode(graph,node,1)

def assColorEdge(graph):
    for a in graph.edges(data=True):

        if graph.node[a[0]]['label']==graph.node[a[1]]['label']:
            if graph.node[a[1]]['label']=='a':
                graph.add_edges_from([a],color='green')
            else:
                graph.add_edges_from([a],color='blue')
        else:
            graph.add_edges_from([a],color='red')

def draw_adjacency_matrix(G, node_order=None, partitions=[], colors=[]):
    """
    - G is a netorkx graph
    - node_order (optional) is a list of nodes, where each node in G
          appears exactly once
    - partitions is a list of node lists, where each node in G appears
          in exactly one node list
    - colors is a list of strings indicating what color each
          partition should be
    If partitions is specified, the same number of colors needs to be
    specified.
    """
    adjacency_matrix = nx.to_numpy_matrix(G, dtype=np.bool, nodelist=node_order)
##    print adjacency_matrix
    #Plot adjacency matrix in toned-down black and white
    fig = pyplot.figure(figsize=(5, 5)) # in inches
    
    pyplot.imshow(adjacency_matrix,
                  cmap="Greys",
                  interpolation="none")
    
    # The rest is just if you have sorted nodes by a partition and want to
    # highlight the module boundaries
    assert len(partitions) == len(colors)
    ax = pyplot.gca()
    for partition, color in zip(partitions, colors):
        current_idx = 0
        for module in partition:
            ax.add_patch(patches.Rectangle((current_idx, current_idx),
                                          len(module), # Width
                                          len(module), # Height
                                          facecolor="none",
                                          edgecolor=color,
                                          linewidth="1"))
            current_idx += len(module)
pyplot.show()
##            
##N=100
##m=20
##G = nx.barabasi_albert_graph(N,m)
##n1=50
##m1=6
##n2=50
##m2=6
##times=20
##p1=0.7
##p2=0.7
##p=0.3
##k1=m1
##k2=m2
##step=25
##stepP=0.01
##pMax=1.0
##timesP=int(pMax/stepP)
##
####b=nx.barabasi_albert_graph(n1,m1)
####c=nx.barabasi_albert_graph(n2,m2)
####b=nx.connected_watts_strogatz_graph(n1,k1,p1)
####c=nx.connected_watts_strogatz_graph(n2,k2,p2)
##b=nx.erdos_renyi_graph(n1,p1)
##c=nx.erdos_renyi_graph(n2,p2)
##
##a=nx.bipartite_random_graph(n1, n2, p)
##bb=nx.dfs_tree(b)
##cc=nx.dfs_tree(c)
##
##aa=a.nodes(data=True)
##ala=[aax[0] for aax in aa if aax[1]['bipartite']==0]
##bla=[aax[0] for aax in aa if aax[1]['bipartite']==1]
##uper_list=[]
##low_list=[]
##up_dic={}
##low_dic={}
##for x in ala:
##    uper_list.append(x)
##for y in bla:
##    low_list.append(y)
##uper_list.sort()
##low_list.sort()
##    
####n1=nodes1
####n2=nodes2
####m1=maxedges1
####m2=maxedges2
##
##b_nodes=sorted(b.nodes())
##c_nodes=sorted(c.nodes())
##
##for xx in range(len(uper_list)):
##    up_dic[b_nodes[xx]]=uper_list[xx]
##for yy in range(len(low_list)):
####        print yy
##    low_dic[c_nodes[yy]]=low_list[yy]
##bb=nx.relabel_nodes(b,up_dic)
##cc=nx.relabel_nodes(c,low_dic)
##
##b_edges=bb.edges()
##c_edges=cc.edges()
####    print b_edges
####    print 'a',c_edges
####    print cc.nodes()
##for x in ala:
##    assLabNode(a,x,0)
##for y in bla:
##    assLabNode(a,y,1)
##a.add_edges_from(b_edges)
##a.add_edges_from(c_edges)
##
##assColorEdge(a)
##partition = community.best_partition(a)
##print partition
##
##size = float(len(set(partition.values())))
##count = 0.
##node_lists=[]
##for i in set(partition.values()):
##    count+=1
##    community_i = "Community", i
##    print "Community", i
##    members  =  list_nodes  =  [nodes  for  nodes  in
##partition.keys()  if  partition[nodes]  ==  i]
####    print members
##    bip=[node[1]['label'] for node in a.nodes(data=True) if node[0] in members ]
####    print bip
##    node_lists.append(members)
##print node_lists
##node_list=[]
##for i in node_lists:
##    
##    for node in i:
##        
##        node_list.append(node)
##print node_list
##draw_adjacency_matrix(a,node_order=node_list)
####sl=subCommunityAnalysis(a,k,i)
