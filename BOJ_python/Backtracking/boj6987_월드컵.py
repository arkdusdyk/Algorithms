import sys
from itertools import combinations
input = sys.stdin.readline
answer = []

def dfs(n):		#round 1~15
	global check
	if n == 16:
		flag = True
		for checker in res:
			if checker == [0,0,0]:
				continue
			else:
				flag = False
				break
		if flag == True:
			check = 1
		return

	match = match_list[n-1]
	# check team1 W, team2 L
	if res[match[0]][0] > 0 and res[match[1]][2] > 0:
		res[match[0]][0] -= 1
		res[match[1]][2] -= 1
		dfs(n+1)
		res[match[0]][0] += 1
		res[match[1]][2] += 1

	# check team1, team2 D
	if res[match[0]][1] > 0 and res[match[1]][1] > 0:
		res[match[0]][1] -= 1
		res[match[1]][1] -= 1
		dfs(n+1)
		res[match[0]][1] += 1
		res[match[1]][1] += 1

	# check team1 L, team2 W
	if res[match[0]][2] > 0 and res[match[1]][0] > 0:
		res[match[0]][2] -= 1
		res[match[1]][0] -= 1
		dfs(n+1)
		res[match[0]][2] += 1
		res[match[1]][0] += 1


teams = [i for i in range(6)]				# 팀 0 ~ 5
match_list = list(combinations(teams, 2))	# match 조합 (combinations 활용)
for _ in range(4):			# case
	wc = list(map(int, input().split()))
	res = []
	for i in range(0,18,3):
		res.append(wc[i:i+3])		# res[0] : T1 W,D,L, res[1] : T2 W,D,L, ...

	check = 0
	dfs(1)
	answer.append(check)

for ans in answer:
	print(ans)

'''
Difficulty : G5
고민한 순서
1) 어떤 유형? 백트래킹, 완전 탐색 (조합)
2) 어떤 자료구조에 어떤 식으로 저장할까? 리스트? 사전형? => 리스트로도 충분할듯

아이디어가 바로 떠오른 문제여서 금방금방 해결
중간에 생긴 문제 : 백트래킹으로 각 결과표에서 하나씩 빼가면서 확인하는 방식인데 음수일때를 제외해주지 않아서 중간에 실행이 멈추지 않는 문제
-> line 22, 30, 38 추가해주는 부분 하나로 해결!
'''