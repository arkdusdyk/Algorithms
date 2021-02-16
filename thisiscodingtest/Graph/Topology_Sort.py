import sys
from collections import deque
v,e = map(int, sys.stdin.readline().split())
indegree = [0]*(v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
	a,b = map(int, sys.stdin.readline().split())
	graph[a].append(b)
	indegree[b] += 1

#Topology Sort
def topology_sort():
	result = []
	q = deque()
	for i in range(1, v+1):
		if indegree[i]==0:	#push initial node with indegree:0
			q.append(i)
	while q:
		front = q.popleft()
		result.append(front)	#when popped, save at result
		for i in graph[front]:
			indegree[i]-=1
			if indegree[i] ==0:
				q.append(i)
	for i in result:
		print(i, end = ' ')

topology_sort()
'''
Topology Sort : O(V+E)
from initial node(indegree=0) -> start searching connected vertex node, push in queue
Must assume acyclic graph.
'''