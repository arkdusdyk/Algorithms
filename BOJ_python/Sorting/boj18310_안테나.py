import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr[(n-1)//2])

'''
Difficulty : S3
너무 단순하게 해결 가능.
'''