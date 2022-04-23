import sys
input = sys.stdin.readline
n = int(input())
t, p = [], []
for _ in range(n):
	t_in, p_in = map(int, input().split(' '))
	t.append(t_in)
	p.append(p_in)
max_arr = [0] * (n+1)
for i in range(n-1, -1, -1):
	if i + t[i] <= n:
		max_tmp = max_arr[i+t[i]] + p[i]
		max_arr[i] = max(max_arr[i+1], max_tmp)
	else:
		max_arr[i] = max_arr[i+1]
print(max_arr[0])

# Difficulty : S3
# 삼성 SW 역량 테스트 기출 문제집 - 누적합 활용