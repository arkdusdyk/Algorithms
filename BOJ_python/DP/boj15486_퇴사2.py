import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]
t = []
p = []
for _ in range(n):
	in_t, in_p = map(int, input().split())
	t.append(in_t)
	p.append(in_p)

cur_max = 0

for i in range(n):
	cur_max = max(cur_max, dp[i])
	if i + t[i] > n:
		continue
	dp[i+t[i]] = max(dp[i+t[i]], cur_max + p[i])

answer = 0
for i in range(1, n+1):
	if answer < dp[i]:
		answer = dp[i]
print(answer)

'''
Difficulty : S1
DP Problem.
1) 처음에 dp[i+t[i]]와 그 이후 값들을 모두 update하는 방식 -> test case는 모두 맞았는데 시간초과 (이중 for문은 안되겄다)
-> 다른 방법으로 update가 필요했음 (cur_max 만들어서, 매 index마다 확인!)
3) 또, 반복 range를 (1, n+1)으로 하니 Indexing 처리가 생각보다 까다로웠음..
-> range(n)으로 바꿔서 전면적 수정함
'''