import sys

n = int(sys.stdin.readline())
dp = [0]*1000
dp[0] = 1
dp[1] = 2
for i in range(2, n):
	dp[i] = (dp[i-1] + dp[i-2])%10007
print(dp[n-1])

'''
Difficulty : S3
DP problem. filling floor (2xn) with two types of tiles (1x2, 2x1)
ai = (ai-1) + (ai-2)
'''