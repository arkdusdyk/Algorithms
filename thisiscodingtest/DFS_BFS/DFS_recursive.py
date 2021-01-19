def dfs(visited, v, graph):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == False :
            dfs(visited, i, graph)

visited = [False for _ in range(9)]
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
dfs(visited, 1, graph)
