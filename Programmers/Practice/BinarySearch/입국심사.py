def solution(n, times):
    answer = 1e9
    left = 1
    right = max(times)*n
    while left <= right:
    	mid = (left + right) // 2
    	people = 0
    	for time in times:
    		people += ((mid // time))
    	if people < n:
    		left = mid+1
    	else:
    		answer = mid
    		right = mid-1
    return answer

n = 6
times = [7,10]
print(solution(n,times))
# 코딩테스트 연습 : Binary Search Level 3
# n 이 1000000000 이하이기 때문에 일반탐색으로는 불가 -> 이분탐색
# 기준 시간을 어떻게 잡는지