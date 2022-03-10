import sys
input = sys.stdin.readline

n = int(input())
coord = []
for _ in range(n):
	x,y = map(int, input().split())
	coord.append((x,y))

def solution(coord):
	answer = 0
	prev_x, prev_y = coord[0]
	if n == 1:
		return prev_y - prev_x
	for i in range(1, n):
		cur_x = coord[i][0]
		cur_y = coord[i][1]
		if prev_y >= cur_x:
			if prev_y < cur_y:
				prev_y = cur_y
			#prev_x 는 유지
		else:
			answer += (prev_y - prev_x)
			prev_y = cur_y
			prev_x = cur_x
	answer += (prev_y - prev_x)
	return answer

coord.sort()
print(solution(coord))

'''
Difficulty : G5
포인터만 관리해주니깐 쉽게 해결 가능
'''