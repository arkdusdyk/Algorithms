n,k = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))
arr_a.sort()
arr_b.sort(reverse = True)	#두 배열 오름차순으로 정렬
for i in range(k):
	if arr_a[i] < arr_b[i]:
		arr_a[i], arr_b[i] = arr_b[i], arr_a[i]	#swap
	else:
		break
print(sum(arr_a))
'''
k번의 원소 교체로 arr_a sum 최대로 만들기
두 배열 정렬 후 쉽게 가능
'''