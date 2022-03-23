def solution(N, stages):
	answer = []
	player = len(stages)
	fail = dict()
	for i in range(1, N+1):
		if player > 0:
			fail[i] = (stages.count(i) / player)
			player -= stages.count(i)
		else:
			fail[i] = 0

	answer = sorted(fail, key = lambda i : fail[i], reverse = True)
	return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))

'''
2019 KAKAO BLIND RECRUITMENT Level1
sorted lambda만 잘 쓰면 쉽게 해결 가능!
-> 하지만 시간이 빡빡하니까 dict 한개로 처리
'''