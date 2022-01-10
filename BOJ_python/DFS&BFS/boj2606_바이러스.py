import sys
input = sys.stdin.readline

n = int(input())
visited = [False]*(n+1)
adj = [[] for _ in range(n+1)]
m = int(input())

for i in range(m):
	a,b = map(int, input().split())
	adj[a].append(b)
	adj[b].append(a)

answer = 0
def dfs(x):
	global answer
	visited[x] = True
	for v in adj[x]:
		if visited[v] == False:
			answer+=1
			dfs(v)
dfs(1)
print(answer)

'''
Difficulty : S3
Basic DFS
'''