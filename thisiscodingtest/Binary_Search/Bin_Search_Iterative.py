def bin_search(arr, start, end, target):	#iterative
	while start <= end:
		mid = (start+end)//2
		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			start = mid+1
		elif arr[mid] > target : #else
			end = mid-1
	return None

n, target = map(int, input().split())
arr = list(map(int, input().split()))
res = bin_search(arr, 0, n-1, target)
if res == None:
	print("No Target")
else:
	print(res+1)
#Iterative Bin Search : O(logN)
#탐색 범위가 1000만 이상이면 보통 BinSearch..