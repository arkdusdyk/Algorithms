import sys
input = sys.stdin.readline
INF = int(1e9)
neg = False

def bellman():
	global neg			# return값을 없애고 전역변수로 flag를 처리해봤더니 시간이 20ms 감소 (얼마나 효율적일지는 모르겠음)
	cost[1] = 0
	for i in range(n):		# N번 반복 (마지막 회차는 음수 간선 순환 확인용)
		for j in range(m):	# 모든 간선 확인
			a,b,c = edge[j]
			if cost[a] != INF and cost[a]+ c < cost[b]:
				cost[b] = cost[a] + c
				if i == n-1:	# 갱신이 마지막 회차라면 => 음수 간선 순환 존재
					neg = True
	return

n,m = map(int, input().split())		# n : 도시 갯수, m : 버스 노선 갯수
cost = [INF]*(n+1)
edge = []
for _ in range(m):
	a,b,c = map(int, input().split())
	edge.append((a,b,c))

bellman()
if neg == True:
	print("-1")
else:
	for i in range(2, n+1):
		if cost[i] == INF:
			print("-1")
		else:
			print(cost[i])

'''
Difficulty : G4
Bellman-Ford Algorithm
'''