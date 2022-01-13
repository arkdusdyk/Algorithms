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

def dfs(k):
	if k == len(blanks):
		for i in range(9):
			for j in range(9):
				print(puzzle[i][j], end = " ")
			print()
		return

	# check kth blank
	ky, kx = blanks[k][0], blanks[k][1]

	chk = [i for i in range(1,10)]
	for i in range(9):
		if puzzle[ky][i] in chk:	#check same row
			chk.remove(puzzle[ky][i])
		if puzzle[i][kx] in chk:	#check same col
			chk.remove(puzzle[i][kx])
	for i in range(ky,(ky//3 +1)*3):	#check 3x3
		for j in range(kx, (kx//3+1)*3):
			if puzzle[i][j] in chk:
				chk.remove(puzzle[i][j])
	for checker in chk:
		puzzle[ky][kx] = checker
		dfs(k+1)
		puzzle[ky][kx] = 0

dfs(0)