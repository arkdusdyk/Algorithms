def solution(numbers):
    answer = ''
    num_list = []
    for num in numbers:
        num_list.append(str(num))
    num_list.sort(key = lambda x: x*3, reverse = True)
    answer = str(int(''.join(num_list)))
    return answer

numbers = [6,10,2]
numbers2 = [3, 30, 34, 5, 9]
numbers3 = [0,0,0,0]
print(solution(numbers3))

# 코딩테스트 연습 : 정렬 Level2
# 3을 곱하는 방법이 굉장히 참신하다. number의 크기가 최대 세자리라는 것을 인지하는 것이 중요