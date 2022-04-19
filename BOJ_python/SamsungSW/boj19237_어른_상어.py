import sys
input = sys.stdin.readline
# n,m,k 입력 (n: 격자, m : 상어, k : 이동 횟수)
n,m,k = map(int, input().split(" "))
grid = []
shark = [[] for _ in range(m)]
dy = [0, 1,-1, 0, 0]
dx = [0, 0, 0, -1, 1]
# 격자 입력
for _ in range(n):
	grid.append(list(map(int, input().split(" "))))
# 각 상어 보고 있는 방향 입력 (1,2,3,4 : 위 아래 왼 오)
direction = list(map(int, input().split(" ")))
# 4줄씩 각 상어 방향 우선순위
for i in range(n):
	for j in range(4):

# 상어 위치 저장 (숫자 순서)
for i in range(n):
	for j in range(n):
		if grid[i][j] > 0:
			shark[grid[i][j]-1].append((i,j))
print(shark)



# Difficulty : G3
# 삼성 SW 역량 테스트 기출 문제집