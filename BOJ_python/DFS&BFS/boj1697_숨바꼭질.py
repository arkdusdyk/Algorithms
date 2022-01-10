import sys
from collections import deque
input = sys.stdin.readline
MAX = 100000
n,k = map(int, input().split())
visited = [False for _ in range(MAX+1)]
def bfs(n,k):
	q = deque()
	q.append(n)
	visited[n] = True
	x = 0
	flag = False
	while q:
		qsize = len(q)
		for i in range(qsize):
			fr = q.popleft()
			if fr == k:
				flag = True
				break
			if fr-1 >=0 and visited[fr-1] == False:
				visited[fr-1] = True
				q.append(fr-1)
			if fr+1 <= MAX and visited[fr+1] == False:
				visited[fr+1] = True
				q.append(fr+1)
			if 2*fr <= MAX and visited[2*fr] == False:
				visited[2*fr] = True
				q.append(2*fr)
		if flag == True:
			break
		x += 1
	print(x)	

bfs(n,k)

'''
Difficulty : S1
BFS 사용해서 각 초에 대해 다음 step을 queue에 삽입하면서 확인.
'''