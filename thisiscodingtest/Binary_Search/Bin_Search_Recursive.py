def bin_search(arr, start, end, target):		#Recursive
	if start > end:
		return None
	mid = (start+end)//2
	if arr[mid] == target:
		return mid
	elif arr[mid] > target:
		return bin_search(arr, start, mid-1, target)
	elif arr[mid] < target:	#else
		return bin_search(arr, mid+1, end, target)

n, target = map(int, input().split())
arr = list(map(int, input().split()))
res = bin_search(arr, 0, n-1, target)
if res == None:
	print("No Target")
else:
	print(res+1)
#Recursive Binary Search : O(logN)