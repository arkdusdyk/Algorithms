from itertools import combinations
def solution(clothes):
    answer = 1
    clothes_dict = dict()
    for cloth in clothes:
    	if cloth[1] in clothes_dict:
    		clothes_dict[cloth[1]] += 1
    	else:
    		clothes_dict[cloth[1]] = 1
    for val in clothes_dict.values():
    	answer *= (val+1)
    answer -= 1
    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
# 코딩테스트 연습 : Hash Level2