import sys
input = sys.stdin.readline

puzzle = []				# 퍼즐 정보 저장
blanks = []				# 빈칸 좌표 저장
for _ in range(9):	# puzzle input
	puzzle.append(list(map(int, input().split())))
for i in range(9):	# blanks input
	for j in range(9):
		if puzzle[i][j] == 0:
			blanks.append((i,j))

def chk_horizontal(y, chk):
	for i in range(9):
		if chk == puzzle[y][i]:
			return False
	return True

def chk_vertical(x, chk):
	for i in range(9):
		if chk == puzzle[i][x]:
			return False
	return True

def chk_three(x,y, chk):
	nx = x//3
	ny = y//3
	for i in range(3):
		for j in range(3):
			if chk == puzzle[3*ny+i][3*nx+j]:
				return False
	return True

def dfs(k):
	if k == len(blanks):
		for row in puzzle:
			for elem in row:
				print(elem, end = " ")
			print()
		sys.exit()

	# kth blank
	ky = blanks[k][0]
	kx = blanks[k][1]

	for i in range(1, 10):		# check candidates
		if chk_horizontal(ky, i) and chk_vertical(kx, i) and chk_three(kx,ky,i):
			puzzle[ky][kx] = i
			dfs(k+1)
			puzzle[ky][kx] = 0

dfs(0)