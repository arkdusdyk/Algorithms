position = input()
pos_x = ord(position[0])-ord('a') +1
pos_y = int(position[1])
dx = [-2,-2,-1,1,-1,1,2,2]
dy = [1,-1,-2,-2,2,2,-1,1]
cnt=0
for i in range(8):
	if(pos_x+dx[i]<1 or pos_x+dx[i]>8 or pos_y+dy[i]<1 or pos_y+dy[i]>8):
		continue
	cnt+=1
print(cnt)

#Implementation
#Simulation + Bruteforce
#could also move with 2d arr ex) steps = [(-2,1), (-1,-2)...]