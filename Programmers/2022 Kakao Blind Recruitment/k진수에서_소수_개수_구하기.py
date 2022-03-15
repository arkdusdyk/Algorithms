import math
def solution(n,k):
	answer = 0
	def todigit(n,k):	# 진법 변환 함수
		new = ''
		while n > 0:
			rem = n % k
			n = n // k
			new += str(rem)
		return new[::-1]

	def isPrime(n):
		if n == 0 or n == 1:
			return False
		if n == 2:
			return True
		for i in range(2, int(math.sqrt(n))+1):
			if n % i == 0:
				return False
		return True

	digit = todigit(n,k)
	check_list = digit.split('0')

	for i in range(len(check_list)):		# 미리 숫자로 변환
		if check_list[i] == '':		# 0으로 처리
			check_list[i] = 0
		else:
			check_list[i] = int(check_list[i])
	
	if len(check_list) == 1 :		# P
		if isPrime(check_list[0]) == True:
			answer += 1
	else:							# P0, 0P0, 0P
		for n in check_list:
			if isPrime(n) == True:
				answer += 1
	return answer

n = 437674
k = 3
print(solution(n,k))

'''
2022 KAKAO Blind Recruitment Level2
중복된 소수여도 규칙에 따라 따로 세어야함 -> 규칙 하나씩 숫자 찾아서 소수 확인하자
-> 0을 기준으로만 나눠도 된다 (ex) 101은 1,1,101 다 확인하는게 아니라 1, 1만 됨)

처음에는 소수 판별을 최대값 구해서 에라토스테네스 체로 풀었는데 test case 두개가 시간초과..
-> root(n)까지만 판별하는건 맞게 했는데..
-> 나머지 값들을 다 찾을 필요는 없을 것 같아서 단순하게 소수인지 판별하는 함수 만들어서 해결.
'''