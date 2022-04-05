import sys
from collections import deque
input = sys.stdin.readline
MAX = int(1e9)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
# 입력
n = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(n)]

fish_cnt = 0
baby_size = 2
baby_y, baby_x = 0, 0
for i in range(n):
	for j in range(n):
		if arr[i][j] == 9:
			baby_y, baby_x = i,j
		elif 0 < arr[i][j] <= 6:
			fish_cnt += 1

def bfs(b_y, b_x):
	q = deque()
	q.append((b_y, b_x, 0))
	min_dist = MAX
	eat_list = []		# (eat_distance, move_y, move_x)
	arr[b_y][b_x] = 0
	while q:
		y,x,dist = q.popleft()
		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]
			if (0<=ny<n) and (0<=nx<n):
				if visited[ny][nx] == False:
					if arr[ny][nx] <= baby_size:		# move 가능
						visited[ny][nx] = True
						if 0 < arr[ny][nx] < baby_size:		# can eat
							min_dist = dist
							eat_list.append((dist+1, ny, nx))
						if dist+1 <= min_dist:		# 움직이고 다음 move도 확인해보자
							q.append((ny,nx, dist+1))
	if len(eat_list) > 0:
		eat_list.sort()
		return eat_list[0]
	else:
		return False

time = 0
exp = 0
while fish_cnt > 0:
	visited = [[False]*n for _ in range(n)]
	visited[baby_y][baby_x] = True
	result = bfs(baby_y, baby_x)
	if result == False:
		break
	dist, baby_y, baby_x = result
	time += dist
	exp += 1
	fish_cnt -=1
	if baby_size == exp:
		baby_size += 1
		exp = 0
print(time)

# Difficulty : G3
# 삼성 SW 역량 테스트 기출 문제집
# BFS 를 쓰면 좋을 것 같다는 생각. (가까운 먹이부터)