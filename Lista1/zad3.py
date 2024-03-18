import networkx as nx
import matplotlib.pyplot as plt

number = int(input("liczba: "))
G = nx.complete_graph(number)
pos = nx.circular_layout(G)
plt.figure(figsize=(7, 7))
nx.draw(G, pos, labels={k: k+1 for k in G.nodes})
plt.show()