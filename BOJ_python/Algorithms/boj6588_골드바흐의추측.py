import sys
input = sys.stdin.readline
MAX = 1000000
primes = [True for _ in range(MAX+1)]
primes[0] = False
primes[1] = False
for i in range(2, int(MAX**0.5)+1):
	j = 2
	while (i*j <= MAX):
		primes[i*j] = False
		j+=1
while True:
	n = int(input())
	if n == 0:
		break
	flag = False
	for i in range(n,2,-1):
		if primes[i] == True:
			if primes[n-i] == True:
				flag = True
				print("%d = %d + %d" %(n,n-i,i))
				break
	if flag == False:
		print("Goldbach's conjecture is wrong.")

'''
Difficulty : S1
골드바흐 추측 역시 소수 구하는 것 -> 에라토스테네스
** 골드바흐의 추측 : 4 보다 큰 모든 짝수는 모든 홀수 소수의 합으로 나타낼 수 있다! **
'''