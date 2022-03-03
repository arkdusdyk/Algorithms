import re
def solution(new_id):
    answer = ''
    # Step1
    first = new_id.lower()
    # Step2
    chk = "-_."
    second = ""
    for ch in first:
    	if ch.isalnum() or ch in chk:
    		second += ch
    #Step3
    third = re.sub(r'[.]+', '.', second)
    #Step4
    four = third.strip(".")
    #Step5
    five = four
    if five == "":
    	five = "a"
    #Step6
    six = five[:15]
    six = six.rstrip('.')
    #Step7
    answer = six + (six[len(six)-1]*(3-len(six)))
    return answer

new_id = '...!@BaT#*..y.abcdefghijklm'
print(solution(new_id))

# 2021 KAKAO BLIND RECRUITMENT Level1
# 마침 정규 표현식을 공부하고 있었기 때문에 이를 활용해 훨씬 쉽게 구현할 수 있었다. (Step3)
# 파이썬 기본 제공 라이브러리 (strip(), lower())는 많이 알수록 좋다!