#미로탈출
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
	queue = deque()
	queue.append((x,y))
	while queue:
		frx, fry = queue.popleft()
		for i in range(4):
			nx = dx[i]+frx
			ny = dy[i]+fry
			if(nx<0 or nx>=n or ny<0 or ny>=m or maze[nx][ny]==0):
				continue
			if(maze[nx][ny]==1):		#must be 1 : 첫방문일때만 count올려야함
				queue.append((nx,ny))
				maze[nx][ny] = maze[frx][fry]+1
	if(maze[n-1][m-1]!=0):
		print(maze[n-1][m-1])



		

n,m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))
bfs(0,0)
'''
monster=0, empty =1
escape route => minimum routine?
미로 탈출에서 중요한건 갈림길에서 선택..잘못됐을때 다음 선택할 수 있도록 모두 저장해놓기 -> BFS
또, 이전 노드 기준 +1 해가면서 count세는것이 중요
'''