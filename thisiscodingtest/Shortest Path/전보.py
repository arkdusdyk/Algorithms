import sys
import heapq
INF = int(1e9)
n,m,c = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
dist = [INF]*(n+1)
for _ in range(m):
	x,y,z = map(int, sys.stdin.readline().split())
	graph[x].append((y,z))

def dijkstra():
	q = []
	heapq.heappush(q,(0,c))
	dist[c] = 0
	while(q):
		min_dist, cur = heapq.heappop(q)
		if dist[cur] < min_dist:
			continue
		for i in graph[cur]:
			cost = min_dist + i[1]
			if cost < dist[i[0]]:
				dist[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))
dijkstra()
cnt=0
max_dist=0
for i in dist:
	if i != INF and i!=0:
		cnt +=1
		if max_dist<i:
			max_dist = i
print(cnt, max_dist)
'''
Solve with Dijkstra
Count distance cost NOT INF
'''