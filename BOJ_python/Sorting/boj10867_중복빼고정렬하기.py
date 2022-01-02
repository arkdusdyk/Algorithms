import sys
input = sys.stdin.readline

n = int(input())
arr = list(set(map(int, input().split())))
arr.sort()
for i in range(len(arr)):
	print(arr[i], end = " ")

'''
Difficulty : S5
Sorting + Use Set (중복제거)
'''