n = int(input())
def key_ret(data):
	return data[1]
	
arr = []
for i in range(n):
	grade_input = input().split()							#grade_input consists of input strings
	arr.append((grade_input[0], int(grade_input[1])))		#append in the form of tuples ('name', grade)
arr = sorted(arr, key = key_ret)
for i in arr:
	print(i[0], end = ' ')

'''
sort using key.
key_return function없이도 lambda(특정 function 한줄 표현) 사용해서 한줄로 sorting 가능:
arr = sorted(arr, key = lambda student: student[1])
for student in arr : 
	print(student[0], end = ' ')
'''