from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
	queue = deque()
	queue.append((x,y))
	visited[x][y] = 1
	tmp = 1
	while queue:
		x,y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx <= -1 or ny <= -1 or nx>=n or ny>=n:
				continue
			else:
				if arr[nx][ny] == 1 and visited[nx][ny] == 0:
					tmp += 1
					queue.append((nx,ny))
					visited[nx][ny] = 1
	return tmp

n = int(input())
arr = []
ans = []
visited = [[0]*n for _ in range(n)]
for i in range(n):
	arr.append(list(map(int, input().strip())))

for i in range(n):
	for j in range(n):
		if arr[i][j] == 1 and visited[i][j] == 0:
			res = bfs(i,j)
			ans.append(res)
ans.sort()
m = len(ans)
print(m)
for i in range(m):
	print(ans[i])

'''
S1
DFS/BFS
input 받을때 왜 split으로 받으면 0이 생략되나..strip vs split..
'''

# 2021/01/10 (Retry with DFS)
import sys
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n = int(input())
arr = []
for i in range(n):
	arr.append(list(map(int, input().strip())))
visited = [[False]*n for _ in range(n)]
cnt = 0
answer = []

def dfs(i,j, visited):
	global x
	visited[i][j] = True
	x += 1
	for k in range(4):
		nx = i + dx[k]
		ny = j + dy[k]
		if (0<=nx<n) and (0<=ny<n):
			if visited[nx][ny] == False and arr[nx][ny] == 1:
				dfs(nx, ny, visited)

for i in range(n):
	for j in range(n):
		x = 0
		if visited[i][j] == False and arr[i][j] == 1:
			dfs(i,j, visited)
			cnt += 1
			answer.append(x)
print(cnt)
answer.sort()
for ans in answer:
	print(ans)
'''
Difficulty : S1
DFS. (Traverse each Connected Component)
'''