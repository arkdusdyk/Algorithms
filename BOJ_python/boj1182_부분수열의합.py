import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
for i in range(n):
	partial_s = 0
	for j in range(i,n):
		partial_s += arr[j]
		if partial_s == s:
			answer += 1

print(answer)
'''
Difficulty : S2
'''