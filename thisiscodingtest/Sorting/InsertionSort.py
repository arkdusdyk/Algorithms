arr = [7,5,9,0,3,1,6,2,4,8]
for i in range(1, len(arr)):
	for j in range(i, 0, -1):
		if arr[j] < arr[j-1]:
			arr[j], arr[j-1] = arr[j-1], arr[j]
		else:
			break
print(arr)
'''
Insertion Sort:
Worst case O(n^2) but if array is almost sorted : O(n)

based on the idea that 'sub-array before the element checking currently' is already sorted
'''