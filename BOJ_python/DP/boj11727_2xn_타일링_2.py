import sys
n = int(sys.stdin.readline())
dp = [0]*1000
dp[0] = 1
dp[1] = 3
for i in range(2, n):
	dp[i] = (dp[i-1] + 2*(dp[i-2]))%10007
print(dp[n-1])

'''
Difficulty : S3
DP problem. filling floor (2xn) with three types of tiles (1x2, 2x1, 2x2)
ai = (ai-1) + (ai-2)*2 (two possible ways to add: one 2x2 or two 1x2) - Bottom Up
'''