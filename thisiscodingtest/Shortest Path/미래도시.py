import sys
INF = int(1e9)
n,m = map(int, sys.stdin.readline().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
	a,b = map(int, sys.stdin.readline().split())
	graph[a][b] = 1
	graph[b][a] = 1
x,k = map(int, sys.stdin.readline().split())

for i in range(1,n+1):
	for j in range(1, n+1):
		if i==j :
			graph[i][j] = 0

for l in range(1, n+1):
	for i in range(1, n+1):
		for j in range(1, n+1):
			graph[i][j] = min(graph[i][j], graph[i][l] + graph[l][j])

if(graph[1][k]==INF or graph[k][x]==INF):
	print(-1)
else:
	print(graph[1][k] + graph[k][x])
'''
Try to find shortest path from node 1 -> K -> X
Must pass K: (Min cost of 1-> K) + (Min Cost of K->X)
Solve with Floyd-Warshall.
'''