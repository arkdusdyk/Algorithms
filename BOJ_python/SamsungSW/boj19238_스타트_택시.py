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
def p_bfs(start_y, start_x):    # to passenger
    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append((0, start_y, start_x))
    visited[start_y][start_x] = True
    candid = []
    while q:
        cur, s_y, s_x = q.popleft()
        for i in range(4):
            ny = s_y + dy[i]
            nx = s_x + dx[i]
            if (0<=ny<n) and (0<=nx<n):
                if (visited[ny][nx] == False) and (grid[ny][nx] != 1):
                    if grid[ny][nx] >= 2:
                        candid.append((cur+1, ny,nx))
                    q.append((cur+1, ny,nx))
                    visited[ny][nx] = True
    if len(candid) == 0:
        return False
    candid = sorted(candid)
    return candid[0]

def d_bfs(start_y, start_x, dest):  # to destination
    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append((start_y, start_x, 0))
    visited[start_y][start_x] = True
    while q:
        s_y, s_x, cur = q.popleft()
        for i in range(4):
            ny = s_y + dy[i]
            nx = s_x + dx[i]
            if (0<=ny<n) and (0<=nx<n):
                if visited[ny][nx] == False and grid[ny][nx] != 1:
                    if grid[ny][nx] == dest :
                        return (ny, nx, (cur+1))
                    q.append((ny,nx,cur+1))
                    visited[ny][nx] = True
    return False

cur_y, cur_x = taxi
while True:
    res = p_bfs(cur_y, cur_x)
    if res == False:
        break
    dist_p, next_y, next_x = res
    if dist_p > k:
        break
    passenger = grid[next_y][next_x]
    grid[next_y][next_x] = 0
    k -= dist_p
    #print(k)
    res = d_bfs(next_y, next_x, -passenger)
    #print(next_y, next_x, dist_d)
    if res == False:
        break
    next_y, next_x, dist_d = res
    if  dist_d > k:
        break
    grid[next_y][next_x] = 0
    k += dist_d
    cur_y, cur_x = next_y, next_x
    #print(k)
    m -= 1
    if m == 0:
        answer = k
        break
print(answer)
# Difficulty : G3
# 삼성 SW 역량 테스트 기출 문제집 - Simulation + BFS