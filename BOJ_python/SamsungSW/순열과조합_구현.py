def combination_without_itertools(array, r):
	for i in range(len(array)):
		if r == 1:
			yield [array[i]]
		else:
			for next in combination_without_itertools(array[i+1:], r-1):
				yield [array[i]] + next

def permutation_without_itertools(array, r):
	for i in range(len(array)):
		if r == 1:
			yield [array[i]]
		else:
			for next in permutation_without_itertools(array[:i]+array[i+1:], r-1):
				yield [array[i]] + next
arr = [2,3,4,5]
print(list(combination_without_itertools(arr, 2)))
print(list(permutation_without_itertools(arr, 2)))

# Permutation, Combination without itertools library