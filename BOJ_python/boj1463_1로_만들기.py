import sys
d = [0]*1000001

x = int(sys.stdin.readline())
for i in range(2,x+1):
	d[i] = d[i-1]+1
	if i%3==0:
		d[i] = min(d[i], d[i//3]+1)
	if i%2==0:
		d[i] = min(d[i], d[i//2]+1)
print(d[x])

'''
Difficulty : S3
Basic Dynamic Problem
Reccurrence Relation: min(ai-1, ai//2, ai//3) +1
Bottum Up DP

Tried: if, elif.-> Realized if input is multiple of 6, need to check both
'''