def solution(s):
    answer = len(s)
    if len(s) == 1:
    	return 1
    for step in range(1, len(s)):
        new_s = ''
        cnt = 1
        cur = s[:step]
        for i in range(step, len(s), step):
        	if cur == s[i:i+step]:
        		cnt += 1
        	else:
        		if cnt > 1:
        			new_s += (str(cnt) + cur)
        		else:
        			new_s += cur
        		cur = s[i:i+step]
        		cnt = 1
        	if (i+step) >= len(s):		# 마지막 파트 처리
        		if cnt > 1:
        			new_s += (str(cnt) + cur)
        		else:
        			new_s += cur
        answer = min(answer, len(new_s))
    return answer
'''
s = 'aabbaccc'
print(solution(s))
'''

# 2020 카카오 BLIND Recruitment (문자열) Level2
