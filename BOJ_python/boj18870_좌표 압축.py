import sys
from bisect import bisect
n = int(sys.stdin.readline())
x_arr = list(map(int, sys.stdin.readline().split()))
y_arr = set(x_arr)		#remove duplicates
y_arr = sorted(list(y_arr))
for i in x_arr:
	print(bisect(y_arr, i, lo=0, hi=len(y_arr))-1, end = ' ')

'''
Difficulty : S2
Sorting 문제. Set로 변환하고 다시 list로 변환하여 중복 제거함.
Used Bisect (Binary Search)
'''