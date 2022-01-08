import sys
input = sys.stdin.readline
n = int(input())
tree = []
for _ in range(n):
	k = int(input())
	tree.append(k)
tree.sort()

tree_dist = []
for i in range(1, n):
	tree_dist.append(tree[i]-tree[i-1])

def gcd(x,y):
	while(y):
		x,y = y, x%y
	return x

min_dist = tree_dist[0]
for i in range(1, len(tree_dist)):
	min_dist = gcd(min_dist, tree_dist[i])

print((tree[-1]-tree[0])//min_dist - n +1)

'''
Difficulty : S4
어렵지 않은 문제. 유클리드 호제법 최대공약수 gcd함수에 익숙해지기.
'''