N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
max_1 = arr[0]
max_2 = arr[1]
res = 0
while(M>0):
	for i in range(K):
		res += max_1
		M-=1
		if(M<=0):
			break
	if(M<=0):
		break
	res += max_2
	M-=1
print(res)

# code above : O(M*K)
# how to make it better?
'''
count = int(M/(K+1))*K
count += M % (K+1)

res = 0
res += count * max_1
res += (M-count)*max_2
print(res)

# idea : calculate the interval beforehand -> 아마 O(1)