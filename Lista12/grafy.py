import networkx as nx
import matplotlib.pyplot as plt
from random import randint

# DFS, Kruskal, Dijkstra

class Graph:
    def __init__(self):
        self.graph = None

    def generate(self, n, p, weights=None, namefile=None):
        self.graph = nx.fast_gnp_random_graph(n, p)
        if weights:
            nx.set_edge_attributes(self.graph, {edge: {
                "weight": randint(1, 10)
            } for edge in self.graph.edges()})
        if namefile is not None:
            nx.write_edgelist(self.graph, namefile)

    def load(self, namefile : str) -> None:
        self.graph = nx.read_edgelist(namefile, nodetype=int)
        self.pos = nx.circular_layout(self.graph)

        nx.set_node_attributes(self.graph, 'whitesmoke', name='color')
        nx.set_edge_attributes(self.graph, 'black', name='color')

    def dfs(self, start):
        plt.figure(figsize=(10, 8))
        self.graph.nodes[start]['color'] = 'orangered'
        self._dfs(start)
        plt.axis('off')
        plt.show()

    def _dfs(self, current, visited=set()):
        visited.add(current)
        for next in ({n for n in self.graph.neighbors(current)} - visited):
            self.visualize_dfs(current, next)
            self._dfs(next, visited)
        return visited

    def visualize_dfs(self, current, next):
        nx.set_edge_attributes(self.graph,
                               {(current, next):
                                    {"color" : "orange" if
                                        self.graph.nodes[next]['color'] == 'whitesmoke'
                                     else "gray"}})
        self.graph.nodes[next]['color'] = 'maroon'
        self.graph.nodes[current]['color'] = 'maroon'
        plt.clf()
        nx.draw(self.graph, self.pos, with_labels=True, node_size=500, font_size=12,
                arrows=False, node_color=nx.get_node_attributes(self.graph, "color").values(),
                edge_color=nx.get_edge_attributes(self.graph, "color").values())
        self.graph.nodes[current]['color'] = 'orangered'
        self.graph.nodes[next]['color'] = 'orangered'
        plt.pause(0.5)

    def min_dist(self):
        minim = 1e7
        for v in self.graph.nodes:
            if self.graph.nodes[v]["distance"] < minim and \
                    self.graph.nodes[v]["checked"] == False:
                minim = self.graph.nodes[v]["distance"]
                index = v
        return index

    def dijkstra(self, start):
        plt.figure(figsize=(10, 8))
        
        nx.set_node_attributes(self.graph, 1e7, "distance")
        nx.set_node_attributes(self.graph, False, "checked")
        self.graph.nodes[start]['distance'] = 0

        for _ in self.graph.nodes:
            u = self.min_dist()
            self.graph.nodes[u]["checked"] = True
            self.graph.nodes[u]['color'] = 'orangered'

            for v in self.graph.nodes:
                try:
                    if self.graph.nodes[v]["checked"] == False and \
                        self.graph.nodes[v]["distance"] > self.graph.nodes[u]["distance"] + \
                            self.graph.edges[u, v]["weight"]:
                        self.graph.nodes[v]["distance"] = self.graph.nodes[u]["distance"] + \
                            self.graph.edges[u, v]["weight"]
                        self.visualize_dijkstra(v)
                except KeyError:
                    pass
            self.graph.nodes[u]['color'] = 'maroon'
        self.visualize_dijkstra(start)
        plt.axis('off')
        plt.show()

    def visualize_dijkstra(self, checked):
        self.graph.nodes[checked]['color'] = 'silver'
        state_pos = {n: (x + 0.12, y + 0.05) for n, (x,y) in self.pos.items()}
        plt.clf()
        nx.draw(self.graph, self.pos, with_labels=True, node_size=500, font_size=12,
                arrows=False, node_color=nx.get_node_attributes(self.graph, "color").values(),
                edge_color=nx.get_edge_attributes(self.graph, "color").values())
        nx.draw_networkx_labels(self.graph, state_pos,
                                labels=nx.get_node_attributes(self.graph, "distance"),
                                font_color="black")
        nx.draw_networkx_edge_labels(self.graph, self.pos,
                                     edge_labels=nx.get_edge_attributes(self.graph, "weight"))
        self.graph.nodes[checked]['color'] = 'whitesmoke'
        plt.pause(2)

    def find(self, parent, v):
        if parent[v] == v:
            return v
        return self.find(parent, parent[v])

    def union(self, parent, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if self.graph.nodes[x]["rank"] < self.graph.nodes[y]["rank"]:
            parent[xroot] = yroot
        elif self.graph.nodes[x]["rank"] > self.graph.nodes[y]["rank"]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            self.graph.nodes[xroot]["rank"] += 1

    def kruskal(self):
        plt.figure(figsize=(10, 8))
        nx.draw_networkx_nodes(self.graph, self.pos, node_size=500,
                               node_color=nx.get_node_attributes(self.graph, "color").values())
        nx.draw_networkx_labels(self.graph, self.pos, font_size=12)

        i, e = 0, 0
        parent, edges = {v : v for v in self.graph.nodes}, []
        s_edges = sorted(self.graph.edges(data=True),
                         key=lambda t: t[2].get("weight", 1))
        nx.set_node_attributes(self.graph, 0, name='rank')
        while e < len(self.graph.nodes)- 1:
            x = self.find(parent, s_edges[i][0])
            y = self.find(parent, s_edges[i][1])
            if x != y:
                e = e + 1
                edges.append(s_edges[i])
                self.union(parent, x, y)
                self.visualize_kruskal(edges)
            i += 1
        plt.axis('off')
        plt.show()

    def visualize_kruskal(self, edges):
        nx.draw_networkx_edges(self.graph, self.pos, edgelist=[edges[-1]],
                               edge_color="black")
        nx.draw_networkx_edge_labels(self.graph, self.pos,
                                     edge_labels={(edges[-1][0], edges[-1][1]): edges[-1][2]["weight"]})
        plt.pause(0.5)

G = Graph()
#G.generate(8, 0.3, weights=True, namefile="graph")
G.load("graph")

#G.dfs(1)
#G.dijkstra(6)
G.kruskal()