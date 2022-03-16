from collections import deque

def solution(cacheSize, cities):
	answer = 0

	# 마지막에 보니 cacheSize = 0 도 따로 설정해야함
	if cacheSize == 0:
		return 5*len(cities)

	q = deque()
	for c in cities:
		c = c.lower()		# 대소문자 구분 X
		if c in q:			# Cache Hit
			#print("Hit")
			q.remove(c)
			answer += 1
		else:				# Cache Miss
			#print("MISS")
			if len(q) == cacheSize:
				q.popleft()			# LRU
			answer += 5
		q.append(c)
	return answer

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))
# 2018 Kakao Blind Recruitment Level2
# 큐 구조로 짜니 쉽게 구현 가능했다.