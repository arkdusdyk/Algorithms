import sys
input = sys.stdin.readline

puzzle = []				# 퍼즐 정보 저장
blanks = []				# 빈칸 좌표 저장
visited = [[False]*9 for _ in range(9)]
for _ in range(9):
	puzzle.append(list(map(int, input().split())))
for i in range(9):
	for j in range(9):
		if puzzle[i][j] == 0:
			blanks.append((i,j))

def dfs(puzzle):
	
dfs(puzzle)