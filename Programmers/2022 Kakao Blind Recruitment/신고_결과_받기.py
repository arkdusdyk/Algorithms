def solution(id_list, report, k):
    answer = []
    cnt = dict()            # 신고 당한 사람 : 횟수  
    target_dict = dict()    # 신고한 사람 : 신고 당하는 사람
    for i in id_list:
        cnt[i] = 0
        target_dict[i] = []
    
    for rep in report:
        mem, trgt = rep.split(' ')
        if trgt not in target_dict[mem]:
            target_dict[mem].append(trgt)
            cnt[trgt] += 1
    
    # find banned
    banned = []
    for key in cnt:
        if cnt[key] >= k:
            banned.append(key)
    
    for i in id_list:
        res = 0
        for tar in target_dict[i]:
            if tar in banned:
                res += 1
        answer.append(res)
    
    return answer


'''
2022 KAKAO Blind Recruitment Level1
단순 구현 문제지만 어떤 자료구조에 저장할지를 고민하는게 중요한 문제
-> 사전 두개에 저장. 효율성도 체크했다면 통과했을까
'''