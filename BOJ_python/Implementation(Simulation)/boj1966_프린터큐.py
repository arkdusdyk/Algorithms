import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
	n, m = map(int, input().split())
	arr = list(map(int, input().split()))
	print_q = deque()
	answer = 0
	for i in range(len(arr)):
		print_q.append((arr[i],i))
	while (len(print_q) > 0):
		cur = print_q[0][0]
		flag = False
		for i in range(1, len(print_q)):
			if print_q[i][0] > cur:
				flag = True
				break
		if flag == True:		# bigger priority exist later
			print_q.append(print_q.popleft())
		else:
			(x,y) = print_q.popleft()
			answer += 1
			if y == m:
				break
	print(answer)


'''
Difficulty : S3
사실상 그냥 구현
'''