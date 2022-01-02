from collections import deque
import sys
dx = [-1,1,0,0]
dy = [0,0,-1,1]
input = sys.stdin.readline			#minimize input time
r,c = map(int, input().split())
forest = []
for i in range(r):
	forest.append(list(input()))
visited = [[0]*c for i in range(r)]
w_queue = deque()
s_queue = deque()
for i in range(r):		#search initial location of porcupine and water
	for j in range(c):
		if(forest[i][j]=='S'):
			forest[i][j] = 0			#initial location set to 0 -> add up count
			s_queue.append((i,j))
			visited[i][j] = 1
		if(forest[i][j]=='*'):
			w_queue.append((i,j))
		if(forest[i][j]=='D'):			#destination location saved
			d_x = i
			d_y = j
while(w_queue or s_queue):
	s = []
	w = []
	while(s_queue):				#s(porcupine) BFS
		frsx, frsy = s_queue.popleft()
		if forest[frsx][frsy] != '*':
			for i in range(4):
				nx = frsx + dx[i]
				ny = frsy + dy[i]
				if(nx<0 or ny<0 or nx>=r or ny>=c or forest[nx][ny]=='X' or forest[nx][ny]=='*'):
					continue
				if(visited[nx][ny]==0):		#can move
					s.append((nx,ny))
					visited[nx][ny] = 1
					forest[nx][ny] = forest[frsx][frsy] +1
	for i in s:				#다음 단계에서 진행할 것들 s_queue에 저장
		s_queue.append(i)
	while(w_queue):				#water BFS
		frwx, frwy = w_queue.popleft()
		for i in range(4):
			nx = frwx + dx[i]
			ny = frwy + dy[i]
			if(nx<0 or ny<0 or nx>=r or ny>=c or (d_x==nx and d_y==ny)):
				continue
			if(forest[nx][ny]!='*' and forest[nx][ny]!='X'):
				forest[nx][ny] = '*'				#물 침범 -> override.
				w.append((nx,ny))
	for i in w:					#다음 단계에서 진행할 것들 w_queue에 저장
		w_queue.append(i)
if forest[d_x][d_y] =='D':		#도착못함
	print("KAKTUS")
else:							#도착하는데 걸린시간
	print(forest[d_x][d_y])
'''
Difficulty : G5
(BFS)
처음 접근에 비해 은근히 까다로웠던 문제
BFS인것을 생각하는건 바로 했지만 처음에 생각은 물부터 BFS 후, 고슴도치 움직임 BFS
추가 고려해야할것 두가지:
	1. 이전 시간(단계/level)에서 큐에 추가된 좌표들은 모두 확인해야하는데 물 한번 고슴도치 한번 BFS를 적용시키면서 각 level 별로 진행해야함.
		-> 처음에는 물먼저 BFS, 레벨별로 진행하기 위해 추가 반복문을 또 돌림 -> 시간초과
		-> 고슴도치를 먼저 움직여놓고 물로 override하는 형식. 또 큐에 추가하는 단계만 큐 반복문 밖으로 빼면 매 분마다 진행가능(tree의 level별로 모두 진행하는것이 가능)
	2. 도착지에 도착하였는가?
		-> forest에 각 단계별로 고슴도치가 도착한 시간을 저장하는 형식으로, water가 침범한 부분이라면 override됨
		-> 최종 도착지 위치를 먼저 저장해놓고 마지막에 해당 forest위치에 있는 값이 여전히 'D'면 도착 못한것. 만약 고슴도치가 도착했다면 숫자(도착시간)

아직 해결되지 않은것:
	1. PyPy3가 Python3에 비해 좋다는 것으로 알고있는데 대신 메모리를 너무 먹는다.. 거의 커트라인에 걸쳐서 통과한 느낌