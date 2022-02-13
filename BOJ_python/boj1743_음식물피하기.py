import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n,m,k = map(int, input().split())
hall = []
visited = [[False]*m for _ in range(n)]
for _ in range(n):
	hall.append([False]*m)
for _ in range(k):
	r, c = map(int, input().split())
	hall[r-1][c-1] = True

def bfs(y,x):
	q = deque()
	q.append((y,x))
	visited[y][x] = True
	tmp = 1
	while q:
		y,x = q.popleft()
		for i in range(4):
			nx = x+dx[i]
			ny = y+dy[i]
			if (0<=nx<m) and (0<=ny<n):
				if hall[ny][nx] == True and visited[ny][nx] == False:
					tmp += 1
					q.append((ny,nx))
					visited[ny][nx] = True
	return tmp

answer = 0
for i in range(n):
	for j in range(m):
		if hall[i][j] == True and visited[i][j] == False:
			res = bfs(i,j)
			answer = max(res, answer)
print(answer)
'''
import sys
input = sys.stdin.readline
sys.getrecursionlimit(10*4)
dx = [-1,0,1,0]
dy = [0,-1,0,1]
n,m,k = map(int, input().split())
hall = []
visited = [[False]*m for _ in range(n)]
for _ in range(n):
	hall.append([False]*m)
for _ in range(k):
	r, c = map(int, input().split())
	hall[r-1][c-1] = True

def dfs(i,j,visited):
	global cnt
	visited[i][j] = True
	cnt+=1
	for k in range(4):
		nx = j + dx[k]
		ny = i + dy[k]
		if (0<=ny<n) and (0<=nx<m):
			if visited[ny][nx] == False and hall[ny][nx] == True:
				dfs(ny,nx,visited)

answer = 0
for i in range(n):
	cnt = 0
	for j in range(m):
		if visited[i][j] == False and hall[i][j] == True:
			dfs(i,j,visited)
			answer = max(cnt,answer)

print(answer)

Difficulty : S1
근처에 있는 것 끼리 뭉친다? => DFS/BFS
1. BFS로 쉽게 해결 가능
2. DFS로 한 번 풀어보자 => 주석 부분
	- 런타임에러(RecursionError) : recursionlimit 설정해주면서 재귀깊이 한계를 주어서 해결함.
	- 런타임에러(TypeError) : 해결 X. 나왔는데 도대체 어딘지..?
'''