import sys
def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a,b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

total =0
n,m = map(int, sys.stdin.readline().split())
parent = [0]*(n+1)
for i in range(1, n+1):
	parent[i] = i
edges = []
for _ in range(m):
	a,b,c = map(int, sys.stdin.readline().split())
	edges.append((c,a,b))
edges.sort()
last =0
for edge in edges:
	c,a,b = edge
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent,a,b)
		total+= c
		last = c
print(total-last)
'''
Difficulty : G4
Separating graph into two spanning trees -> Use Kruskal to find Spanning Trees
Separate the last edge (max cost edge)
'''