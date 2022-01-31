import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def answer(graph):
	q = []
	heapq.heappush(q, (graph[0][0],(0,0)))
	distance[0][0] = graph[0][0]
	while q:
		dist, now = heapq.heappop(q)
		if distance[now[0]][now[1]] < dist:
			continue
		for i in range(4):
			ny = now[0] + dy[i]
			nx = now[1] + dx[i]
			if ny < 0 or ny >= n or nx < 0 or nx >= n:
				continue
			cost = dist + graph[ny][nx]
			if cost < distance[ny][nx]:
				distance[ny][nx] = cost
				heapq.heappush(q, (cost, (ny, nx)))
	return distance[n-1][n-1]

t = 1
while True:
	n = int(input())
	if n == 0:
		break
	distance = [[INF]*n for _ in range(n)]
	graph = []
	for _ in range(n):
		graph.append(list(map(int, input().split())))
	print("Problem %d: %d" %(t, answer(graph)))
	t+=1
	
'''
Difficulty : G4
Dijkstra 로 구현만 잘하면 쉽게 해결 가능
Python으로 Dijkstra로 처음 해보았는데, 시간초과보다는 메모리 초과가 걱정되었지만 다행히 문제 없었음.
'''