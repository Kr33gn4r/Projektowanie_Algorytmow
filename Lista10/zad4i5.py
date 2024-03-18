"""
macierz incydencji mówi o tym że krawędź e_i łączy wierzchołki A i B
macierz sąsiedztwa wyznacza czy wierzchołek A jest połączony z wierzchołkiem B
"""
import numpy as np
from random import choice

class Graf():
    def __init__(self, V, q):
        self.V = V
        self.E = int(q * (self.V * (self.V - 1)) / 2)

        self.MI = [[0 for _ in range(self.E)] for __ in range(self.V)]
        self.MS = [[0 for _ in range(self.V)] for __ in range(self.V)]
        visited = []
        varray = [_ for _ in range(self.V - 1)]

        for _ in range(self.E):
            while True:
                a = choice(varray)
                b = choice([_ for _ in range(a+1, self.V)])

                if (a, b) not in visited:
                    visited.append((a, b))
                    self.MI[a][_], self.MI[b][_] = 1, 1
                    self.MS[a][b], self.MS[b][a] = 1, 1
                    break
    def ssMI(self):
        sets = [_ for _ in range(self.V)]
        for edge in np.array(self.MI).T:
            vertices = [i for i, x in enumerate(edge) if x == 1]
            if sets[vertices[0]] != sets[vertices[1]]:
                union = [i for i, x in enumerate(sets) if x == sets[vertices[1]]]
                for v in union:
                    sets[v] = sets[vertices[0]]
        s = []
        for v in np.unique(sets):
            s.append([i for i, x in enumerate(sets) if x == v])
        return s

    def ssMS(self):
        sets = [_ for _ in range(self.V)]
        for row in range(len(self.MS)):
            for col in range(row):
                if self.MS[row][col] == 1:
                    if sets[row] != sets[col]:
                        union = [i for i, x in enumerate(sets) if x == sets[col]]
                        for v in union:
                            sets[v] = sets[row]

        s = []
        for v in np.unique(sets):
            s.append([i for i, x in enumerate(sets) if x == v])
        return s


g = Graf(100, 0.01)

for _ in g.MI:
    print(_)

print()

for _ in g.MS:
    print(_)

print()
print(sorted(g.ssMI()))
print(sorted(g.ssMS()))
print(len(g.ssMS()))

