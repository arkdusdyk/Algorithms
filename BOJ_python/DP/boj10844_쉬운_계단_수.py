import sys
input = sys.stdin.readline
n = int(input())
dp = [[0 for i in range(10)] for j in range(101)]
# j : 자리수
# 각 자리수에서 맨 뒤에 올 수 있는 숫자 갯수
for i in range(1, 10):
	dp[1][i] = 1
for i in range(2, n+1):
	for j in range(10):
		if j == 0:
			dp[i][j] = dp[i-1][1]
		elif j == 9:
			dp[i][j] = dp[i-1][8]
		else:
			dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n])%1000000000)

'''
Difficulty : S1
DP 문제... (생각보다 어려웠다..)
각 자리수에서 맨 뒤에 올 수 있는 숫자 갯수 (0~9)
즉 전 자리수 기준 (대각선 두 값.)
'''