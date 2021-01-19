graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5,],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
def dfs(root):
    stack = [root]
    visited = [False for _ in range(9)]
    visited[root] = True
    print(root, end = ' ')
    while stack :
        top = stack[-1]
        cont = False
        next_v=0
        for next_v in graph[top]:
           if visited[next_v] == False:
                visited[next_v] = True
                cont = True
                print(next_v, end = ' ')
                stack.append(next_v)
                break
        if cont == False:   #no more adjacent nodes
            stack.pop()

dfs(1)
