arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(arr)):
	min_idx = i
	for j in range(i+1, len(arr)):
		if arr[j] < arr[min_idx] :
			min_idx = j
	tmp = arr[i]
	arr[i] = arr[min_idx]
	arr[min_idx] = tmp
print(arr)

'''
Selection Sort:
중간에 Swap하는 부분은 python에서 한줄로 arr[i], arr[min_idx] = arr[min_idx], arr[i] 로 대체 가능
'''