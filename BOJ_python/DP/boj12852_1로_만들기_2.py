import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (n+1)
answer = [0] * (n+1)
answer[1] = [1]

for i in range(2, n+1):
	dp[i] = dp[i-1] + 1
	answer[i] = answer[i-1] + [i]
	if i % 3 == 0:
		if (dp[i//3]+1) < dp[i] :
			dp[i] = dp[i//3] + 1
			answer[i] = answer[i//3] + [i]
	if i % 2 == 0:
		if (dp[i//2]+1) < dp[i] :
			dp[i] = dp[i//2] + 1
			answer[i] = answer[i//2] + [i]
print(dp[n])
answer[n].sort(reverse = True)
print(*answer[n])

# Difficulty : S1
# DP 문제 (1로 만들기 문제에서 조금만 변형)