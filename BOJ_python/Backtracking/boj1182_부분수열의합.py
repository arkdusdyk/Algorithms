import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

def dfs(i, graph, total):
	global answer, n, s
	if total == s:
		answer += 1
	for j in range(i+1, n):
		dfs(j, graph, total + graph[j])

for i in range(0, n):
	dfs(i, arr, arr[i])

print(answer)
'''
Difficulty : S2
Bruteforce + Backtracking


* 이런식으로도 짤 수 있다...
def dfs(i, graph, total):
    global answer, n, s
    if i == n: 
        return
    if total + graph[i] == s:
        answer += 1
    dfs(i+1, graph, total)
    dfs(i+1, graph, total + graph[i])

###
1) dfs(i+1, graph, total) : 해당 숫자를 더하지 않고 확인
2) dfs(i+1, graph, total + graph[i]) : 해당 숫자를 더하고 확인

'''