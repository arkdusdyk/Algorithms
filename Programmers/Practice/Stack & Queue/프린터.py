from collections import deque
def solution(priorities, location):
	answer = 0
	q = deque()
	for i in range(len(priorities)):
		q.append((priorities[i],i))
	
	priorities.sort()
	n = len(priorities)-1			# max 확인용
	while q:
		p, loc = q.popleft()
		if p >= priorities[n]:		# 출력
			n -=1
			answer += 1
			if loc == location :
				break
		else:						# back to queue
			q.append((p,loc))
	return answer

priorities = [1,1,9,1,1,1]
location = 0
print(solution(priorities, location))

# 코딩테스트 연습 : 스택/큐 Level2
# 자료구조만 잘 선택하고 차근차근 구현