import sys
input = sys.stdin.readline
n = int(input())
alph = dict()
answer = 0
for _ in range(n):
	word = input().strip()
	digit = 1
	for i in range(len(word)-1, -1,-1):
		if word[i] in alph.keys():
			alph[word[i]] += digit
		else:
			alph[word[i]] = digit
		digit*=10
sorted_alph = sorted(alph.items(), key = lambda item: item[1], reverse = True)
num = 9
for i in sorted_alph:
	answer += (num*i[1])
	num -= 1

print(answer)

'''
Difficulty : G4
Greedy, Implementation
Dict Type을 item 기준으로 정렬하는 방법은 기억해두면 좋을 것 같다!
'''