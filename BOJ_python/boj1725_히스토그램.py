import sys
input = sys.stdin.readline

n = int(input())
answer = 0
h = []			# 높이 정보 저장
for i in range(n):
	h.append(int(input()))
st = []				# height stack에 이전 idx 저장
for i in range(n):
	while (len(st)>0) and (h[st[-1]] > h[i]):
		height = h[st[-1]]
		st.pop()
		width = i
		if len(st) > 0:
			width = i-st[-1]-1
		answer = max(answer, width*height)
	st.append(i)

while len(st) > 0:		# 마지막 남은 것들 정리
	height = h[st[-1]]
	st.pop()
	width = n
	if len(st) > 0:
		width = n-st[-1]-1
	answer = max(answer, width*height)
print(answer)

'''
Difficulty : P5
플래 문제 몇년 전에 스터디하면서 풀어본거 다시 풀어봄.
'''