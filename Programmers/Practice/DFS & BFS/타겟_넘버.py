def solution(numbers, target):
	answer = 0
	def dfs(i, res):
		nonlocal answer
		if i == len(numbers):
			if target == res:
				answer += 1
			return
		dfs(i+1, res+numbers[i])
		dfs(i+1, res-numbers[i])

	dfs(0,0)
	return answer


numbers = [4,1,2,1]
target = 4
print(solution(numbers, target))
# 코딩테스트 연습 : DFS/BFS Level2
# Backtracking 기본 문제!!
# 조합으로 푸는게 더 편하긴 했는데 DFS 연습삼아 dfs로.