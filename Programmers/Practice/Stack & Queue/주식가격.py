from collections import deque
def solution(prices):
    answer = []
    q = deque(prices)
    while len(q):
    	cur = q.popleft()
    	t = 0
    	for i in q:
    		t += 1
    		if i < cur:
    			break
    	answer.append(t)
    return answer
prices = [1,2,3,2,3]
print(solution(prices))
# 코딩테스트 연습 : 스택/큐 Level2