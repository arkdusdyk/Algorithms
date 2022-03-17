import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
ing = []
mp, mf, ms, mv = map(int, input().split())
for _ in range(n):
	ing.append(list(map(int, input().split())))

a_cost = 7500
a_list = []
idx = [i for i in range(1,n+1)]
for i in range(1,n+1):
	c = list(combinations(idx, i))
	#print(c)
	for j in range(len(c)):
		price = 0
		p, f, s, v = 0,0,0,0
		for k in range(i):
			p += ing[c[j][k]-1][0]
			f += ing[c[j][k]-1][1]
			s += ing[c[j][k]-1][2]
			v += ing[c[j][k]-1][3]
			price += ing[c[j][k]-1][4]
		if (p>=mp) and (f>=mf) and (s>=ms) and (v>=mv):
			if price < a_cost:
				a_list = []
				a_list.append(c[j])
				a_cost = price
			elif price == a_cost:
				a_list.append(c[j])
if len(a_list) == 0:
	print(-1)
else:
	a_list.sort()
	print(a_cost)
	print(*a_list[0])

'''
Difficulty : G5 (Bruteforce)
asterisk 사용해서 tuple unpacking 해본게 뿌듯함.
조합 순서로 확인해서 같은 price일때 먼저 있는 것을 채택하는 것 -> 반례 존재!! (한 번 틀림)
- ex) (3) (1,3) (2,3), (1,2,3) 에서 사전순으로는 1,2,3
'''