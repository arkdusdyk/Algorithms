import sys
input = sys.stdin.readline
n = int(input())
students = n**2
likes = [[] for _ in range((students)+1)]
order = []
for i in range(students):
	tmp = list(map(int, input().split(' ')))
	likes[tmp[0]] = tmp[1:]
	order.append(tmp[0])

room = [[0]*n for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for idx in range(len(order)):
	cur = order[idx]
	max_adj = 0
	candid = []
	for i in range(n):
		for j in range(n):
			adj = 0
			if room[i][j] == 0:			# 비어있는 칸
				for d in range(4):
					ny = i + dy[d]
					nx = j + dx[d]
					if (0<=nx<n) and (0<=ny<n):
						if room[ny][nx] in likes[cur]:
							adj += 1
				if adj > max_adj:
					max_adj = adj
					candid = [(i,j)]
				elif adj == max_adj:
					candid.append((i,j))
	if len(candid) == 1:
		y,x = candid[0]
		room[y][x] = cur
	elif len(candid) > 1:
		# 2 확인
		second_candid = []
		max_blanks = 0
		for i in range(len(candid)):
			y, x = candid[i]
			blanks = 0
			for d in range(4):
				ny = y + dy[d]
				nx = x + dx[d]
				if (0<=nx<n) and (0<=ny<n):
					if room[ny][nx] == 0:
						blanks += 1
			if blanks > max_blanks:
				max_blanks = blanks
				second_candid = [(y,x)]
			elif blanks == max_blanks:
				second_candid.append((y,x))
		if len(second_candid) == 1:
			y, x = second_candid[0]
			room[y][x] = cur
		elif len(second_candid) > 1:
			# 3 확인
			third_candid = sorted(second_candid)
			y, x = third_candid[0]
			room[y][x] = cur

answer = 0
for i in range(n):
	for j in range(n):
		adj = 0
		cur = room[i][j]
		for d in range(4):
			ny = i + dy[d]
			nx = j + dx[d]
			if (0<=nx<n) and (0<=ny<n):
				for k in range(4):
					if room[ny][nx] == likes[cur][k]:
						adj += 1
		if adj > 0:
			answer += (10**(adj-1))
print(answer)

# Difficulty : G5
# 삼성 SW 역량 테스트 기출 문제집 - Simulation
# 인접한 것만 확인하면 되는 것이어서 간단한 구현 문제