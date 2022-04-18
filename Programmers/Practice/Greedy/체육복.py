def solution(n, lost, reserve):
    answer = 0
    stud = [True] * (n+1)

    res = set(reserve) - set(lost)
    loss = set(lost) - set(reserve)
    for l in loss:
    	stud[l] = False
    for r in res:
    	if stud[r] == False:		# 여분 + 도난
    		stud[r] = True
    	elif stud[r-1] == False:
    		stud[r-1] = True
    	elif (r < n) and stud[r+1] == False:
    		stud[r+1] = True
    answer = stud[1:].count(True)
    return answer

n = 7
lost = [2,3,4]
reserve = [1,2,3,6]
print(solution(n, lost, reserve))
# 코딩테스트 연습 : Greedy Level 1
# 사실 문제 자체는 매우 쉬웠는데 짜잘한 부분에서 이해하기 어려운 부분이 있었음