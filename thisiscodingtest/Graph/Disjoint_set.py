import sys
'''
def find_parent(parent, x):	#recursive style-> O(V) 
	if parent[x] != x:
		return find_parent(parent, parent[x])
	return x
'''
def find_parent(parent, x):	#Compressed Path -> update parent table, find root quickly -> O(V + MlogV)
	if parent[x]  != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a,b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a<b:
		parent[b] = a
	else:
		parent[a] = b

v, e = map(int, sys.stdin.readline().split())
parent = [0] * (v+1)
for i in range(1, v+1):	#initialize parent table
	parent[i] = i
for i in range(e):
	a,b = map(int, sys.stdin.readline().split())
	union_parent(parent,a,b)

print('각 원소가 속한 집합: ', end = ' ')
for i in range(1, v+1):
	print(find_parent(parent, i), end = ' ')
print()
print('부모 테이블: ', end = ' ')
for i in range(1,v+1):
	print(parent[i], end = ' ')