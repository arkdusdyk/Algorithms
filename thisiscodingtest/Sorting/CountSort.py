arr = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
cnt = [0 for i in range(max(arr)+1)]
for i in range(len(arr)):
	cnt[arr[i]]+=1
for i in range(len(cnt)):
	for j in range(cnt[i]):
		print(i, end = ' ')
'''
Count Sort : O(N+K) in any case
처음에는 count sort가 도대체 무엇일까 했는데
사실 그냥 단순하게 값에 대한 count만 세서 그 횟수 출력하는 방법, => 당연히 데이터의 범위가 한정된 경우만 가능
this method can be inefficient -> spatially
'''