import heapq
def solution(operations):
    answer = []
    max_heap = []
    min_heap = []
    for op in operations:
    	cmd, num = op.split(" ")
    	num = int(num)
    	if cmd == "I":
    		heapq.heappush(min_heap, num)
    		heapq.heappush(max_heap, -num)
    	else:				# cmd == "D"
    		if len(max_heap) > 0:
	    		if num == 1:
	    			cur = heapq.heappop(max_heap)
	    			min_heap.remove(-cur)
	    		else:
	    			cur = heapq.heappop(min_heap)
	    			max_heap.remove(-cur)
    if len(max_heap)==0 :
    	answer = [0,0]
    else:
    	answer.append(-(heapq.heappop(max_heap)))
    	answer.append(heapq.heappop(min_heap))
    return answer

operations1 = ["I 16","D 1"]
operations2 = ["I 7","I 5","I -5","D -1"]
operations3 = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations3))

# 코딩테스트 연습 : Heap Level3
# Heap 을 두 개 쓰면 너무 쉽게 해결 가능한 문제.. (remove함수도 가능하다..)