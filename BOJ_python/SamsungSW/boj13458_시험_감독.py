import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split(' ')))
b, c = map(int, input().split(' '))
answer = 0
for i in range(n):
	answer += 1
	a[i] -= b
for i in range(n):
	if a[i] > 0:
		answer += (a[i]//c)
		if a[i]%c > 0:
			answer += 1
print(answer)
# Difficulty : B2
# 삼성 SW 역량 테스트 기출 문제집 - 매우 단순 구현