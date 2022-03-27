import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y,x):
	if check[y][x]:		# DP table 확인해서 첫 방문일때만 dfs
		return check[y][x]
	# 첫 방문
	check[y][x] = 1 			
	for i in range(4):
		ny = y + dy[i]
		nx = x + dx[i]
		if (0<=ny<n) and (0<=nx<n):
			if forest[ny][nx] > forest[y][x]:
				# 이동 후 확인(dfs : 최장경로)+1 vs 현재 위치
				check[y][x] = max(check[y][x], dfs(ny, nx)+1)
	return check[y][x]

n = int(input())
forest = []
for i in range(n):
	forest.append(list(map(int, input().split())))
check = [[0]*n for _ in range(n)]

for i in range(n):
	for j in range(n):
		check[i][j] = dfs(i,j)

answer = 0
for i in range(n):
	answer = max(answer, max(check[i]))
print(answer)

'''
Difficulty : G3
처음에 DFS로 풀었을때는 시간초과가 난다.. 계속해서 같은 부분을 확인해야하기 때문인듯..
-> DFS + DP(Memoization) 을 사용해야함!!
Line 23 은 꼭 기억해두자..
+ 계속해서 Recursion Error -> sys.setrecursionlimit을 해도해도 계속 메모리초과만 뜸..
-> 알고보니 PyPy3에서는 sys.setrecursionlimit 효과 없었다. -> Python3로 제출해보니 성공
** PyPy3, Python3 둘 다 제출해보자.. **
'''