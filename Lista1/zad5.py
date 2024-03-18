import networkx as nx
import matplotlib.pyplot as plt
from random import randrange
from math import sqrt

def if_avail(xy, xydict):
    for p in xydict.values():
        if sqrt( ( xy[0] - p[0] )**2 + ( xy[1] - p[1] )**2 ) < 2 * r: return False
    return True

plt.figure(figsize=(7, 7))
err_iter = 100
G = nx.Graph()
pos = {}
i = 1
r = 8

G.add_node(0)
pos[0] = [randrange(-100, 101, 1), randrange(-100, 101, 1)]
while err_iter:
    temppos = [randrange(-100, 101, 1), randrange(-100, 101, 1)]
    if if_avail(temppos, pos):
        pos[i] = temppos
        err_iter = 100
        G.add_node(i)
        i += 1
    else: err_iter -= 1

nx.draw(G, pos, labels={k: k+1 for k in G.nodes}, node_size=100, node_color='tab:blue', font_size=5,)
ax = plt.gca()
for p in pos.values():
    ax.add_patch(plt.Circle((p[0], p[1]), radius=r, edgecolor='tab:blue', fill=False))
plt.axis('equal')
plt.show()