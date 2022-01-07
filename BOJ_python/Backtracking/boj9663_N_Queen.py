import sys
input = sys.stdin.readline

def dfs(x):
	global answer
	if x == n:
		answer += 1
	else:
		# 각 행에 Queen 놓기
		for i in range(n):	# i 를 0부터 n-1까지 유망한 위치 찾기
			row[x] = i
			flag = True
			for j in range(x):
				if (row[x] == row[j]) or (abs(row[x]-row[j])== x-j):	#같은 열, 같은 대각선 아닌 경우 다른 Queen 위치 가능
					flag = False
			if flag == True:
				dfs(x+1)

n = int(input())
row = [0 for _ in range(n)]
answer = 0
dfs(0)
print(answer)

'''
Difficulty : G5
Backtracking 문제. 예전에 아이디어를 보고 감탄한 문제.
-> 다시 풀때 기억을 되짚어보면서 해결한 문제.
Backtracking은 식만 잘 세우면 생각보다도 훨씬 간단하게 해결 가능함
'''