N, M = map(int, input().split())
arr = [0 for i in range(N)]
min_list = []
for i in range(N):
	arr[i] = list(map(int, input().split()))
	min_list.append(min(arr[i]))
print(max(min_list))
#Greedy
#Just go through all mins -> find max
