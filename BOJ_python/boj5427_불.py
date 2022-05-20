from collections import deque
import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
	t = 0
	while sg:
		t += 1
		while fire:
			y, x, cur = fire.popleft()
			if cur >= t:
				break
			for d in range(4):
				ny = y + dy[d]
				nx = x + dx[d]
				if (0<=ny<h) and (0<=nx<w):
					if building[ny][nx] == '.' or building[ny][nx] == '@':
						building[ny][nx] = '*'
						fire.append((ny,nx, cur+1))
		while sg:
			y, x, cur = sg.popleft()
			if cur >= t:
				break
			for d in range(4):
				ny = y + dy[d]
				nx = x + dx[d]
				if (0<=ny<h) and (0<=nx<w):
					if building[ny][nx] == '.':
						if visited[ny][nx] == False:
							sg.append((ny,nx, cur+1))
							visited[ny][nx] = True
				else:
					return t
	return False

t_case = int(input())
for _ in range(t_case):
	w, h = map(int, input().split(' '))
	building = []
	for _ in range(h):
		building.append(list(input().strip()))
	visited = [[False]* w for _ in range(h)]
	sg = deque()
	fire = deque()
	for i in range(h):
		for j in range(w):
			if building[i][j] == '@':
				sg.append((i,j))
				visited[i][j] = 0
			elif building[i][j] == '*':
				fire.append((i,j))
	result = bfs()
	if result == False:
		print("IMPOSSIBLE")
	else:
		print(result)

# Difficulty : G4
# BFS