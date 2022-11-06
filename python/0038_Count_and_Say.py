class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        digitStr = self.countAndSay(n - 1)
        
        res = ""
        targetChar = digitStr[0]
        count = 1
        
        for i in range(1, len(digitStr)):
            cur = digitStr[i]
            if cur == targetChar:
                count += 1
            else:
                res += str(count) + targetChar
                targetChar = cur
                count = 1
                
        res += str(count) + targetChar

        return res
