import sys
n,m = map(int, sys.stdin.readline().split())
coin = []
for i in range(n):
	coin.append(int(sys.stdin.readline().rstrip()))
MAX = 10001
dp = [MAX]*(m+1)
dp[0] = 0
for i in range(n):
	for j in range(coin[i], m+1):
		if dp[j-coin[i]] != MAX:
			dp[j] = min(dp[j-coin[i]]+1, dp[j])
if dp[m] == MAX:
	print(-1)
else:
	print(dp[m])
'''
DP Bottom Up
어떻게 할지 많이 고민했던 문제.
시간을 고려하지 않고 n^2이 되도 상관 없을거라고는 생각도 못했다.
reccurence relation : Ak = min(Ak, A(k-coin(0~n))+1)
Bottom Up으로 채워나가면서 현재 값에서 (coin모든 경우)를 뺀 값이 MAX 값이 아니라면,
dp[j-coin[i]]에는 이미 어떠한 구성 갯수에 대한 값이 채워져있다.
점화식 부분을 잘 이해해보자.
'''