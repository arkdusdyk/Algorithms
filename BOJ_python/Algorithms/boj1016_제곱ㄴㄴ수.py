import sys
input = sys.stdin.readline

def solution(a, b):
	num = [False for _ in range(b-a+1)]
	til = int(b**0.5)
	answer = b-a+1
	for i in range(2, til+1):
		sq = i*i
		j = 0
		if a % sq == 0:
			j = a//sq
		else:
			j = a//sq + 1
		while sq * j <= b:
			if sq*j < a :
				j+=1
				continue
			if num[sq*j - a] == False:
				num[sq*j - a] = True
				answer -= 1
			j+=1
	print(answer)

min_x, max_x = map(int, input().split())
solution(min_x, max_x)

'''
Difficulty : G1
메모리는 초과될 것이 분명했고, 시간 초과도 신경써야하는게 분명했기에
에라토스테네스의 체를 활용한다는 아이디어가 바로 떠올랐다.

분명히 다양한 반례 처리를 했는데 생겼던 문제 : line 15의 범위를 a<=sq*j<=b로 처리하고 line 16~17를 생각하지 않았다.
=> 여러 번 틀린 이유 (해당 문제 수정 후에도 1000000000000 1000001000000 에 대해서 시간이 너무 오래걸림)
=> j의 시작점을 1부터 확인하는 대신 line 10 ~ line 14까지를 추가해서 시간 초과를 확실하게 잡을 수 있었다!!
'''