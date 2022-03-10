import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
arr = list(map(int, input().split()))

def solution(arr):
	diff = []
	if len(arr) == 1:
		return 0
	for i in range(1, len(arr)):
		diff.append(arr[i] - arr[i-1])
	diff.sort()
	return sum(diff[:len(diff)-k+1])

arr.sort()
print(solution(arr))

'''
Difficulty : G5
문제 예시가 없어서 이해가 잘 안 됐다.
처음에는 이분탐색을 활용해볼까 했는데, 차이 확인해보니 쉽게 방법 찾은.
'''