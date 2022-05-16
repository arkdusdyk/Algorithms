import sys
input = sys.stdin.readline
answer = []
wrong = []
picked = []
for _ in range(9):
	picked.append(list(map(int, input().split(' '))))

for i in range(9):
	yes = []
	no = []
	if picked[i][0] == 1:		# 거짓말이라고 가정
		picked[i][0] = 0
	else:
		picked[i][0] = 1

	for j in range(9):
		if picked[j][0] == 1:
			yes.append(picked[j][1])
		else:
			no.append(picked[j][1])

	yes = list(set(yes))		# 1루수
	no = list(set(no))			# 1루수 아님

	for j in range(len(yes)):
		if len(yes) == 1:
			if yes[j] in yes and yes[j] not in no:
				answer.append(yes[j])
			else:
				wrong.append(yes[j])

	if len(yes) == 0:
		for j in range(1, 10):
			if j not in no:
				answer.append(j)

	if picked[i][0] == 0:		# 다시 원상복구
		picked[i][0] = 1
	else:
		picked[i][0] = 0

answer = list(set(answer))
wrong = list(set(wrong))

if len(answer) == 1:
	print(answer[0])
elif len(answer) == 0:
	if len(wrong) == 9:	# 불가
		print(-1)
	else:
		for i in range(1, 10):
			if i not in wrong:
				answer.append(i)
		if len(answer) == 1:
			print(answer[0])
		else:
			print(-1)
else:
	print(-1)

# Difficulty : G4
# 아이디어만 잘 생각하고 한 명씩 거짓말쟁이임을 가정하여 모순인 상황을 모두 확인