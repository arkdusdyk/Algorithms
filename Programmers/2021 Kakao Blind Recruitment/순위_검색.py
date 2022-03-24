def solution(info, query):
	answer = []
	for q in query:
		q_cond = q.split(" and ")
		q_cond_last = q_cond[-1].split(" ")
		q_cond[-1] = q_cond_last[0]
		score = int(q_cond_last[1])

		check = [True]*len(info)
		for i in range(len(info)):
			for j in range(len(q_cond)):
				if (q_cond[j] != "-") and (q_cond[j] not in info[i]):
					check[i] = False
		cnt = 0
		for i in range(len(check)):
			if check[i] == True:
				if int(info[i].split(" ")[-1]) >= score:
					cnt += 1
		answer.append(cnt)
	return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))
# 2021 KAKAO BLIND RECRUITMENT Level2
# 효율성 테스트가 있는지 확인안하고 단순하게 풀었는데, 시간 초과ㅋㅋㅋ
# 