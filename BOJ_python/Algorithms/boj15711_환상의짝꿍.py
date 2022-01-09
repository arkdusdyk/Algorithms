import sys
input = sys.stdin.readline
MAX = 2*1000000
primes = [True for _ in range(MAX+1)]
for i in range(2, int(MAX**0.5)+1):
	j = 2
	while (i*j <= MAX):
		primes[i*j] = False
		j+=1
prime = [i for i in range(2,MAX+1) if primes[i] == True]


def is_prime(x):
	if x>= MAX:		# root(4*(10**12))인 2*(10**6)까지 소수들로 나누어보면 확인 가능
		for i in range(len(prime)):
			if prime[i] >= MAX:
				break
			elif x%prime[i] == 0:
				return False
		return True
	else:			# 미리 구해놓은 리스트 확인
		return primes[x]

t = int(input())
for _ in range(t):
	a, b = map(int, input().split())
	m = a+b
	if m < 4:			# 2, 3인 경우 불가능
		print("NO")
	else:
		if m%2==0:			# 골드바흐의 추측 (4보다 큰 짝수들 => 홀수 소수들의 합으로 나눌 수 있)
			print("YES")
		else:
			if is_prime(m-2):	#is_prime으로 확인
				print("YES")
			else:
				print("NO")

'''
Difficulty : G3
에라토스테네스의 체 + 골드바흐 활용
but 입력 범위 : 2*(10^12) 두 개이기 때문에 총 4*(10^12)만큼 만들면, 메모리 + 시간 초과!!
=> 그 제곱근인 2*(10^6)까지 먼저 확인

4보다 큰 짝수들 : 어제 해본 '골드바흐 추측' 활용 가능
4보다 큰 홀수들 : 확인
	1) 2*(10^6)이내의 값 : 미리 만들어놓은 소수 확인 배열로 확인
	2) 그보다 커지면 (<4*(10^12)) : 미리 만들어놓은 소수들로 나누어보고, 나누어지지 않으면 소수 X
'''