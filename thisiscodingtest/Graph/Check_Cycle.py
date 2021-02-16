import sys
def find_parent(parent, x):
	if parent[x]!=x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a<b:
		parent[b] = a
	else:
		parent[a] = b

flag = False
v, e = map(int, sys.stdin.readline().split())
parent = [0]*(v+1)
for i in range(1, v+1):
	parent[i] = i

for i in range(e):
	a, b = map(int, sys.stdin.readline().split())
	if(find_parent(parent, a)==find_parent(parent, b)):	#cycle
		flag = True
		break
	else:
		union_parent(parent, a,b)

if(flag):
	print("Graph is cyclic")
else:
	print("Graph is acyclic")
'''
check if given graph forms a cycle, using disjoint set.
: only works if graph has no direction
'''