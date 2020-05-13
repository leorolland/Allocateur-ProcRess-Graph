import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(1)
G.add_nodes_from([2, 3, 4, 5])
G.add_edges_from([(4, 5)])

nx.draw(G, with_labels=True)
plt.show()

print("wesh gros")
fdsfdsfds
