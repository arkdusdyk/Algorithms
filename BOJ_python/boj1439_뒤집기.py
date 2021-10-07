# 뒤집기
import sys
input = sys.stdin.readline

s = input().rstrip()
cnt_1 = 0
cnt_0 = 0
flag = True
for i in range(len(s)-1):
	if s[i] != s[i+1]:
		if flag:
			cnt_1 += 1
			flag = False
		else:
			cnt_0 += 1
			flag = True
if flag:	# last check
	cnt_1 += 1
else:
	cnt_0 += 1

if cnt_1 < cnt_0:
	print(cnt_1)
else:
	print(cnt_0)
'''
Difficulty : S5
완전탐색
'''