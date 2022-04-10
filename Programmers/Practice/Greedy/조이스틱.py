def solution(name):
    answer = 0
    num = list(min(ord("Z")-ord(i)+1,ord(i)-ord("A")) for i in name)
    cur = 0
    name_len = len(name)
    while True:
    	answer += num[cur]
    	change[cur] = 0
    	if change.count(0) == name_len:
    		break

    	l,r = name

    A_cnt = len(name)-name.count('A')
    name_l = list('A' for i in range(len(name)))
    while A_cnt:
    	answer += min(ord('Z')-ord(name[cur])+1,ord(name[cur])-ord('A'))
    	name_l[cur] = name[cur]
    	A_cnt -= 1
    	if A_cnt == 0:		# no more moves
    		break
    	l,r = cur,cur
    	cnt = 0
    	while True:
    		cnt += 1
    		l = (l-1)%len(name_l)
    		r = (r+ 1)%len(name_l)
    		if name[r] != 'A':
    			cur = r
    			answer += cnt
    			break
    		elif name[l] != 'A':
    			cur = l
    			answer += cnt
    			break
    return answer

name = "JEROEN"
print(solution(name))
# 코딩테스트 연습 : Greedy Level 2