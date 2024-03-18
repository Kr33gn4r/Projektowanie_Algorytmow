import networkx as nx
import matplotlib.pyplot as plt
from random import randrange

number = int(input("liczba: "))
plt.figure(figsize=(7, 7))
G = nx.empty_graph(number)
pos = {k: [randrange(-100, 105, 5), randrange(-100, 105, 5)] for k in range(number)}
nx.draw(G, pos, labels={k: k+1 for k in G.nodes}, node_size=100, font_size=5)
plt.show()