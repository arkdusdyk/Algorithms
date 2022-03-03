import math
def solution(fees, records):
    answer = []    
    cars = []
    record_list = []
    for rec in records:
        time, c_no, io = rec.split(' ')
        if c_no not in cars:
            cars.append(c_no)
        t1, t2 = time.split(':')
        time = int(t1)*60 + int(t2)
        record_list.append((time, c_no, io))
    cars.sort()
    for c in cars:
        total_parked = 0
        in_flag = False
        in_time = 0
        for rec in record_list:
            if rec[1] == c:
                if rec[2] == 'IN':
                    in_time = rec[0]
                    in_flag = True
                elif rec[2] == 'OUT':
                    total_parked += (rec[0] - in_time)
                    in_flag = False
        if in_flag == True:
            total_parked += (1439 - in_time)

        cost = fees[1]
        if total_parked > fees[0]:
            cost += (math.ceil((total_parked-fees[0])/fees[2]) * fees[3])
        answer.append(cost)
    return answer

#fees = [180, 5000, 10, 600]
#records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
#print(solution(fees, records))

# 2022 KAKAO Blind Recruitment Level1
# 구현 문제! 차근차근 규칙만 지키면 쉽게 해결 가능했다.