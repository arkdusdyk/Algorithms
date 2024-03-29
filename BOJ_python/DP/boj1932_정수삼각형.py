import sys
input = sys.stdin.readline

n = int(input())
dp = []
for i in range(n):
	dp.append(list(map(int, input().split())))

for i in range(1,n):
	for j in range(len(dp[i])):
		if j == 0:
			dp[i][j] = dp[i-1][j] + dp[i][j]
		if 0 < j and j < (len(dp[i])-1):
			dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]
		if j == (len(dp[i])-1):
			dp[i][j] = dp[i-1][j-1] + dp[i][j]
print(max(dp[n-1]))

'''
Difficulty : S1
전 줄 저장 + 현재 줄 확인 max => 갱신 (DP)
'''