def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    sum_board = [[0]*m for _ in range(n)]
    
    for s in skill:
        r1, c1, r2, c2 = s[1:5]
        deg = s[5]
        if s[0] == 1:   # 파괴
            deg *= -1
        sum_board[r1][c1] += deg
        if (r2+1 < n) and (c2+1 < m):
            sum_board[r2+1][c2+1] += deg
        if r2+1 < n:
            sum_board[r2+1][c1] -= deg
        if c2+1 < m:
            sum_board[r1][c2+1] -= deg
    for i in range(n):
        for j in range(1, m):
            sum_board[i][j] += sum_board[i][j-1]
    for i in range(m):
        for j in range(1, n):
            sum_board[j][i] += sum_board[j-1][i]
    for i in range(n):
        for j in range(m):
            if board[i][j] + sum_board[i][j] > 0:
                answer += 1
    return answer

'''
2022 KAKAO BLIND RECRUITMENT Level 3.
*** 누적합 *** 배열을 새로 만들어서 관리하는 방법.
'''