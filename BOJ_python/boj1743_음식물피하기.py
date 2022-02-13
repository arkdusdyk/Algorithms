import sys
input = sys.stdin.readline
sys.getrecursionlimit()
dx = [-1,0,1,0]
dy = [0,-1,0,1]
answer = 0
n,m,k = map(int, input().split())
hall = []
visited = [[False]*m for _ in range(n)]
for _ in range(n):
	hall.append([False]*m)
for _ in range(k):
	r, c = map(int, input().split())
	hall[r-1][c-1] = True

def dfs(i,j, visited):
	global x
	visited[i][j] = True
	x+=1
	for k in range(4):
		nx = j + dx[k]
		ny = i + dy[k]
		if (0<=ny<n) and (0<=nx<m):
			if visited[ny][nx] == False and hall[ny][nx] == True:
				dfs(ny,nx,visited)

for i in range(n):
	for j in range(m):
		x = 0
		if visited[i][j] == False and hall[i][j] == True:
			dfs(i,j,visited)
			answer = max(x, answer)

print(answer)

'''
근처에 있는 것 끼리 뭉친다? => DFS/BFS
둘 다 풀 수 있을 것 같은데 최근에 BFS로 문제를 풀어서 이번에는 DFS 사용
'''