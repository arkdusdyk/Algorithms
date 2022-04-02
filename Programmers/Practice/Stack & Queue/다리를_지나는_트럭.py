def solution(bridge_length, weight, truck_weights):
    answer = 0
    cur = [0]*bridge_length

    while len(cur) > 0:
    	answer += 1
    	cur.pop(0)
    	if len(truck_weights)>0:
	    	if (sum(cur) + truck_weights[0]) <= weight:
	    		cur.append(truck_weights.pop(0))
	    	else:
	    		cur.append(0)
    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))
# 코딩테스트 연습 : 스택/큐 Level2