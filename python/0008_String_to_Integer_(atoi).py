class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        sign = 1
        readingInt = False
        
        for i in range(len(s)):
            if readingInt:
                if s[i].isdigit():
                    num = num * 10 + (ord(s[i]) - ord('0'))
                    continue
                break
            else:
                if s[i] == " ":
                    continue
                elif s[i] == "+":
                    readingInt = True
                elif s[i] == "-":
                    readingInt = True
                    sign = -1
                elif s[i].isdigit():
                    readingInt = True
                    num = ord(s[i]) - ord('0')
                else:
                    break
        
        num *= sign
        threshold = 2 ** 31 - 1
        
        if num > threshold:
            num = threshold
        if num < -threshold - 1:
            num = -threshold - 1
        
        return num