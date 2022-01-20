import sys
input = sys.stdin.readline
t = int(input())

def frog_cnt(sound):
	answer = 0
	frog = {"c": 0, "r":0, "o": 0, "a":0, "k": 0}
	for ch in sound:
		frog[ch] += 1
		if not(frog['c'] >= frog['r'] >= frog['o'] >= frog['a'] >= frog['k']):
			answer = -1
			break
		if ch == 'c':
			if 0 not in frog.values():
				for v in frog.keys():
					frog[v] -= 1
	if frog['c'] == frog['r'] == frog['o'] == frog['a'] == frog['k']:
		answer = frog['c']
	else:
		answer = -1
	return answer

for i in range(t):
	snd = input().rstrip()
	print("#%d %d" %(i+1, frog_cnt(snd)))


# Dict type을 활용해서 생각보다 쉽게 해결한 문제.