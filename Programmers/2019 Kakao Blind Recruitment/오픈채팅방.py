def solution(record):
    answer = []
    enter_sign = "님이 들어왔습니다."
    exit_sign = "님이 나갔습니다."
    nick = dict()
    for rec in record:
        rc = rec.split(' ')
        if (rc[0][0] == "E") or (rc[0][0] == "C"):
            nick[rc[1]] = rc[2]
    for rec in record:
        rc = rec.split(' ')
        if rc[0][0] == "E":
            answer.append(nick[rc[1]]+enter_sign)
        elif rc[0][0] == "L":
            answer.append(nick[rc[1]]+exit_sign)
    return answer
'''
2019 KAKAO BLIND RECRUITMENT Level2
구현 문제이긴 한데, 사전만 잘 쓰면 쉽게 해결 가능한 느낌이다.
'''