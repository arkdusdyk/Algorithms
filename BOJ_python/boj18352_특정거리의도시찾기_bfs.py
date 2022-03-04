import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
cost = [0]*(n+1)
visited = [False]*(n+1)
path = [[] for _ in range(n+1)]


def bfs(start):
	answer = []
	q = deque()
	q.append(start)
	visited[start] = True
	cost[start] = 0
	while q:
		cur = q.popleft()
		for nx in path[cur]:
			if visited[nx] == False:
				visited[nx] = True
				q.append(nx)
				cost[nx] = cost[cur] + 1
				if cost[nx] == k:
					answer.append(nx)
	if len(answer) == 0:
		print(-1)
	else:
		answer.sort()
		for v in answer:
			print(v)

for _ in range(m):
	a,b = map(int, input().split())
	path[a].append(b)

bfs(x)


'''
Difficulty : S2
BFS Ver.
cost가 모두 1이고 최단거리기 때문에 BFS로 간단히 해결 가능.
메모리 : 177060KB, 시간 : 1184ms
'''