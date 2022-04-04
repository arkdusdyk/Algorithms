import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville)>1:
    	if scoville[0] >= K:
    		break
    	s1 = heapq.heappop(scoville)
    	s2 = heapq.heappop(scoville)
    	mix = s1 + (s2*2)
    	answer += 1
    	heapq.heappush(scoville, mix)
    if scoville[0] < K:
    	answer = -1
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))
# 코딩테스트 연습 : Heap Level2
# 처음에는 스택으로도 풀 수 있을 것 같았는데, 섞었을때 스코빌 지수값이 항상 최상위에 오는 것이 아님
# 힙을 통해 관리가 필요 -> Heapq 사용
# heapq.heappush(heap, X)
# heapq.heappop(heap)
# heap[0] : heap root
# heapq.heapify(heap)