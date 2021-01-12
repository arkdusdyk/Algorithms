def check_3(checker):
	if(checker%10==3 or checker//10==3):
		return True
	else:
		return False
N = int(input())
cnt=0
for i in range(N+1):
	for j in range(60):
		for k in range(60):
			if(check_3(i) or check_3(j) or check_3(k)):
				cnt+=1
print(cnt)

#Bruteforce
'''can also use str transformation instead of functions
ex)
if '3' in str(i) + str(j) + str(k) : cnt+=1
: i+j+k forms string, check if '3' inside string
