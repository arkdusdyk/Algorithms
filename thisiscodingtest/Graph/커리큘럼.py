import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]
indegree = [0]*(n+1)
time = [0]*(n+1)
for i in range(1, n+1):
	info = list(map(int, sys.stdin.readline().rsplit()))
	time[i] = info[0]
	for j in info[1:-1]:
		graph[j].append(i)
		indegree[i] += 1

result = [0]*(n+1)
for i in range(1,n+1):
	result[i] = time[i]
def topology_sort():
	q = deque()
	for i in range(1, n+1):
		if indegree[i] ==0:		#finding initial node
			q.append(i)

	while(q):
		front = q.popleft()
		for i in graph[front]:
			result[i] = max(result[i], result[front]+time[i])
			indegree[i] -=1
			if indegree[i] == 0:
				q.append(i)

	for i in range(1, n+1):
		print(result[i])

topology_sort()
'''
Topology Sort
'''