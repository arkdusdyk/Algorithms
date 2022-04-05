def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
    	h = citations[i]
    	if h >= (len(citations)-i):
    		answer = len(citations)-i
    		break
    return answer

citations = [3, 0, 6, 1, 5]	
print(solution(citations))

# 코딩테스트 연습 : 정렬 Level2