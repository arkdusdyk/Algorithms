def solution(people, limit):
    answer = 0
    people.sort()	# 50, 50, 70, 80
    min_i = 0
    max_i = len(people)-1
    while min_i <= max_i:
    	answer += 1
    	if people[min_i] + people[max_i] <= limit:
    		min_i += 1
    	max_i -=1
    return answer

people = [70,80,50]
limit = 100
print(solution(people, limit))
# 코딩테스트 연습 : Greedy Level 2
# 최대 2명씩 탄다 -> 매우 간단
# 다양한 방법이 떠오르긴 했는데 결국 가장 간단한 방법이 정답