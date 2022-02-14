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
Difficulty : S1
근처에 있는 것 끼리 뭉친다? => DFS/BFS
BFS로 쉽게 해결 가능
'''