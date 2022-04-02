def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
    	if phone_book[i+1].startswith(phone_book[i]):
    		return False
    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))
# 코딩테스트 연습 : Hash Level2
# hash 카테고리 문제긴 한데.. 굳이 dict만들어야할지 싶다