import sys
from collections import deque
input = sys.stdin.readline

n, q = map(int, input().split(' '))
ice_len = 2**n
ice = []
for i in range(ice_len):
	ice.append(list(map(int, input().split(' '))))
l_list = list(map(int, input().split(' ')))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for idx in range(q):
	# rotate
	l = 2**(l_list[idx])
	new_ice = [[0]*(ice_len) for _ in range(ice_len)]
	for i in range(0,ice_len,l):
		for j in range(0,ice_len,l):
			for k in range(l):
				for m in range(l):
					new_ice[i+m][(j+l)-1-(k)] = ice[i+k][j+m]
			for k in range(l):
				for m in range(l):
					ice[i+k][j+m] = new_ice[i+k][j+m]
	# melt
	melt = []
	for i in range(ice_len):
		for j in range(ice_len):
			if ice[i][j] > 0:
				cnt = 0
				for k in range(4):
					ny = i + dy[k]
					nx = j + dx[k]
					if (0<=ny<ice_len) and (0<=nx<ice_len):
						if ice[ny][nx] >=1 :
							cnt += 1
				if cnt < 3:
					melt.append((i,j))
	for m in melt:
		y,x = m
		ice[y][x] -= 1

# 남아있는 얼음 합 + BFS로 가장 큰 덩어리 찾기
left = 0
visited = [[False] * ice_len for _ in range(ice_len)]
max_connected = 0
for i in range(ice_len):
	for j in range(ice_len):
		connected = 0
		if (visited[i][j] == False) and (ice[i][j] > 0):
			q = deque()
			q.append((i,j))
			visited[i][j] = True
			while q:
				y,x = q.popleft()
				left += ice[y][x]
				connected += 1
				for k in range(4):
					ny = y + dy[k]
					nx = x + dx[k]
					if (0<=nx<ice_len) and (0<=ny<ice_len):
						if visited[ny][nx] == False and ice[ny][nx] > 0:
							q.append((ny,nx))
							visited[ny][nx] = True
			max_connected = max(connected, max_connected)
print(left)
print(max_connected)

# Difficulty : G4
# 삼성 SW 역량 테스트 기출 문제집 - Simulation + BFS
# 90도 회전하는것의 indexing이 오래걸렸다.
# 분명 잘 짯는데 총합, 덩어리 문제가 생김. (아무래도 설명이 덜되어있다보니 난감..)
# 뭐가 문제였을까했는데 얼음을 녹일때는 동시에 모든 melting point들 녹여야함. (원래는 녹이면서 진행했음)