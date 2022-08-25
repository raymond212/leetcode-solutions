class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        count = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
                count += 1
            else:
                return False
        return count % 2 == 0