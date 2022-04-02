def solution(participant, completion):
    answer = ''
    part_dict = dict()
    for part in participant:
        if part in part_dict:
            part_dict[part] += 1
        else:
            part_dict[part] = 1
    for complete in completion:
        part_dict[complete] -= 1
    for member in part_dict:
        if part_dict[member] > 0:
            answer = member
            break
    return answer

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))

# 코딩테스트 연습 : Hash Level1