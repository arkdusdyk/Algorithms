import sys
from collections import deque
input = sys.stdin.readline
m,n = map(int, input().split(' '))
grid = []
for _ in range(n):
	grid.append(list(map(int, input().split(' '))))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def bfs():
	while q:
		y,x = q.popleft()
		for d in range(4):
			ny = y + dy[d]
			nx = x + dx[d]
			if (0<=nx<m) and (0<=ny<n):
				if grid[ny][nx] == 0:
					grid[ny][nx] = grid[y][x] + 1
					q.append((ny,nx))

q = deque()
for i in range(n):
	for j in range(m):
		if grid[i][j] == 1:
			q.append((i,j))

bfs()
answer = 0
zero_flag = False
for i in range(n):
	for j in range(m):
		if grid[i][j] == 0:
			zero_flag = True
			break
		answer = max(grid[i][j]-1, answer)
if zero_flag == True:
	print(-1)
else:
	print(answer)

# Difficulty : G5
# BFS