import sys
from collections import deque
input = sys.stdin.readline
n, m, k = map(int, input().split(' '))
grid = [[] for i in range(n)]
for i in range(n):
    grid[i] = list(map(int, input().split(' ')))
taxi_y, taxi_x = map(int, input().split(' '))
taxi = (taxi_y-1, taxi_x-1)
person = 2
for _ in range(m):
    s_y, s_x, d_y, d_x = map(int, input().split(' '))
    grid[s_y-1][s_x-1] = person
    grid[d_y-1][d_x-1] = -person
    person += 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
answer = -1
def bfs(start):
    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append(start)
    while q:
        s_y, s_x = q.popleft()
        

# Difficulty : G3
# 삼성 SW 역량 테스트 기출 문제집 - Simulation + BFS