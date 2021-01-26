import sys
n, m = map(int, sys.stdin.readline().split())
n_arr = list(map(int, sys.stdin.readline().split()))
n_arr.sort()
start = 0
end = max(n_arr)
res = end
while(start <= end):
	cut_arr = []
	mid = (start+end)//2
	for i in n_arr:
		leftover = i-mid
		if leftover<0 :
			leftover=0
		cut_arr.append(leftover)
	total_cut = sum(cut_arr)
	if(total_cut<m):
		end = mid-1
	else:
		res = mid	#결과저장
		start = mid+1
print(res)

'''
가지 치기 문제와 비슷 (Parametric Search)
M크기가 너무 크기 때문에 Sequentially 확인은 시간 초과 -> binary search로 접근해서 left over sum으로 탐색 pivot 이동
left over 값들을 배열에 저장해놓고 합을 확인하면서 탐색 범위 이동
'''