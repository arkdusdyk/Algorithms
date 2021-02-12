import sys
INF = int(1e9)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):	#node i -> i cost : 0
	for b in range(1, n+1):
		if a==b:
			graph[a][b]=0

for _ in range(m):
	a,b,c = map(int, sys.stdin.readline().split())
	graph[a][b] = c

for k in range(1, n+1):
	for i in range(1, n+1):
		for j in range(1, n+1):
			graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, n+1):		#print final distance in 2D. if can't reach : X
	for j in range(1, n+1):
		if graph[i][j]== INF:
			print("X", end = ' ')
		else:
			print(graph[i][j], end = ' ')
	print()
'''
Floyd Warshall Algorithm : O(n^3)
use 2d list "graph" to record distance
Recurrence Relation : min (graph[i][j], graph[i][k]+graph[k][j])
'''