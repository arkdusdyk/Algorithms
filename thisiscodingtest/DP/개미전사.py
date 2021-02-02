import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0]*100
for i in range(0,2):
	dp[i] = arr[i]
for i in range(2, n):
	dp[i] = max(dp[i-1], dp[i-2]+arr[i])
print(dp[n-1])

'''
DP : Bottom Up Style
Reccurence Relation : ai = max(ai-1, ai-2 + k)
'''