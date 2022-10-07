class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x *= sign
        res = 0
        while x > 0:
            digit = x % 10
            x //= 10
            res *= 10
            res += digit
        res *= sign
        if res > 2 ** 31 - 1 or res < -(2 ** 31):
            return 0
        return res
            
            