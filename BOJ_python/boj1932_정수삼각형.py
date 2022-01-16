import sys
input = sys.stdin.readline

n = int(input())
dp = [[] for _ in range(n)]
for i in range(n):
	line = list(map(int, input().split()))
	dp[i] = line

for i in range(1,n):
	for j in range(1, i+2):
		dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + dp[i][j]
'''
Difficulty : S1
dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + dp[i][j]
'''