'''
조합 활용.
조건 : 알파벳 순, 모음 1개 이상, 자음 2개 이상
'''
from itertools import combinations
l,c = map(int, input().split(' '))
arr = input().split(' ')
arr.sort()  #알파벳 순 정렬
for pwd in combinations(arr,l):	#arr에서 l개로 조합
    flag=0
    for i in pwd:
        if i in ['a', 'e', 'i', 'o', 'u']:
            flag+=1
    #flag가 결국 의미하는건 모음 갯수, l-flag가 자음 갯수
    if(flag>=1 and l-flag >=2):
        print(''.join(pwd))
        #join함수 활용 : 리스트 문자열 합치기

'''
Difficulty : G5
조합을 통해 permutation을 진행하면 쉽게 할 수 있는데, 여러번 봐야할 것 같다.
-> 모음 자음 갯수 구분하는 법 이렇게 쉽게 할 수 있을지 + 리스트 문자열 합칠때 사용하는 join 함수
'''