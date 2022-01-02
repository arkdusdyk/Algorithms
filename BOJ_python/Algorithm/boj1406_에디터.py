import sys
input = sys.stdin.readline
answer = input().rstrip()
n = int(input())
left = []
right = []
for i in range(len(answer)):
	left.append(answer[i])
for _ in range(n):
	cmd = input().split()
	if cmd[0] == "P":
		ch = cmd[1]
		left.append(ch)
	elif cmd[0] == "L":
		if len(left)>0:
			ll = left.pop()
			right.append(ll)
	elif cmd[0] == "D":
		if len(right)>0:
			rr = right.pop()
			left.append(rr)
	elif cmd[0] == "B":
		if len(left) > 0:
			left.pop()
for i in range(len(left)):
	print(left[i], end = "")
for j in range(len(right)-1,-1,-1):
	print(right[j], end = "")

'''
Difficulty : S3
문자열 단순 구현으로 풀이 -> 커서 바꿔가면서 계속해서 문자열 수정 : 시간초과
커서의 이동을 두개의 스택을 사용해서 풀이. (아이디어 신선함)
'''