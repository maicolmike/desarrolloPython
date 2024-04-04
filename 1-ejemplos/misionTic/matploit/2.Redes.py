import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(["Tom Hanks" ,"Bill Patson","Arnold Schecoso","Angelina Jolie"])

G.add_edges_from([("Tom Hanks","Bill Patson"), ("Arnold Schecoso","Tom Hanks"),("Tom Hanks","Angelina Jolie"),("Angelina Jolie","Arnold Schecoso")])

print(list(G.nodes))
print(list(G.edges))

nx.draw(G, with_labels=True, font_weight='bold')
plt.tight_layout()
plt.savefig("grafo.jpg",format="jpg")