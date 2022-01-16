import sys
input = sys.stdin.readline

n = int(input())
stair = [0]
dp = [0 for _ in range(n+3)]
for _ in range(n):
	stair.append(int(input()))

dp[1] = stair[1]
if n>=2:
	dp[2] = stair[1] + stair[2]
if n>=3:
	dp[3] = max(stair[1]+stair[3], stair[2]+stair[3])
if n>=4:
	for i in range(4,n+1):
		dp[i] = max(dp[i-2]+stair[i], dp[i-3]+stair[i-1]+stair[i])
print(dp[n])
'''
Difficulty : S3
DP 문제를 풀 때는 점화식을 세우는 것에 더욱 익숙해져야한다..
n=1 : dp[1] = stair[1]
n=2 : dp[2] = stair[1] + stair[2]
n=3 : dp[3] = max(stair[1]+stair[3], stair[2]+stair[3])
n>=4 : dp[n] = max(dp[n-2]+stair[n], dp[n-3]+stair[n-1]+stair[n])

추가로 업데이트하는 값을 더했을떄를 경우로 나눠서 식을 세우는 방향으로 생각해보자..
'''