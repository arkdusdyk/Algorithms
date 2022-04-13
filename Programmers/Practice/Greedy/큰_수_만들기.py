def solution(number, k):
	answer = ''
	stack = []
	i = 0
	while i < len(number):
		if not stack:
			stack.append(number[i])
			i+=1
		else:
			while stack and number[i] > stack[-1]:
				if k <= 0:
					break
				stack.pop()
				k-=1
			stack.append(number[i])
			i += 1
	if len(stack) > (len(number)-k):
		stack = stack[:-k]
	answer = ''.join(stack)
	return answer

number = "654321"
k = 5
print(solution(number,k))
# 코딩테스트 연습 : Greedy Level 2
# 17,18 줄을 처음에 빼먹었지만 그 외에는 크게 어려움이 없었다.