def solution(lottos, win_nums):
    answer = []
    lottos.sort()
    win_nums.sort()
    cnt_zero = 0
    cnt = 0

    j = 0 				# Two pointer
    for i in range(len(lottos)):
        if lottos[i] == 0:
            cnt_zero += 1
        else:
            if j == len(win_nums):
                break
            if lottos[i] > win_nums[j]:
                while lottos[i] > win_nums[j]:
                    j += 1
                    if j == len(win_nums):
                        break
                if j == len(win_nums):
                    break
            if lottos[i] == win_nums[j]:
                cnt += 1
                j += 1
    max_rank = 7-(cnt+cnt_zero)
    min_rank = 7- cnt
    if max_rank > 6:		# 1개, 0개 번호 일치 = 모두 6
        max_rank = 6
    if min_rank > 6:
        min_rank = 6
    answer.append(max_rank)
    answer.append(min_rank)
    return answer

'''
2021 Dev-Matching: 웹 백엔드 개발. Level1 (구현)
'''