def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    dist = []
    for i in range(len(rocks)):
        if i == 0:
            dist.append(rocks[i])
        else:
            dist.append(rocks[i] - rocks[i-1])
    dist.append(distance - rocks[-1])
    left, right = 1, distance
    while left <= right:
        mid = (left + right)//2
        
    print(dist)
    return answer

distance = 25
rocks = [2,14, 11, 21, 17]
n = 2
print(solution(distance, rocks, n))