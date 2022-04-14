def solution(name):
    answer = int(1e9)
    moves = list(min(ord("Z")-ord(i)+1,ord(i)-ord("A")) for i in name)

    def dfs(moves, i, lr, cnt):
        cnt += lr
        cnt += moves[i]
        moves[i] = 0
        if sum(moves)==0:
            print(cnt+lr+moves[i])
            return
        l,r = 1,1
        while moves[i-l] == 0:
            l += 1
        while moves[i+r] == 0:
            r += 1
        tmp = moves[i]
        dfs(moves, i-l, l, cnt)
        dfs(moves, i+r, r, cnt)
        moves[i] -= tmp


    dfs(moves, 0, 0, 0)
    return answer

name = "JEROEN"
print(solution(name))
# 코딩테스트 연습 : Greedy Level 2
# Greedy 문제인데, Greedy로 절대 못푼다.
# 이 문제 보이는 것보다 훨씬 어려웠는데, Greedy가 아니라 완전탐색으로 풀어야한다.
# 테케들까지 모두 맞추기 위해서는 한 쪽으로만 이동하는 횟수를 세서는 충분하지 않다.