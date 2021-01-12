N = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moves = input().split()
nav = ['L', 'R', 'U', 'D']
x,y = 1,1
for move in moves:
	for i in range(4):
		if(move == nav[i]):
			if(x+dx[i]<1 or y+dy[i]<1 or x+dx[i]>N or y+dy[i]>N):
				break
			x += dx[i]
			y += dy[i]
print(x,y)
#Implementation
#x,y 가 (x,y)라는 것 (ex) y가 y축을 의미하는게 아님)