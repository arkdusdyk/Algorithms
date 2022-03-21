def solution(s):
	answer = 0
	num_vocab = ['zero','one','two','three','four','five','six','seven','eight','nine']
	for i in range(len(num_vocab)):
		s = s.replace(num_vocab[i], str(i))
	answer = int(s)
	return answer

s = "one4seveneight"
print(solution(s))

# 2021 KAKAO Internship Level1
# replace 함수로 너무 쉽게 가능