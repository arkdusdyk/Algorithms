import sys
def bin_search(arr, target, start, end):	#Iterative
	while(start<=end):
		mid = (start+end)//2
		if(target==arr[mid]):
			return True
		elif(target<arr[mid]):
			end = mid-1
		else:
			start = mid+1
	return False

n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))
n_arr = sorted(n_arr)
m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))
for i in range(m):
	if(bin_search(n_arr, m_arr[i], 0, n-1)==True):
		print("yes", end = ' ')
	else:
		print("no", end = ' ')

'''
M (1<= M <= 100,000), N (1<=N<=1,000,000)
Sequential 하게 M개를 모두 찾는것: O(M*N) -> 시간초과 날 가능성 높음.
위 코드에서는 Binary Search(Iterative) 활용함. O(M*logN + N*logN) = O((M+N)*logN)
Alternative : 
1. Counting도 가능
ex) n_arr = [0]*1000001
for i in input().split():
	n_arr[int(i)] = 1
m 입력받고, 각 원소별로 n_arr에 있는지 확인 -> O(M)

2. Using Set
ex) n_arr = set(map(int, input().split()))	#set자료형에 저장
m입력후,
for i in m_arr:
	if i in n_arr:
		print(yes)
	else:
		print(no)

Set자료형으로 저장을 하면 단순히 존재 유무 (한번이라도 등장한지)만 확인하면 될때 효과적으로 처리 가능, 간결
'''