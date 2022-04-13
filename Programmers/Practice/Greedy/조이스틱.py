def solution(name):
    answer = 0
    moves = list(min(ord("Z")-ord(i)+1,ord(i)-ord("A")) for i in name)
    i = 0
    while True:
        answer += moves[i]
        moves[i] = 0
        if sum(moves)==0:
            break
        l, r = 1,1
        while moves[i-l] == 0:
            l += 1
        while moves[i+r] == 0:
            r += 1
        if l < r:
            answer += l
            i = (i-l)%len(moves)
        else:
            answer += r
            i = (i+r)%len(moves)
    return answer

name = "JEROEN"
print(solution(name))
# 코딩테스트 연습 : Greedy Level 2
# 해설을 찾아보니, 한쪽으로만 이동하는 것이랑 가다가 돌아와서 거꾸로 이동하는 것만 비교하면 된다고는 하는데,
# 내가 한 방식이 더 직관적인 것 같다.