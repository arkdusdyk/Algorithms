import sys
def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a,b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a<b:
		parent[b] = a
	else:
		parent[a] = b

n,m = map(int, sys.stdin.readline().split())
parent = [0]*(n+1)
for i in range(1, n+1):
	parent[i] = i

for _ in range(m):
	c,a,b = map(int, sys.stdin.readline().split())
	if c==0:
		union_parent(parent,a,b)
	elif c==1:
		if find_parent(parent, a) != find_parent(parent, b):
			print("NO")
		else:
			print("YES")
'''
간단하게 '팀합치기'연산과 '같은팀여부확인'연산 둘로 나눈 문제
직관적으로 Disjoint Set으로 해결 가능
'''