import sys
input = sys.stdin.readline

# pyramid : 1 ~ 10000 까지의 수.
pyr = [0]*141
r = 1
i = 1
while i <= 141:
	pyr[i-1] = r
	i += 1
	r += i

def find(x):		# find row, col of x
	r,c = 0, 0
	for i in range(141):
		if x <= pyr[i]:
			r = i
			if x>1:
				c = x - (pyr[i-1] +1)
			break
	return (r,c)

t = int(input())
for i in range(1, t+1):
	a,b = map(int, input().split())
	if a > b:		#smaller as a
		a, b = b,a
	r_a, c_a = find(a)		# 좌표 찾기. r : row, c : col
	r_b, c_b = find(b)
	if r_a == r_b:			# 같은 층 : col 차이
		answer = (c_b - c_a)
	else:
		c_l, c_r = c_a, c_a			# c_l, c_r 는 c_a부터 피라미드 그려서 l,r bound
		answer = (r_b - r_a)		# 일단 level차이만큼
		for _ in range(r_b - r_a):	# row하나씩 내려가면서 c_r 증가
			c_r += 1
		if c_b < c_l:				# c_b 위치와 c_a의 피라미드 하층 꼭짓점 비교해서 col차이 더해주면 answer
			answer += (c_l - c_b)
		elif c_r < c_b:
			answer += (c_b - c_r)
	print("#%d %d" %(i, answer))

'''
아이디어는 알겠는데, level과 삼각형의 형태 안의 노드들간의 관계를
수학적으로 풀어내는거에서 헤맸지만, 사실 그럴 필요 없었다.
좌표만 잘 설정해주면 너무 쉽게 해결 가능!
'''


