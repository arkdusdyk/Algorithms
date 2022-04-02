def solution(brown, yellow):
    answer = []
    b = (brown+4)//2
    for i in range(2, (b//2)+1):
        m = i
        n = b - m
        if (m-2)>0 and (n-2)>0:
            if yellow == (m-2)*(n-2):
                answer.append(n)
                answer.append(m)
    return answer

brown = 24
yellow = 24
print(solution(brown, yellow))
# 코딩테스트 연습 : 완전탐색 Level 2