import sys
input = sys.stdin.readline
# n,m,k 입력 (n: 격자, m : 상어, k : 이동 횟수)
n,m,k = map(int, input().split(" "))
time = 0
grid = []
shark = [[] for _ in range(m)]
cnt = m
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]
# 격자 입력
for _ in range(n):
	grid.append(list(map(int, input().split(" "))))
# 각 상어 보고 있는 방향 입력 (1,2,3,4 : 위 아래 왼 오)
cur_dir = list(map(int, input().split(" ")))

# 우선순위 저장
next_dir = [[] for _ in range(m)]

# 4줄씩 각 상어 방향 우선순위
for i in range(m):
	for j in range(4):
		next_dir[i].append(list(map(int,input().split(" "))))

# 상어 위치 저장 (숫자 순서)
for i in range(n):
	for j in range(n):
		if grid[i][j] > 0:
			shark[grid[i][j]-1] = (i,j)

# 냄새 저장할 배열  [냄새 주인, 냄새 timer]
scent = [[[0,0] for _ in range(n)] for _ in range(n)]
for i in range(m):
	s_y, s_x = shark[i]
	scent[s_y][s_x] = [i+1, k]

while cnt > 1:
	time += 1
	if time > 1000:
		time = -1
		break
	for i in range(m):
		y, x = shark[i]
		if x < 0 or y < 0: 	# 먹힌 상어 : -1 로 처리
			continue
		face = cur_dir[i]	# 1,2,3,4
		poss = []
		my = []
		next_y, next_x, n_dir = None, None, None
		for j in range(1,5):
			ny = y + dy[j]
			nx = x + dx[j]
			if (0 <= nx < n) and (0<= ny < n):
				if scent[ny][nx][0] == 0:
					poss.append((ny,nx))
					n_dir = j
				if scent[ny][nx][0] == (i+1):	# 본인 scent
					my.append((ny,nx,j))
		if len(poss) > 0:		# 냄새 없는 칸 존재
			if len(poss) == 1:		# 냄새 없는 칸 하나 = 갈 수 있는 칸 하나 (바로 이동)
				next_y, next_x = poss[0]
			else:					# 냄새 없는 칸 여러개 (우선 순위 확인)
				for j in range(4):
					n_dir = next_dir[i][face-1][j]
					ny = y + dy[n_dir]
					nx = x + dx[n_dir]
					if (0 <= nx < n) and (0 <= ny < n):
						if scent[ny][nx][0] == 0:
							next_y, next_x = ny, nx
							break
		else:					# 냄새 없는 칸 없음
			if len(my) == 1:		# 본인의 냄새 하나 존재 (바로 해당 칸 이동)
				next_y, next_x, n_dir = my[0]
			elif len(my) > 1:		# 본인의 냄새 여러개 (우선순위 확인)
				for j in range(4):
					n_dir = next_dir[i][face-1][j]
					ny = y + dy[n_dir]
					nx = x + dx[n_dir]
					if (0 <= nx < n) and (0 <= ny < n):
						if scent[ny][nx][0] == (i+1):
							next_y, next_x = ny, nx
							break
		# 상어 이동 + 냄새 남기기
		cur_dir[i] = n_dir
		shark[i] = (next_y, next_x)
		grid[y][x] = 0
	for i in range(n):
		for j in range(n):
			if scent[i][j][0] > 0:
				scent[i][j][1] -= 1
			if scent[i][j][1] == 0:
				scent[i][j][0] = 0
	# 여러 상어가 한 칸에 (작은 것 빼고 모두 제거 shark x,y : -1로 처리)
	for i in range(m):
		tmp_y, tmp_x = shark[i]
		if tmp_y == -1 or tmp_x == -1:
			continue
		if 0 < grid[tmp_y][tmp_x] < (i+1):
			cnt -= 1
			shark[i] = (-1,-1)
		else:
			grid[tmp_y][tmp_x] = i+1
			scent[tmp_y][tmp_x] = [i+1, k]
	'''
	print("GRID:")
	for i in range(n):
		for j in range(n):
			print(grid[i][j], end = ' ')
		print()
	print("SHARKS:")
	print(shark)
	print("CUR DIRECTIONS:")
	print(cur_dir)
	print("SCENTS:")
	for i in range(n):
		for j in range(n):
			print(scent[i][j], end = ' ')
		print()
	'''
print(time)

# Difficulty : G3
# 삼성 SW 역량 테스트 기출 문제집 - Simulation