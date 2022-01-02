import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):			# input matrix
	line = list(map(int, input().split()))
	arr.append(line)

x = [i for i in range(1,n+1)]		# make list of 1~n
comb = list(combinations(x, n//2))	# combination of numbers in 1~n


answer = 10000
for i in range(len(comb)//2):
	# team start
	sc1 = 0
	start = comb[i]
	for j in range(n//2):
		mem = start[j]
		for k in start:
			sc1 += arr[mem-1][k-1]

	# team link
	sc2 = 0
	link = comb[-i-1]
	for j in range(n//2):
		mem = link[j]
		for k in link:
			sc2 += arr[mem-1][k-1]
	temp = abs(sc1 - sc2)
	answer = min(answer, temp)
print(answer)
'''
Difficulty : S3
여러가지 방법이 있겠지만 가장 먼저 생각이 든 조합 + bruteforce (n : max 20)로 해결
'''