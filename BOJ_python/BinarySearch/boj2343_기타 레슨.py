import sys
def blueray_check(arr, n,m,mid):
	cnt=1
	subsum=0
	for i in range(n):
		if arr[i] > mid :		#impossible
			return 0
		subsum+= arr[i]
		if subsum > mid :
			subsum = arr[i]	#begin filling next blueray
			cnt+=1
	if cnt <= m :		#sufficient blueray
		return 1
	else :
		return 0

n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
start = 1
end = sum(arr)
res = 0
while start <= end:
	mid = (start+end)//2
	if(blueray_check(arr, n, m, mid)):
		end = mid-1
		res = mid
	else:
		start = mid+1
print(res)
'''
Difficulty : S1
Binary Search, Implementation
이분 탐색을 활용해서 적합한 blueray 크기를 찾는 알고리즘.
'''