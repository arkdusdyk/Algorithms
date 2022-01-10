import sys
from collections import deque
input = sys.stdin.readline
n,m,v = map(int,input().split())
adj = [[] for i in range(n+1)]
visit = [False for _ in range(n+1)]
for i in range(m):
	a, b = map(int, input().split())
	adj[a].append(b)
	adj[b].append(a)

for i in range(len(adj)):		# 작은 vertex부터
	adj[i].sort()

def dfs(start, visited):
	visited[start] = True
	print(start, end = " ")
	for i in adj[start]:
		if not visited[i]:
			dfs(i, visited)

def bfs(start, visited):
	q = deque()
	q.append(start)
	visited[start] = True
	while q:
		v = q.popleft()
		print(v, end = " ")
		for i in adj[v]:
			if not visited[i]:
				q.append(i)
				visited[i] = True

dfs(v, visit)
print()
visit = [False for _ in range(n+1)]	# visit 초기화 
bfs(v, visit)
print()

'''
Difficulty : S2
Basic DFS & BFS
'''