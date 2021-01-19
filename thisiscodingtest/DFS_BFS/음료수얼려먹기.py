def dfs(x,y, graph):
	if(x<0 or x>=n or y<0 or y>=m):
		return
	if graph[x][y] == 0:
		graph[x][y] = 1
		dfs(x-1, y, graph)
		dfs(x+1, y, graph)
		dfs(x, y+1, graph)
		dfs(x, y-1, graph)

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
cnt=0
for i in range(n):
	for j in range(m):
		if(graph[i][j]==0):	#start dfs
			dfs(i,j,graph)
			cnt+=1
print(cnt)

'''    
그래프 탐색을 하면서 인접하지 않은 0들의 갯수 구하기
: (끝까지 가는게 중요할듯)-> DFS

2차원 배열 입력 기본:
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
'''