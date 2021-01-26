arr = [7,5,9,0,3,1,6,2,4,8]
#basic libraries
#1. sorted(list)
print(sorted(arr))

#2. list.sort()
arr.sort()
print(arr)

#3. Using keys in sorting libraries
array = [('Banana', 2), ('Apple', 5), ('Carrot', 3)]	#List Data: tuple form
def setting(data):
	return data[1]
print(sorted(array, key = setting))	#sort by key

#Sorted Libraries in Python
#기본적으로 오름차순
#can also use lambda function