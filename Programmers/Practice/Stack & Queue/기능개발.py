import math
def solution(progresses, speeds):
    answer = []
    stack = []
    for i in range(len(progresses)):
    	stack.append(math.ceil((100-progresses[i])/speeds[i]))
    cur = stack[0]
    done = 0
    for i in range(len(stack)):
    	stack[i] -= cur
    	if stack[i] <= 0:
    		done += 1
    	if stack[i] > 0:
    		answer.append(done)
    		done = 0
    		cur += stack[i]
    		done +=1
    answer.append(done)
    return answer

progresses = [93,30,55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))
# 코딩테스트 연습 : 스택/큐 Level2