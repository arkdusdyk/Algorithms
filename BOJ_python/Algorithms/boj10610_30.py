import sys
input = sys.stdin.readline
n = int(input())
n = list(str(n))
n.sort(reverse = True)

sum_of_digit = 0
for i in range(len(n)):
	sum_of_digit += int(n[i])


if sum_of_digit % 3 == 0:
	if n[-1] == '0':
		print(''.join(n))
	else:
		print(-1)
else:
	print(-1)

# Math
# 30의 배수 : (자리수 모두 더했을때 3의 배수 (3의 배수)) and (ends with 0 (10의 배수))