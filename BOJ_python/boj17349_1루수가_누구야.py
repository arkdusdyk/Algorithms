import sys
input = sys.stdin.readline
checker = [0] * 10

picked = dict()
answer = 0
answer_flag = False
for _ in range(9):
	flag, a = map(int, input().split(' '))
	if a not in picked:
		picked[a] = 1
		checker[a] += flag
	else:
		picked[a] += 1
		checker[a] += flag

sus = []
check = [False] * 10
for player in picked:
	times = picked[player]
	check[player] = True
	if times > 1:
		if (0 < checker[player] < times):
			sus.append(player)
if len(sus) == 1:
	print(sus[0])
else:
	for i in range(1,10):
		if check[i] == False:
			sus.append(i)
	if len(sus) == 1:
		print(sus[0])
	else:
		print(-1)