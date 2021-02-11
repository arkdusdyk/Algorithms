import sys
INF = int(1e9)	#INF = 10 billion
n, m = map(int, sys.stdin.readline().split())	#n : node, m: edges
start = int(sys.stdin.readline())	#start node
graph = [[] for i in range(n+1)]	#graph info of connected nodes
visited = [False]*(n+1)
distance = [INF]*(n+1)			#shortest path table

for _ in range(m):
	a,b,c = map(int, sys.stdin.readline().split())
	graph[a].append((b,c))


def get_smallest_node():
	min_value = INF
	idx =0
	for i in range(1, n+1):
		if distance[i] < min_value and not visited[i]:
			min_value = distance[i]
			idx = i
	return idx

def dijkstra(start):
	distance[start] = 0
	visited[start] = True
	for i in graph[start]:
		distance[i[0]] = i[1]
	for i in range(n-1):
		cur = get_smallest_node()
		visited[cur] = True
		for j in graph[cur]:	#check other nodes connected to current node
			cost = distance[cur] + j[1]
			if cost < distance[j[0]]:		#if previous cost > (passing current node) : update
				distance[j[0]] = cost

dijkstra(start)
for i in range(1, n+1):
	if distance[i] == INF:
		print("Can't Reach")
	else:
		print(distance[i])
'''O(V^2) version of Dijkstra (Simple Version)
Possible when vertex count <= 5000. If more, use Complex Version (using heap)
'''