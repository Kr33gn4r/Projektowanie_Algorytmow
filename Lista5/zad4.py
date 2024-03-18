#          0      1      2      3      4      5      6      7      8      9      10
graf = [[False, False, False, False, False, False, False, False, False, False, False],  #0
        [False, False, True,  True,  False, False, False, False, False, False, False],  #1
        [False, True,  False, False, True,  True,  False, False, False, False, False],  #2
        [False, True,  False, False, False, False, True,  False, False, False, False],  #3
        [False, False, True,  False, False, False, False, True,  False, False, False],  #4
        [False, False, True,  False, False, False, True,  False, True,  False, False],  #5
        [False, False, False, True,  False, True,  False, False, False, False, False],  #6
        [False, False, False, False, True,  False, False, False, False, True,  False],  #7
        [False, False, False, False, False, True,  False, False, False, True,  True ],  #8
        [False, False, False, False, False, False, False, True,  True,  False, False],  #9
        [False, False, False, False, False, False, False, False, True,  False, False]]  #10

def recursion_graph(graph, startingpoint, endingpoint):
    visited = [False for i in range(len(graph))]
    visited[startingpoint] = True
    result = visiting(graph, visited, startingpoint, endingpoint)
    #print(result)
    if not result: print("Nie znaleziono żadnej ścieżki")
    else:
        smallestindex = 0
        for index in range(0, len(result), 2):
            if result[smallestindex] > result[index]: smallestindex = index
        print(f"Znaleziono najmniejszą ścieżkę o długości {result[smallestindex]} prowadzącą przez {result[smallestindex + 1]}")


def visiting(graph, visited, currentpoint, endpoint, nodes = [], path=0):
    newnodes = nodes.copy()
    newnodes.append(currentpoint)
    temp = []
    for i in range(len(graph)):
        if graph[currentpoint][i]:
            if not visited[i]:
                if i == endpoint:
                    newnodes.append(endpoint)
                    return [path + 1, newnodes]
                newvisit = visited.copy()
                newvisit[i] = True
                resp = visiting(graph, newvisit, i, endpoint, newnodes, path + 1)
                temp.extend(resp)
    return temp

recursion_graph(graf, 1, 0)