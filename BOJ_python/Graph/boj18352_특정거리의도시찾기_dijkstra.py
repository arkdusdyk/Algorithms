import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
cost = [INF]*(n+1)
visited = [False]*(n+1)
path = [[] for _ in range(n+1)]

for _ in range(m):
	a,b = map(int, input().split())
	path[a].append(b)

def dijkstra(start):
	answer = []
	q = []
	heapq.heappush(q, (0, start))
	cost[start] = 0
	while q:
		dist, cur = heapq.heappop(q)
		if cost[cur] < dist:
			continue
		for dest in path[cur]:
			c = dist + 1
			if c < cost[dest]:
				cost[dest] = c
				heapq.heappush(q, (c, dest))
	for i in range(len(cost)):
		if cost[i] == k:
			answer.append(i)

	if len(answer)==0:
		print(-1)
	else:
		for i in answer:
			print(i)

dijkstra(x)

'''
Dijkstra Ver.
음의 간선이 없기 때문에 가능. cost 도 모두 1이니깐 path[i]마다 cost 따로 저장 필요 X
-> Dijkstra는 O(ElogV) > bfs의 O(n). BFS로 하는게 나을 것이라고 예상됨.
메모리 : 182852KB, 시간 : 1624ms
BFS 로 해결가능하면 BFS로 풀자ㅋㅋㅋ
'''