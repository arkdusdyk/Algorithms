import sys
input = sys.stdin.readline
a,b = map(int, input().split())
'''
# 1. 직접 구하기
if a < b:			# swap (a > b가 되도록)
	a, b = b, a
for i in range(b,0,-1):		# 최대공약수
	if b%i ==0 and a%i == 0:
		print(i)
		break
for i in range(a,(a*b)+1):		#최소공배수
	if i%a==0 and i%b==0:
		print(i)
		break
'''
# 2. 유클리드 호제법
def gcd(x,y):
	while(y):
		x,y = y, x%y
	return x

def lcm(x,y):
	res = (x*y)//gcd(x,y)
	return res

print(gcd(a,b))
print(lcm(a,b))
'''
# 3. Math Module
print(math.gcd(a,b))
print(math.lcm(a,b))
'''

'''
Difficulty : S5
최대공약수와 최소공배수 구하는 법 (다양한 방법으로 시간 비교 해보았음)
1. 직접 구하기 : PyPy3 메모리 : 124504KB, 시간 : 756 ms, Python3 시간초과
2. 유클리드 호제법 : PyPy3 메모리 : 123316KB, 시간 : 100ms, Python3 29200KB, 시간:68ms
3. Python Math module (math.gcd, math.lcm) : 메모리 : 31312KB, 시간:68ms (Python3 에서만 가능. PyPy X)
=> 직접 구하는 것에 비해 유클리드 호제법이 훨씬 빠름. (== module을 갖다쓰는것과 거의 비슷)
'''