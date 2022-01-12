import sys
input = sys.stdin.readline
zero_cnt = [1,0]
one_cnt = [0,1]

for i in range(2,41):
	zero_cnt.append(zero_cnt[i-1] + zero_cnt[i-2])	
	one_cnt.append(one_cnt[i-1]+one_cnt[i-2])

t = int(input())
for _ in range(t):
	n = int(input())
	print(zero_cnt[n], one_cnt[n])

'''
Difficulty : S3
피보나치를 메모이제이션을 통해 O(2^N) => O(N)으로 최적화가능하다는 것은 알고있었지만
문제 해결이 생각보다 까다로웠다..
Dynamic Programming은 아직 연습이 더 필요하다.
'''