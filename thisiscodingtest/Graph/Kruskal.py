import sys
def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]
def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a<b:
		parent[b] = a
	else:
		parent[a] = b

v,e = map(int, sys.stdin.readline().split())
parent = [0]*(v+1)
for i in range(1,v+1):
	parent[i] = i

edges = []
for _ in range(e):
	a,b,c = map(int, sys.stdin.readline().split())
	edges.append((c,a,b))	#edges : list contained of tuple of (cost, v1, v2)

total =0
edges.sort()	#정렬
for edge in edges:
	cost, a, b = edge
	if find_parent(parent,a) != find_parent(parent, b):	#added only when graph makes no cycle
		union_parent(parent,a,b)
		total += cost
print(total)
'''
Kruskal Algorithm: O(eloge)
Sort all edges, start adding (greedy) every edge unless it makes a cycle, add up cost
'''