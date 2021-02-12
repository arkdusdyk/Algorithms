import heapq
import sys
INF = int(1e9)	#10 bil = INF
n,m = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]
dist = [INF] *(n+1)

for _ in range(m):	#input of graph edge info
	a,b,c = map(int, sys.stdin.readline().split())
	graph[a].append((b,c))

def dijkstra(start):
	q = []
	heapq.heappush(q,(0,start))	#initial start node push with dist:0
	dist[start] =0
	while q:
		min_dist, cur = heapq.heappop(q)
		if dist[cur] < min_dist :	#already checked
			continue
		for i in graph[cur]:
			cost = min_dist + i[1]
			if cost < dist[i[0]]:
				dist[i[0]] = cost
				heapq.heappush(q,(cost, i[0]))

dijkstra(start)
for i in range(1, n+1):
	if dist[i] == INF:
		print("Can't Reach")
	else :
		print(dist[i])
'''
Dijkstra using min heap (priority queue : Insertion, Deletion both O(logN))
=> O(ElogV).
heapq in python : 1. consists of tuples () 2. min heap (insertion, deletion) 3. when inserting, deleting, compare the first element of tuple (cost)
'''