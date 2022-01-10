import sys
from collections import deque
input = sys.stdin.readline
maze =[]
n,m = map(int, input().split())
for i in range(n):
	maze.append(list(map(int, input().strip())))
visited = [[False]*m for _ in range(n)]

def bfs(x,y):
	q = deque()
	q.append((x,y))
	visited[x][y] = True
	dx = [-1,1,0,0]
	dy = [0,0,-1,1]
	while q:
		fr = q.popleft()
		tmp = maze[fr[0]][fr[1]]
		for k in range(4):
			nx = fr[1] + dx[k]
			ny = fr[0] + dy[k]
			if 0<=nx<m and 0<=ny<n:
				if visited[ny][nx] == False and maze[ny][nx] == 1:
					visited[ny][nx] = True
					maze[ny][nx] = tmp+1
					q.append((ny, nx))
	print(maze[n-1][m-1])

bfs(0,0)

'''
Difficulty : S1
처음에 DFS로 시도해보다가 BFS로 해결. (이런 최소값 구할 때 훨씬 편하다)
count를 어떻게 저장할까 전역변수도 써보고 했는데 이렇게 maze안의 값을 바꿔주는 방법도 좋은 것 같다.
'''