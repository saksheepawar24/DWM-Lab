#PageRank
import networkx as nx
G=nx.barabasi_albert_graph(10,9)
pr=nx.pagerank(G,0.85)
print(pr)

#HITS
import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
G.add_edges_from([('A','B'),('B','C'),('B','E'),('C','A'),
 ('D','G'),('E','D'),('E','B'),('E','F'),
 ('E','C'),('F','C'),('F','H'),('G','A'),
 ('G','C'),('H','A')])
plt.figure(figsize=(10,10))
nx.draw_networkx(G, with_labels=True)
hubs, authorities=nx.hits(G,max_iter=50,normalized=True)
print("Hub Scores:", hubs)
print("Authority Scores: ",authorities)
plt.show()
