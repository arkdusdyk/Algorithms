from itertools import combinations
def solution(orders, course):
	answer = []
	res = []
	for c in course:
		menu_list = dict()
		for order in orders:
			order = ''.join(sorted(order))
			combi = list(combinations(order, c))
			for cc in combi:
				if cc not in menu_list.keys():
					menu_list[cc] = 1
				else:
					menu_list[cc] += 1
		max_val = 0
		for value in menu_list.values():
			if value > max_val:
				max_val = value
		#print(menu_list)
		for (key,value) in menu_list.items():
			if (value == max_val) and (value >= 2):
				res.append(key)
	for r in res:
		menu = ''
		for i in r:
			menu += i
		answer.append(menu)
	answer.sort()
	return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))
# 2021 KAKAO BLIND RECRUITMENT Level2
# 구현 문제.