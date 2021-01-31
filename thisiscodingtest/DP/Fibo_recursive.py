def fibo(x):
	if x==1 or x==2:
		return 1
	return fibo(x-1) + fibo(x-2)

print(fibo(3))

'''
fibonacci basic - recursive function
Time Complexity : O(2^n) (do same function everytime it is called...ex) fibo(6) 에서 fibo(3)만 세번 서로 다른 횟수로 진행..(중복))
-> Top down but too much time.
-> use memoization
'''
