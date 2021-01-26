def sequential_search(n, target, arr):
	for i in range(n):
		if arr[i] == target:		#In Python, string compare is easily done with '=' operator
			return i+1
print("Number of Element & Search Target")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]
print("Input Elements:")
arr = input().split()
print(sequential_search(n, target, arr))
# Sequential Search : O(n)