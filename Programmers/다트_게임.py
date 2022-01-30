def solution(dartResult):
    answer = 0
    bonus = {'S':1, 'D':2, 'T':3}
    num = ''
    score = []
    for ch in dartResult:
        if ch.isdigit():
            num += ch
        else:
            if ch in 'SDT':
                score.append(int(num)**bonus[ch])
            elif ch == '*':
                if len(score) > 1:
                    score[-2] *= 2
                score[-1]*=2
            elif ch == '#':
                score[-1] *= -1
            num = ''
    answer = sum(score)
    return answer


# 2018 카카오 Blind Recruitment
# 문자열 구현 문제
