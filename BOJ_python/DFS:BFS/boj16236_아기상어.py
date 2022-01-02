import sys
from collections import deque
input = sys.stdin.readline
MAX = int(1e9)

size = 2
n = int(input())
arr = []
for i in range(n):
	arr.append(list(map(int, input().split())))
fish_pos = []
baby_x, baby_y = (0,0)
cnt = 0
for i in range(n):
	for j in range(n):
		if 0< arr[i][j] <= 6:
			fish_pos.append((i,j))
			cnt += 1
		elif arr[i][j] == 9:
			baby_x, baby_y = (i,j)
			arr[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(baby_x, baby_y):
	q = deque()
	q.append((baby_x, baby_y, 0))
	visited[baby_x][baby_y] = True
	dist_list = []
	min_dist = MAX
	while q:
		x, y, dist = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < n:
				if visited[nx][ny] == True:
					continue
				else:
					if arr[nx][ny] <= size:		# can pass
						visited[nx][ny] = True
						if 0 < arr[nx][ny] < size:
							min_dist = dist
							dist_list.append((dist+1, nx, ny))
						if dist+1 <= min_dist:
							q.append((nx,ny, dist+1))
	if dist_list:		#found next
		dist_list.sort()
		return dist_list[0]
	else:
		return False
	
time = 0
exp = 0
while cnt > 0:
	visited = [[False]*n for _ in range(n)]
	res = bfs(baby_x, baby_y)
	if res == False:
		break
	time += res[0]
	baby_x, baby_y = res[1], res[2]
	cnt -= 1
	exp += 1
	if size == exp:		#size up
		exp = 0
		size +=1
	arr[baby_x][baby_y] = 0 # empty current

print(time)
'''
Difficulty : G4
BFS, 구현
큐에 거리까지 저장해놓는게 굉장히 좋은 아이디어 같다..
'''