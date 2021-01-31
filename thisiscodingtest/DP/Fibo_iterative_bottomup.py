d = [0]*100
d[1] =1
d[2] =1
for i in range(3,100):
	d[i] =  d[i-1] + d[i-2]
print(d[99])
'''
Fibonacci  - Iterative function (DP table)
 <Bottom Up> - solve big problem from smaller problems to bigger...
-> bottom up is not really memoization
 Time Complexity : O(n)
'''