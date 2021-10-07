import sys
t = int(sys.stdin.readline())
for i in range(t):
	n,m = map(int, sys.stdin.readline().split())
	a_arr = list(map(int, sys.stdin.readline().split()))
	b_arr = list(map(int, sys.stdin.readline().split()))
	a_arr.sort(reverse = True)
	b_arr.sort()
	cnt=0
	for i in range(n):
		for j in range(m):
			if a_arr[i] > b_arr[j] :
				cnt+=1
			else :
				break
	print(cnt)
'''
Difficulty : S3
Easily Done with Python Sorting..
PyPy3로 채점하면 맞지만 Python3로 채점하면 시간초과가 뜬다..
대신에 PyPy3로 하는데도 메모리가 126~7 mb 정도 되는듯..
'''