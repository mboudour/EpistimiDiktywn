import igraph as ig
file_name=str(G.name)+str(lvl2)+'.graphml'
nx.write_graphml(G, file_name)
g = ig.read(file_name, format="graphml")
mcliques=g.maximal_cliques(0,5)
print mcliques
[(8, 4, 6), (8, 2), (0, 7, 5), (0, 7, 4, 9), (0, 7, 4, 3, 6), (0, 2), (0, 1)]
colors_list=["gray","brown","yellow","cyan","green","blue","purple"]
group_markers = [(mcliques[i], colors_list[i]) for i in range(len(mcliques))]
ig.plot(g, mark_groups=group_markers)