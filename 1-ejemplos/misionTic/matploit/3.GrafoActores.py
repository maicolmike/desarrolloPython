import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(["Tom Hanks","Kevin Bacon","Bill Patxon","Gari Sinise","Ed Harris"])

G.add_edges_from( [
	("Tom Hanks", "Bill Patxon", {'weight': 1}),
	("Tom Hanks", "Gari Sinise", {'weight': 4}),
	("Tom Hanks", "Kevin Bacon", {'weight': 1}),
	("Bill Patxon", "Gari Sinise", {'weight': 1}),
	("Kevin Bacon", "Gari Sinise", {'weight': 1}),
	("Ed Harris", "Gari Sinise", {'weight': 1}),
])

aristas = list(G.edges)
pos = nx.spring_layout(G) 

nx.draw_networkx_nodes(G, pos, node_size=700)

nx.draw_networkx_edges(
    G, pos, edgelist=aristas, width=2, alpha=0.5, edge_color="b", 
		)

nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")

labels = nx.get_edge_attributes(G,'weight')

nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

plt.axis("off")
plt.savefig("actores.jpg",format="jpg")


A = nx.adjacency_matrix(G)
print(A.todense())