import sys
input = sys.stdin.readline

def binary_search(arr, x):
	start = 0
	end = len(arr)-1
	while(start <= end):
		mid = (start + end)//2
		if arr[mid] == x:
			return 1
		elif arr[mid] < x:
			start = mid+1
		else:
			end = mid-1
	return 0

n = int(input())
arr = list(map(int, input().split()))
arr.sort()				# for binary search
n_min = min(arr)
n_max = max(arr)

m = int(input())
check = list(map(int, input().split()))

answer = []
for i in range(m):
	if (check[i] < n_min) or (check[i] > n_max):	# Prune
		answer.append(0)
	else:
		if binary_search(arr, check[i]):
			answer.append(1)
		else:
			answer.append(0)


'''
Difficulty : S4
일단 1) 완전탐색 = 시간초과 날 것 + 2) 전체 수 배열 : 메모리 초과
=> 이진탐색 활용 (from bisect import bisect 도 가능)
'''