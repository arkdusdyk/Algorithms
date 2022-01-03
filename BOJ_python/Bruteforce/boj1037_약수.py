import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
idx = 0
if len(arr)%2 == 0:
	idx1 = len(arr)//2
	idx2 = idx1 -1
	print(arr[idx1]*arr[idx2])
else:
	idx1 = len(arr)//2
	print(arr[idx1]*arr[idx1])
'''
Difficulty : S5
단순 구현
'''