def dfs(start_point: int, graph: list) -> list:
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited

def bfs(start_point: int, graph: list) -> list:
    lengths = [None] * len(graph)
    lengths[start_point] = 0
    queue = [start_point]
    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)
    return lengths

#Ввод:
start = 3
graph1 = [
    # список смежности
    [1, 3],         # 0
    [0, 3, 4, 5],   # 1
    [4, 5],         # 2
    [0, 1, 5],      # 3
    [1, 2],         # 4
    [1, 2, 3],      # 5
    [7],            # 6
    [6]             # 7
]

#Вывод:
# path_graph = dfs(start, graph1)
path_graph = bfs(start, graph1)
print(path_graph)