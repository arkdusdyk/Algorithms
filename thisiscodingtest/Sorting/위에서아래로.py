n = int(input())
arr = []
for i in range(n):
	arr.append(int(input()))
arr.sort(reverse=True)		#	arr = sorted(arr, reverse = True)
for i in range(n):
	print(arr[i], end = ' ')
'''
N integers (1<=N<=500), time limit 1sec
수열에 속할 수 있는 N이 최대 100,000이기 때문에 Count Sort도 가능할듯
출력을 할 때 line6~7을 다음과 같이 대체 가능
for i in arr:
	print(i, end = ' ')
'''