import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
	arr.append(list(map(int, input().split())))
chicken = []
apartm = []
for i in range(n):
	for j in range(n):
		if arr[i][j] == 2:
			chicken.append([i,j])
		elif arr[i][j] == 1:
			apartm.append([i,j])
answer = 1e9
for cand in list(combinations(chicken, m)):
	temp = 0
	for apart in apartm:
		min_d = 1e9
		for c in cand:
			min_d = min((abs(c[0] - apart[0]) + abs(c[1] - apart[1])), min_d)
		temp += min_d
	answer = min(temp, answer)
print(answer)

'''
Difficulty : G5
Bruteforce 구현은 어렵지 않았는데 문제 이해하기가 어려웠다.
line22~23을 간단하게 min_d = min(abs(c[0]- apart[0]) + abs(c[1]-apart[1]) for c in cand) 로도 구현 가능.
'''