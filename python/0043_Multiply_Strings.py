class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        num1 = num1[::-1]
        num2 = num2[::-1]
        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)

        for i in range(n2):
            for j in range(n1):
               res[i + j] += int(num1[j]) * int(num2[i])

        for i in range(n1 + n2):
            carry = res[i] // 10
            if carry > 0:
                res[i + 1] += carry
            res[i] %= 10
        
        while res[-1] == 0:
            res.pop()

        return ''.join(str(x) for x in reversed(res))