class Solution(object):
    def romanToInt(self, s):
        answer = 0
        roman_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        i = 0
        while i < len(s):
            subtract_flag = False
            if s[i] == "I":
                if (i+1) < len(s):
                    if s[i+1] == "V":
                        answer += 4
                        subtract_flag = True
                    elif s[i+1] == "X":
                        answer += 9
                        subtract_flag = True
            elif s[i] == "X":
                if (i+1) < len(s):
                    if s[i+1] == "L":
                        answer += 40
                        subtract_flag = True
                    elif s[i+1] == "C":
                        answer += 90
                        subtract_flag = True
            elif s[i] == "C":
                if (i+1) < len(s):
                    if s[i+1] == "D":
                        answer += 400
                        subtract_flag = True
                    elif s[i+1] == "M":
                        answer += 900
                        subtract_flag = True

            if subtract_flag == True:
                i += 2
                continue
            answer += roman_dict[s[i]]
            i += 1
        return answer

s = "MCMXCVI"
solution = Solution()
print(solution.romanToInt(s))

# 단순 구현
# LeetCode Challenges for New Users