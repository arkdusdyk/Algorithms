import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t+1):
	answer = 0
	a,b = map(int, input().split())
	if a > b:		#smaller as a
		a, b = b,a

	print("#%d %d" %(i, answer))