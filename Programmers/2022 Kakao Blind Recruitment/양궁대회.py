from itertools import combinations_with_replacement
def solution(n, info):
	answer = []
	max_score = 0
	hit = combinations_with_replacement([i for i in range(11)], n)
	for point in hit:
		p = list(point)
		cur = [0 for _ in range(11)]	# 맞은 점수 조합으로 info 와 같이 화살갯수 저장.
		for i in range(n):
			cur[p[i]] += 1
		# cur 은 [0점, 1점, 2점, ... 10점] 순으로 저장되어있음 (info역순)
		ryan = 0
		apeach = 0
		for i in range(11):			# 화살 갯수 비교 -> 점수
			if cur[i] > info[10-i]:
				ryan += i
			else:
				if info[10-i] > 0:
					apeach += i
		if ryan > apeach:
			if ryan - apeach > max_score:
				max_score = (ryan-apeach)
			answer.append((ryan-apeach,cur))
	if len(answer) == 0:
		return [-1]
	answer.sort(reverse = True)		# 지금 cur (info의 역순)..역순 정렬로 하면 가장 앞에 있는 것이 동최고점의 answer
	for ans in answer:
		if ans[0] == max_score:
			return ans[1][::-1]
n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]
print(solution(n, info))

'''
2022 KAKAO Blind Recruitment Level2
이번에도 결국 조합으로 풀어서 아쉬움도 있다.
분명 DFS/BFS로도 해결이 가능할 것 같은데... 숙련도 부족ㅜ
'''