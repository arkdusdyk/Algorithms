# 뒤집기
import sys
input = sys.stdin.readline

s = input().rstrip()
cnt = 0
for i in range(1, len(s)):	# flip 1s
	if s[i] == '1':
		if s[i-1] == '1':
			continue
		else:
			cnt += 1
cnt1 = 0
for i in range(1, len(s)):	# flip 0s
	if s[i] == '0':
		if s[i-1] == '0':
			if i == 1:
				cnt1 += 1
			continue
		else:
			cnt1 += 1
if cnt1 < cnt:
	print(cnt1)
else:
	print(cnt)
'''
Difficulty : S5
완전탐색
'''