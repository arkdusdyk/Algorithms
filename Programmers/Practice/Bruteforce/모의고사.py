def solution(answers):
    answer = []
    scores = [0,0,0]
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i] == one[i%(len(one))]:
            scores[0] += 1
        if answers[i] == two[i%(len(two))]:
            scores[1] += 1
        if answers[i] == three[i%(len(three))]:
            scores[2] += 1
    high = scores[0]
    if scores[1] >= high:
        high = scores[1]
    if scores[2] >= high:
        high = scores[2]
    for i in range(3):
        if scores[i] == high:
            answer.append(i+1)
    return answer

answers = [1,2,3,4,5]
print(solution(answers))
# 코딩테스트 연습 : 완전탐색 Level 1