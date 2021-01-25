arr = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(arr, start, end):	#recursive 활용
	if start >= end:
		return
	pivot = start
	left = start+1
	right = end
	while left <= right:
		while left <= end and arr[left] <= arr[pivot]:	#left = first value bigger than pivot
			left+=1
		while right > start and arr[right] >= arr[pivot]:	#right = first value smaller than pivot
			right-=1
		if left > right:	#if left, right switched -> swap pivot and right
			arr[right], arr[pivot] = arr[pivot], arr[right]
		else:		#swap left, right
			arr[left], arr[right] = arr[right], arr[left]
	quick_sort(arr,start,right-1)
	quick_sort(arr, right+1, end)
quick_sort(arr,0,len(arr)-1)
print(arr)
'''
Quicksort : O(nlogn). however if array is already almost sorted -> O(n^2)
Using python, can also go with code below
def quick_sort(arr):
	if len(arr)<=1:
		return arr
	pivot = arr[0]
	tail = arr[1:]
	left = [x for x in tail if x<=pivot]
	right = [x for x in tail if x> pivot]
	return quick_sort(left) + [pivot] + quick_sort(right) 		#return full list