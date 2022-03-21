from collections import deque
def bfs(graph, y,x):		
	visited = [[False]*5 for _ in range(5)]
	dist = [[0]*5 for _ in range(5)]

	dy = [-1, 1, 0, 0]
	dx = [0,0, -1, 1]

	q = deque()
	q.append((y,x))
	visited[y][x] = True
	while q:
		cur_y, cur_x = q.popleft()
		for k in range(4):
			ny = cur_y + dy[k]
			nx = cur_x + dx[k]
			if (0<=nx<5) and (0<=ny<5):
				if visited[ny][nx] == False:
					if graph[ny][nx] == 'O':
						q.append((ny,nx))
						visited[ny][nx] = True
						dist[ny][nx] = dist[cur_y][cur_x] + 1

					if graph[ny][nx] == 'P':	# 다른 응시자
						if dist[cur_y][cur_x] <= 1:		#현재 2이상이면 모두 거리두기 지킨 것
							return False
	return True

def solution(places):
	answer = []
	for place in places:
		tester = []
		for i in range(5):
			for j in range(5):
				if place[i][j] == 'P':		# 응시자 좌표 저장
					tester.append((i,j))
		
		flag = True
		for t in tester:
			t_y, t_x = t
			possible = bfs(place, t_y, t_x)
			if possible == False:
				flag = False
				break
		if flag == False:			# 하나라도 거리두기 X -> 실패
			answer.append(0)
		else:
			answer.append(1)
	return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))

# 2021 KAKAO Internship Level2
# BFS로 해결한 문제
# 생각해보니 확인해야하는 범위가 최대 2칸이니깐 if문 중첩으로 X나오면 확인하는 식으로 짜는거도 가능할듯..