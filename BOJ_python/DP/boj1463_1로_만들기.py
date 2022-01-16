import sys
input = sys.stdin.readline
dp = [0]*1000001

x = int(input())
for i in range(2,x+1):
	dp[i] = dp[i-1]+1
	if i%3==0:
		dp[i] = min(dp[i], dp[i//3]+1)
	if i%2==0:
		dp[i] = min(dp[i], dp[i//2]+1)
print(dp[x])

'''
Difficulty : S3
Basic Dynamic Problem
Reccurrence Relation: min(ai-1, ai//2, ai//3) +1
Bottum Up DP

Tried: if, elif.-> Realized if input is multiple of 6, need to check both
'''