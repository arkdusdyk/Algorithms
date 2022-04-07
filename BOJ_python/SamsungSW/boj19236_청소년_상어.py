import sys
import copy
input = sys.stdin.readline
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
arr = [list(map(int, input().split(' '))) for _ in range(4)]
fish = [[] for _ in range(4)]
direction = [[] for _ in range(4)]
for i in range(4):
	for j in range(0, len(arr[0]), 2):
		fish[i].append(arr[i][j])
	for j in range(1, len(arr[0]), 2):
		direction[i].append(arr[i][j]-1)

def find_fish(fish, fish_n):
	for f_i in range(4):
		for f_j in range(4):
			if fish[f_i][f_j] == fish_n:
				return f_i,f_j
	return False

def move_fish(fish, direction, s_y, s_x):		# s_y , s_x : shark 위치
	for n in range(1, 17):
		find_res = find_fish(fish, n)
		if find_res == False:
			continue
		else:
			fish_y, fish_x = find_res
			fish_dir = direction[fish_y][fish_x]
			#print("move:", fish_y, fish_x, fish_dir)
			orig = fish_dir
			while True:
				move_flag = False
				ny = fish_y + dy[fish_dir]
				nx = fish_x + dx[fish_dir]
				#print("with:", ny, nx)
				if 0 <= ny < 4 and 0 <= nx < 4:
					if not((ny==s_y) and (nx==s_x)):	# move fish
						fish[ny][nx], fish[fish_y][fish_x] = fish[fish_y][fish_x], fish[ny][nx]
						direction[ny][nx], direction[fish_y][fish_x] = fish_dir, direction[ny][nx]
						move_flag = True
				if move_flag == True:
					break
				fish_dir = (fish_dir+1)%8
				if orig == fish_dir:
					break

def dfs(fish, direction, i, j, total):
	global answer
	shark_i, shark_j = i,j
	shark_dir = direction[i][j]
	eat = fish[i][j]
	fish[i][j] = 0
	direction[i][j] = -1
	move_fish(fish, direction, shark_i, shark_j)
	answer = max(answer, total + eat)
	shark_moves = []
	for c in range(1, 5):
		n_sy = shark_i + (c*dy[shark_dir])
		n_sx = shark_j + (c*dx[shark_dir])
		if (0<=n_sy<4) and (0<=n_sx<4):
			if fish[n_sy][n_sx] > 0:
				shark_moves.append((n_sy,n_sx))
	for next_y, next_x in shark_moves:
		dfs(copy.deepcopy(fish), copy.deepcopy(direction), next_y, next_x, total + eat)

answer = 0
dfs(fish, direction, 0,0,0)
print(answer)

# Difficulty : G2
# 삼성 SW 역량 테스트 기출 문제집
# 백트래킹 문제 -> DFS로
# DFS로 배열이 변하도록, 또는 안바뀌도록, 유지하기 위해
# parameter로 넘겨줄지 전역변수로 선언할지, deepcopy로 처리하는지.. 이 부분이 정말 오래 걸렸다.
# 이런건 계속 연습하는 수 밖에