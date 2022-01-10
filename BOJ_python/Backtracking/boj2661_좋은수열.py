import sys
input = sys.stdin.readline
answer = ''
num = ['1','2','3']
n = int(input())

def check(checker):
	#print("checking : ", checker)
	for i in range(1, len(checker)+1):
		a = checker[len(checker)-i-i : len(checker)-i]
		b = checker[len(checker)-i:]
		#print("a: ", a, "b:", b)
		if a == b:
			return False
	return True

def solution(answer):
	if len(answer) == n:
		print(answer)
		exit()
	for i in range(3):
		if check(answer+num[i]):
			solution(answer+num[i])

solution(answer)

'''
Difficulty : G4
Backtracking 문제
재귀에서 나갈때 지금까지 global flag 를 활용했지만 return대신 exit()으로 나가도 된다.
'''