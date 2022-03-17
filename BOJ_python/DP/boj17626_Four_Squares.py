import sys
input = sys.stdin.readline
n = int(input())
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
	ans = 50000
	for j in range(1, i+1) :
		if (j**2) > i:
			break
		else:
			ans = min(ans, dp[i-(j**2)])
	dp[i] = ans + 1
print(dp[n])

'''
Difficulty : S4
DP 문제... 처음에는 단순 Greedy 구현으로 쉽게 해결해보려고 했는데 결국 DP 문제였다.
'''