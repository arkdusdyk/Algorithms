import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

# 앞에서부터 연속합 (최대 연속)
dp = [0]*n
dp[0] = arr[0]
for i in range(1,n):
	dp[i] = max(dp[i-1]+arr[i], arr[i])

# 뒤에서부터 연속합
rev = [0]*n
rev[n-1] = arr[n-1]
for i in range(n-2, -1, -1):
	rev[i] = max(rev[i+1]+arr[i], arr[i])

# i번째 값 하나 제거한 연속합
ex_one = [0]*n
ex_one[0] = arr[0]
ex_one[n-1] = arr[n-1]
for i in range(1,n-1):
	ex_one[i] = dp[i-1] + rev[i+1]

answer = max(max(dp), max(ex_one))
print(answer)

'''
Difficulty : G5
DP 문제. (3번 아이디어는 알아두면 좋을 것 같다.)
1. 일반적으로 앞에서부터 연속합 구한 것. (dp)
2. 같은 방식으로 뒤에서부터 연속합 구한다. (rev)
3. i 번째 값 하나 제거한 연속합 : dp[i-1] + rev[i-1]
4. 1과 3 최대값 비교
'''