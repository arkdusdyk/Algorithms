import sys
input = sys.stdin.readline
n, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

# 로봇 (들어온 순서)의 위치 저장하는 큐
# arr : 내구도 컨베이어벨트
# exist : 로봇이 현재 칸에 몇 개 존재하는지
robot = []
exist = [0]*(2*n)
t = 0
while arr.count(0) < k:
	t += 1
	# Step1
	# 컨베이어 벨트 이동
	last = arr[-1]
	e_last = exist[-1]
	for i in range(2*n-1, 0,-1):
		arr[i] = arr[i-1]
		exist[i] = exist[i-1]
	arr[0] = last
	exist[0] = e_last
	# 로봇도 같이 이동
	down_flag = False
	for i in range(len(robot)):
		next_robot = (robot[i]+1)%(2*n)
		if next_robot == n-1 :	#내리는 위치
			exist[n-1] -= 1
			down_flag = True	# 로봇 내리기
		else:
			robot[i] = (robot[i]+1)%(2*n)
	if down_flag == True:
		robot.pop(0)

	# Step2
	# 먼저 올라간 로봇부터 벨트 회전하는 방향으로 이동 (가능할때만)
	down_flag = False
	for i in range(len(robot)):
		p = robot[i]
		n_p = (p+1)%(2*n)
		if exist[n_p] > 0:
			continue
		if arr[n_p] < 1:
			continue
		# 이동 가능
		exist[p] -= 1
		robot[i] = n_p
		exist[n_p] += 1
		if n_p == n-1:
			down_flag = True
			exist[n_p] -= 1
		arr[n_p] -= 1

	# 내리기에 도착한 로봇 존재
	if down_flag == True:
		robot.pop(0)

	# Step3
	if arr[0] > 0:
		robot.append(0)
		arr[0] -= 1
		exist[0] += 1

print(t)

# Difficulty : G5
# 삼성 SW 역량 테스트 기출 문제집 - Simulation
# 문제 설명을 이해하기만 하면 쉬움. 설명이 조금 부족하다는 생각. ex) 로봇을 올리고 내리는 것은 1~N, 컨베이어벨트는 1~2N
# 구현 자체는 차근 차근하면 무난. PyPy3로 하면 통과인데 Python3로 제출하니 시간 초과..
# q = deque, q.rotate(1)로 회전 매우 쉽게 처리 가능!
