class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            if n % 2 != 0:
                return False
            n //= 2
        return n == 1