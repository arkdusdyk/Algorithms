import math as m
from itertools import permutations
def isPrime(num):
    if num < 2:
        return False
    last = int(m.sqrt(num))
    for i in range(2, last+1):
        if num % i == 0:
            return False
    return True
    
def solution(numbers):
    answer = 0
    num_list = []
    for num in numbers:
        num_list.append(num)
    checklist = []
    for i in range(1, len(num_list)+1):
        for num in list(permutations(num_list, i)):
            num_joined = "".join(num)
            new_num = int(num_joined)
            if new_num not in checklist:
                checklist.append(new_num)
                if isPrime(new_num) == True:
                    answer += 1
    return answer

numbers = "17"
solution(solution(numbers))
# 코딩테스트 연습 : 완전탐색 Level 2