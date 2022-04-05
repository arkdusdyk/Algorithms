import heapq
def solution(jobs):
    answer = 0
    h = []
    t, prev = 0, 0
    i = 0
    prev = -1
    while i < len(jobs):
        for j in range(len(jobs)):
            if prev < jobs[j][0] <= t:
                heapq.heappush(h, (jobs[j][1], jobs[j][0]))
        if len(h) > 0:
            on = heapq.heappop(h)
            prev = t
            t += on[0]
            answer += (t-on[1])
            i += 1
        else:
            t += 1
    return answer//len(jobs)

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))

# 코딩테스트 연습 : Heap Level3
# 쉽게 풀 수 있을 것 같았는데 생각보다 오래 걸렸다.. 