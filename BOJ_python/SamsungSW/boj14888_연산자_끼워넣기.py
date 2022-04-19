import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split(' ')))
op = list(map(int, input().split(' ')))
max_ans = -int(1e9)
min_ans = int(1e9)

def dfs(result, i):
	global op, max_ans, min_ans
	if i == n:
		max_ans = max(max_ans, result)
		min_ans = min(min_ans, result)
		return
	if op[0] > 0:	# add
		op[0] -= 1
		dfs(result + arr[i], i+1)
		op[0] += 1
	if op[1] > 0:	# sub
		op[1] -= 1
		dfs(result - arr[i], i+1)
		op[1] += 1
	if op[2] > 0:	# mult
		op[2] -= 1
		dfs(result * arr[i], i+1)
		op[2] += 1
	if op[3] > 0:	# div
		op[3] -= 1
		dfs(int(result/arr[i]), i+1)
		op[3] += 1

dfs(arr[0], 1)
print(max_ans)
print(min_ans)