import sys
d = [0]*30001

x = int(sys.stdin.readline())
for i in range(2,x+1):
	d[i] = d[i-1]+1
	if i%2==0:
		d[i] = min(d[i], d[i//2]+1)
	if i%3==0:
		d[i] = min(d[i], d[i//3]+1)
	if i%5==0:
		d[i] = min(d[i], d[i//5]+1)
print(d[x])

'''
Basic Dynamic Problem
Reccurrence Relation: min(ai-1, ai//2, ai//3, ai//5) +1
Bottum Up DP
'''