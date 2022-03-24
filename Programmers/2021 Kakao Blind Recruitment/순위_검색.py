from itertools import combinations
from bisect import bisect_left

def solution(info, query):
	answer = []
	info_dict = dict()
	for ii in info:
		i_cond = ii.split(" ")
		score = int(i_cond[-1])
		i_cond = i_cond[:-1]
		for i in range(5):
			for c in combinations(i_cond,i):
				tmp = "".join(c)
				if tmp in info_dict:
					info_dict[tmp].append(score)
				else:
					info_dict[tmp] = [score]

	for i in info_dict:
		info_dict[i].sort()

	for q in query:
		q_cond = q.split(" ")
		q_key = q_cond[:-1]
		q_score = int(q_cond[-1])
		while 'and' in q_key:
			q_key.remove('and')
		while '-' in q_key:
			q_key.remove('-')
		q_key = ''.join(q_key)

		if q_key in info_dict:
			info_scores = info_dict[q_key]
			if info_scores:
				idx = bisect_left(info_scores, q_score)
				answer.append(len(info_scores)-idx)
		else:
			answer.append(0)

	return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))
# 2021 KAKAO BLIND RECRUITMENT Level2
# 효율성 테스트가 있는지 확인안하고 단순하게 풀었는데, 시간 초과
# 정확성 테스트 해결방법이 생각보다 까다롭다.. (사전형으로 hash, 이분탐색 정도는 생각했는데, 모든 조합에 대해 dict key만드는건 예상못함..)