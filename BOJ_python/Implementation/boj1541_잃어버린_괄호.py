import sys
input = sys.stdin.readline
equ = input().rstrip()
equ_split = equ.split('-')
answer = []
for i in range(len(equ_split)):
	num_split = equ_split[i].split('+')
	total = 0
	for num in num_split:
		total += int(num)
	answer.append(total)
res = answer[0]
for i in range(1, len(answer)):
	res -= answer[i]
print(res)

'''
Difficulty : S2
단순 구현. 연산자 다양해지면 문제가 훨씬 어려워질듯.
'''