import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
grid = []
for i in range(n):
	grid.append(list(map(int, input().split(' '))))

out = 0
dy = [0,1,0,-1]
dx = [-1,0,1,0]
sy = [-1, 1,-2, 2, 0, -1, 1, -1, 1, 0]		# 1, 1, 2, 2, 5, 7, 7, 10, 10, a
sx = [1, 1, 0, 0, -2, 0, 0, -1, -1,-1]

y,x = n//2, n//2
for i in range(1,n,2):
	for j in range(1,i+1):	# 좌
		cur = grid[y][x]
		y = y + dy[0]
		x = x + dx[0]
		out_tmp = 0
		for k in range(2): # 1%
			s_ny = y + sy[k]
			s_nx = x + sx[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.01)
				out_tmp += int(cur*0.01)
			else:
				out += int(cur*0.01)
		for k in range(2, 4): # 2%
			s_ny = y + sy[k]
			s_nx = x + sx[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.02)
				out_tmp += int(cur*0.02)
			else:
				out += int(cur*0.02)
		for k in range(4, 5): # 5%
			s_ny = y + sy[k]
			s_nx = x + sx[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.05)
				out_tmp += int(cur*0.05)
			else:
				out += int(cur*0.05)
		for k in range(5, 7): # 7%
			s_ny = y + sy[k]
			s_nx = x + sx[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.07)
				out_tmp += int(cur*0.07)
			else:
				out += int(cur*0.07)
		for k in range(7, 9): # 10%
			s_ny = y + sy[k]
			s_nx = x + sx[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.1)
				out_tmp += int(cur*0.1)
			else:
				out += int(cur*0.1)
		for k in range(9, 10): # a
			s_ny = y + sy[k]
			s_nx = x + sx[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += (cur - out_tmp)
			else:
				out += (cur-out_tmp)
	print(grid)
	for j in range(1,i+1):	# 하
		cur = grid[y][x]
		y = y + dy[0]
		x = x + dx[0]
		out_tmp = 0
		for k in range(2): # 1%
			s_ny = y - sx[k]
			s_nx = x - sy[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.01)
				out_tmp += int(cur*0.01)
			else:
				out += int(cur*0.01)
		for k in range(2, 4): # 2%
			s_ny = y - sx[k]
			s_nx = x - sy[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.02)
				out_tmp += int(cur*0.02)
			else:
				out += int(cur*0.02)
		for k in range(4, 5): # 5%
			s_ny = y - sx[k]
			s_nx = x - sy[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.05)
				out_tmp += int(cur*0.05)
			else:
				out += int(cur*0.05)
		for k in range(5, 7): # 7%
			s_ny = y - sx[k]
			s_nx = x - sy[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.07)
				out_tmp += int(cur*0.07)
			else:
				out += int(cur*0.07)
		for k in range(7, 9): # 10%
			s_ny = y - sx[k]
			s_nx = x - sy[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.1)
				out_tmp += int(cur*0.1)
			else:
				out += int(cur*0.1)
		for k in range(9, 10): # a
			s_ny = y - sx[k]
			s_nx = x - sy[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += (cur - out_tmp)
			else:
				out += (cur-out_tmp)
	for j in range(1,i+2):	# 우
		cur = grid[y][x]
		y = y + dy[0]
		x = x + dx[0]
		out_tmp = 0
		for k in range(2): # 1%
			s_ny = y + sy[k]
			s_nx = x - sx[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.01)
				out_tmp += int(cur*0.01)
			else:
				out += int(cur*0.01)
		for k in range(2, 4): # 2%
			s_ny = y + sy[k]
			s_nx = x - sx[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.02)
				out_tmp += int(cur*0.02)
			else:
				out += int(cur*0.02)
		for k in range(4, 5): # 5%
			s_ny = y + sy[k]
			s_nx = x - sx[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.05)
				out_tmp += int(cur*0.05)
			else:
				out += int(cur*0.05)
		for k in range(5, 7): # 7%
			s_ny = y + sy[k]
			s_nx = x - sx[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.07)
				out_tmp += int(cur*0.07)
			else:
				out += int(cur*0.07)
		for k in range(7, 9): # 10%
			s_ny = y + sy[k]
			s_nx = x - sx[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.1)
				out_tmp += int(cur*0.1)
			else:
				out += int(cur*0.1)
		for k in range(9, 10): # a
			s_ny = y + sy[k]
			s_nx = x - sx[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += (cur - out_tmp)
			else:
				out += (cur-out_tmp)
	for j in range(1,i+2):	# 상
		cur = grid[y][x]
		y = y + dy[0]
		x = x + dx[0]
		out_tmp = 0
		for k in range(2): # 1%
			s_ny = y + sx[k]
			s_nx = x + sy[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.01)
				out_tmp += int(cur*0.01)
			else:
				out += int(cur*0.01)
		for k in range(2, 4): # 2%
			s_ny = y + sx[k]
			s_nx = x + sy[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.02)
				out_tmp += int(cur*0.02)
			else:
				out += int(cur*0.02)
		for k in range(4, 5): # 5%
			s_ny = y + sx[k]
			s_nx = x + sy[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.05)
				out_tmp += int(cur*0.05)
			else:
				out += int(cur*0.05)
		for k in range(5, 7): # 7%
			s_ny = y + sx[k]
			s_nx = x + sy[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.07)
				out_tmp += int(cur*0.07)
			else:
				out += int(cur*0.07)
		for k in range(7, 9): # 10%
			s_ny = y + sx[k]
			s_nx = x + sy[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += int(cur*0.1)
				out_tmp += int(cur*0.1)
			else:
				out += int(cur*0.1)
		for k in range(9, 10): # a
			s_ny = y + sx[k]
			s_nx = x + sy[k]
			if (0 <= s_ny < n) and (0<=s_nx < n):
				grid[s_ny][s_nx] += (cur - out_tmp)
			else:
				out += (cur-out_tmp)
print(grid)


# Difficulty : G3
# 삼성 SW 역량 테스트 기출 문제집 - Simulation + DS
# 자료구조를 어떻게 설계할지만 잘 생각해주면 될 듯
# 문제를 백준으로 옮기다보니 설명이 너무 부족하다.. (ex) 범위 밖으로 나가면 어떻게 처리할지..)