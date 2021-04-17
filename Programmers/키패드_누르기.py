a = [[0]*12 for _ in range(12)]
a[1][2] = 1; a[1][5]=2; a[1][8]=3; a[1][0] =4;
a[2][5] = 1; a[2][8]=2; a[2][0]=3; a[5][8] =1; a[5][0]=2; a[8][0]=1;
a[3][2] = 1; a[3][5]=2; a[3][8]=3; a[3][0] =4;
a[4][2] = 2; a[4][5]=1; a[4][8]=2; a[4][0] =3;
a[6][2] = 2; a[6][5]=1; a[6][8]=2; a[6][0] =3;
a[7][2] = 3; a[7][5]=2; a[7][8]=1; a[7][0] =2;
a[9][2] = 3; a[9][5]=2; a[9][8]=1; a[9][0] =2;
a[10][2] = 3; a[10][5]=3; a[10][8]=2; a[10][0]=1;
a[11][2] = 3; a[11][5]=3; a[11][8]=2; a[11][0]=1;
for i in range(10):
	for j in range(10):
		if(a[j][i]!=0):
			a[i][j] = a[j][i]

def closer_dist(start_L, start_R, end, h):
	if a[start_L][end] < a[start_R][end]:
		return 'L'
	elif a[start_L][end] > a[start_R][end]:
		return 'R'
	else:
		return 'R' if (h=='right') else 'L'

def solution(numbers, hand):
    answer = ''
    L_list = [1,4,7]
    R_list = [3,6,9]
    cur_L = 10
    cur_R = 11
    for i in range(len(numbers)):
    	if numbers[i] in L_list:
    		answer+='L'
    		cur_L = numbers[i]
    	elif numbers[i] in R_list:
    		answer+='R'
    		cur_R = numbers[i]
    	else :
    		res = closer_dist(cur_L, cur_R, numbers[i], hand)
    		if res=='L':
    			cur_L = numbers[i]
    			answer+= 'L'
    		else:
    			cur_R = numbers[i]
    			answer += 'R'
    return answer

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"
print(solution(numbers, hand))

# 2020 카카오 인턴십 1번 키패드 누르기 문제 (구현)
# 키패드의 종류가 적기 때문에 distance matrix 'a'를 정의할 수 있었다.
# key_dict = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), ...}
# 이런식으로 각 위치와 (L,R 까지의 distance를 확인하는 방법도 있다..)