def move(graph, w,x,y,z):
	num_list = []
	w_y, w_x = w[0]-1, w[1]-1
	x_y, x_x = x[0]-1, x[1]-1
	y_y, y_x = y[0]-1, y[1]-1
	z_y, z_x = z[0]-1, z[1]-1
	tmp1 = graph[w_y][y_x]
	num_list.append(tmp1)
	for j in range(y_x, w_x,-1):
		graph[w_y][j] = graph[w_y][j-1]
		num_list.append(graph[w_y][j-1])

	tmp2 = graph[z_y][z_x]
	num_list.append(tmp2)
	for i in range(z_y, y_y+1,-1):
		graph[i][y_x] = graph[i-1][y_x]
		num_list.append(graph[i-1][y_x])
	graph[y_y+1][y_x] = tmp1
	
	tmp1 = graph[x_y][x_x]
	num_list.append(tmp1)
	for j in range(x_x, z_x-1):
		graph[x_y][j] = graph[x_y][j+1]
		num_list.append(graph[x_y][j+1])
	graph[x_y][z_x-1] = tmp2

	for i in range(w_y, x_y-1):
		graph[i][w_x] = graph[i+1][w_x]
		num_list.append(graph[i+1][w_x])
	graph[x_y-1][x_x] = tmp1
	
	return min(num_list)

def solution(rows, columns, queries):
	answer = []
	graph = []
	n = 1
	for i in range(rows):		# 행렬 만들기
		tmp = []
		for j in range(columns):
			tmp.append(n)
			n+=1
		graph.append(tmp)
	for i in range(len(queries)):
		i1, j1, i4, j4 = queries[i]
		i2, j2 = i4, j1
		i3, j3 = i1, j4
		min_num = move(graph, (i1,j1), (i2,j2), (i3,j3), (i4,j4))
		answer.append(min_num)
	return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))

'''
2021 Dev-Matching: 웹 백엔드 개발. Level2 (구현)
완전 구현 문제
'''