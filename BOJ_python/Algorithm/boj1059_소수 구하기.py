#에라토스테네스의 체
import math
m, n = map(int, input().split())
arr = [True for i in range(n+1)]
arr[0] = 0
arr[1] = 0
for i in range(2, int(math.sqrt(n)+1)):
#제곱근까지만 확인,  O(root(n))으로 단축
    j = 2
    while(i*j<=n):
        arr[i*j] = 0
        j+=1

for i in range(m,n+1):
    if(arr[i]==True):
        print(i)
'''
Difficulty : S5
에라토스테네스의 체 연습 문제
'''