import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int, input().split(' '))
fire = deque()
dy = [-1,-1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(m):
	# r, c, m, s, d
	r, c, m, s, d = map(int, input().split(' '))
	fire.append((r-1,c-1,m,s,d))

while k > 0:
	k -= 1
	grid = [[[] for _ in range(n)] for _ in range(n)]	# m,s,d
	while fire:
		r,c,m,s,d = fire.popleft()
		ny = (r + (s*dy[d]))%n
		nx = (c + (s*dx[d]))%n
		grid[ny][nx].append((m,s,d))
	for i in range(n):
		for j in range(n):
			if grid[i][j]:
				if len(grid[i][j]) > 1:
					cnt = len(grid[i][j])
					m_sum = 0
					s_sum = 0
					odd_cnt = 0
					even_cnt = 0
					for l in range(cnt):
						m,s,d = grid[i][j][l]
						m_sum += m
						s_sum += s
						if d % 2 == 1:
							odd_cnt += 1
						else:
							even_cnt += 1
					new_m = m_sum//5
					new_s = s_sum//cnt
					if new_m == 0:
						continue
					if (odd_cnt == cnt) or (even_cnt == cnt):
						fire.append((i,j,new_m,new_s,0))
						fire.append((i,j,new_m,new_s,2))
						fire.append((i,j,new_m,new_s,4))
						fire.append((i,j,new_m,new_s,6))
					else:
						fire.append((i,j,new_m,new_s,1))
						fire.append((i,j,new_m,new_s,3))
						fire.append((i,j,new_m,new_s,5))
						fire.append((i,j,new_m,new_s,7))
				else:
					m,s,d = grid[i][j][0]
					fire.append((i,j,m,s,d))
answer = 0
for i in range(len(fire)):
	answer += fire[i][2]
print(answer)
# Difficulty : G4
# 삼성 SW 역량 테스트 기출 문제집 - Simulation + DS
# 자료구조를 어떻게 설계할지만 잘 생각해주면 될 듯
# 문제를 백준으로 옮기다보니 설명이 너무 부족하다.. (ex) 범위 밖으로 나가면 어떻게 처리할지..)