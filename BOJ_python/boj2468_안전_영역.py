import sys
from collections import deque
input = sys.stdin.readline


dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y, h):
	queue = deque()
	queue.append((x,y))
	visited[x][y] = 1

	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x+ dx[i]
			ny = y+ dy[i]
			if nx <= -1 or nx>= n or ny<=-1 or ny>=n:
				continue
			else:
				if arr[nx][ny] >= h and visited[nx][ny] == 0:
					visited[nx][ny] = 1
					queue.append((nx,ny))

n = int(input())
arr = []
high = 101
for i in range(n):
	input_list = list(map(int, input().split()))
	arr.append(input_list)
	temp = max(input_list)
	if high < temp:
		high = temp


ans = 0
for h in range(1, high+1):
	visited = [[0]*n for _ in range(n)]
	temp = 0
	for i in range(n):
		for j in range(n):
			if arr[i][j] >= h and visited[i][j] == 0:
				bfs(i,j,h)
				temp += 1
		if temp > ans:
			ans = temp

print(ans)

'''
S1
DFS/BFS 문제
DFS로 풀었을때 recursion depth 초과 문제가 계속 떠서 BFS 로 해결함.
'''