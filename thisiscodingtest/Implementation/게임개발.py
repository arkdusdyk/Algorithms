N, M = map(int, input().split())
pos_x, pos_y, dir_in = map(int, input().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
arr = [0 for i in range(N)]
for i in range(N):
	arr[i] = list(map(int, input().split()))
arr[pos_x][pos_y] = 2
direction = dir_in
cnt =1
not_found = 0

def next_dir(cur_dir):
	n_dir = cur_dir-1
	if(n_dir==-1):
		n_dir=3
	return n_dir

while(True):
	if(not_found==4):	#stuck
		break
		if(arr[pos_x-dx[direction]][pos_y-dy[direction]]==1):	#ocean behind
			break
		pos_x = pos_x -dx[direction]
		pos_y = pos_y -dy[direction]
		not_found=0
	if(arr[pos_x + dx[next_dir(direction)]][pos_y+dy[next_dir(direction)]]==0):	#found unvisited land
		direction = next_dir(direction)
		pos_x = pos_x + dx[direction]
		pos_y = pos_y + dy[direction]	#move
		arr[pos_x][pos_y] = 2			#mark visited
		cnt+=1
		not_found=0
	else:
		not_found+=1
		direction = next_dir(direction)
print(cnt)
'''
visited land = 2
ocean = 1
not visited land = 0
'''