import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
	n, m = map(int, input().split())
	arr = list(map(int, input().split()))

	check = arr[m]
	arr.sort()
	