import sys
input = sys.stdin.readline

t = int(input())
for c in range(t):
	n, cmd = input().split()
	n = int(n)
	board = []
	for _ in range(n):
		board.append(list(map(int, input().split())))
	if cmd[0] == 'u':			# up
		for i in range(n):
			st = [board[j][i] for j in range(n) if board[j][i]!=0]
			for j in range(len(st)):
				board[j][i] = st[j]
			for j in range(len(st), n):
				board[j][i] = 0

		for i in range(n):
			for j in range(n-1):
				if board[j][i] == board[j+1][i]:
					board[j][i] = board[j][i]*2
					for k in range(j+1, n-1):
						board[k][i] = board[k+1][i]
					board[n-1][i] = 0
	elif cmd[0] == 'd':			# down
		for i in range(n):
			st = [board[j][i] for j in range(n-1, -1, -1) if board[j][i]!=0]
			for j in range(n-len(st)):
				board[j][i] = 0
			for j in range(n-1, n-len(st)-1, -1):
				board[j][i] = st[n-j-1]

		for i in range(n):
			for j in range(n-1, 0, -1):
				if board[j][i] == board[j-1][i]:
					board[j][i] = board[j][i]*2
					for k in range(j-1, 0, -1):
						board[k][i] = board[k-1][i]
					board[0][i] = 0
	elif cmd[0] == 'l':			# left
		for i in range(n):
			st = [board[i][j] for j in range(n) if board[i][j]!=0]
			for j in range(len(st)):
				board[i][j] = st[j]
			for j in range(len(st), n):
				board[i][j] = 0

		for i in range(n):
			for j in range(n-1):
				if board[i][j] == board[i][j+1]:
					board[i][j] = board[i][j]*2
					for k in range(j+1, n-1):
						board[i][k] = board[i][k+1]
					board[i][n-1] = 0
	elif cmd[0] == 'r':			# right
		for i in range(n):
			st = [board[i][j] for j in range(n-1, -1, -1) if board[i][j]!=0]
			for j in range(n-len(st)):
				board[i][j] = 0
			for j in range(n-1, n-len(st)-1, -1):
				board[i][j] = st[n-j-1]
		for i in range(n):
			for j in range(n-1, 0, -1):
				if board[i][j] == board[i][j-1]:
					board[i][j] = board[i][j]*2
					for k in range(j-1, 0, -1):
						board[i][k] = board[i][k-1]
					board[i][0] = 0

	print("#%d" %(c+1))
	for i in range(n):
		for j in range(n):
			print(board[i][j], end = ' ')
		print()

'''
구현 문제
언제나 구현 문제는 조건을 이해하는게 오래걸린다...
다행히 두번만에 해결.
'''