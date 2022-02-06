import sys
from collections import deque
input = sys.stdin.readline
field = []

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def bfs(y,x):
	cur = field[y][x]
	q = deque()
	q.append((y,x))
	visited = [[False]*6 for _ in range(12)]
	visited[y][x] = True
	poplist = [(y,x)]
	while q:
		y,x = q.popleft()
		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]
			if (0<=nx<6) and (0<=ny<12):
				if (field[ny][nx] == cur) and (visited[ny][nx]==False):
					q.append((ny,nx))
					visited[ny][nx] = True
					poplist.append((ny,nx))
	if len(poplist) >= 4:
		for coord in poplist:
			field[coord[0]][coord[1]] = '.'
		return True
	return False

def nextfield():
	for i in range(10,-1,-1):
		for j in range(6):
			if (field[i][j] != '.') and (field[i+1][j] == '.'):		# fall
				for k in range(i+1, 12):
					if field[k][j] == '.':		# last line
						if k == 11:
							field[k][j] = field[i][j]
					else:
						if field[k][j] != '.':
							field[k-1][j] = field[i][j]
							break
				field[i][j] = '.'

for i in range(12):				# 필드 입력
	field.append(list(input().strip()))

answer = 0
while True:
	cnt = 0
	for i in range(12):
		for j in range(6):
			if field[i][j] != '.':
				pop_flag = bfs(i,j)
				if pop_flag == True:		# 연쇄 발생!
					cnt += 1
	if cnt == 0:
		break
	answer += 1
	nextfield()
print(answer)

'''
Difficulty : G4
BFS & Simulation
'''