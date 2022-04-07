import sys
import heapq
input = sys.stdin.readline
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
arr = [list(map(int, input().split(' '))) for _ in range(4)]
fish = [[] for _ in range(4)]
direction = [[] for _ in range(4)]
fish_order = []
for i in range(4):
	for j in range(0, len(arr[0]), 2):
		fish[i].append(arr[i][j])
		heapq.heappush(fish_order, (arr[i][j], i,j))
	for j in range(1, len(arr[0]), 2):
		direction[i].append(arr[i][j])

# Difficulty : G2
# 삼성 SW 역량 테스트 기출 문제집
# 백트래킹 문제 -> DFS로 풀어야겠다..
# 