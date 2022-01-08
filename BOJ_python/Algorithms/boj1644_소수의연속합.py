import sys
input = sys.stdin.readline

n = int(input())
s_primes = [1 for i in range(n+1)]
s_primes[0] = 0
s_primes[1] = 0
for i in range(2, int(n**0.5)+1):		# 에라토스테네스의 체 (소수 확인)
    j = 2
    while(i*j<=n):
        s_primes[i*j] = 0
        j+=1

prime_list = []
for i in range(2, n+1):					# n이하 소수 리스트
	if s_primes[i] == 1:
		prime_list.append(i)

def cont_prime(x):
	answer = 0
	if x <= 1:
		return 0
	for i in range(len(prime_list)):			#two_pointer로 부분합 확인
		r_sum = 0
		for j in range(i, len(prime_list)):
			r_sum += prime_list[j]
			if r_sum == x:
				answer += 1
				break
			elif r_sum > x:
				break
	return answer
print(cont_prime(n))

'''
Difficulty : G3
Sieve of Eratosthenes (Find the primes) + Two Pointer (Check Range Sum) => Time Efficiency
'''