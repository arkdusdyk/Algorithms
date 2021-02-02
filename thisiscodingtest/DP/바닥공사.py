import sys
dp = [0]*1000
def tilefunc(x):
	dp[0] = 1
	dp[1] = 3
	for i in range(2, x):
		dp[i] = (dp[i-1] + dp[i-2]*2)%796796
	return dp[x-1]

n = int(sys.stdin.readline())
print(tilefunc(n))

'''
DP : Bottom Up Style
1x2, 2x1, 2x2
same with boj11727
-> check : https://github.com/arkdusdyk/BOJ_python/blob/main/boj11727_2xn_%ED%83%80%EC%9D%BC%EB%A7%81_2.py
'''