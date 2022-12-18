class Solution:
    def smallestValue(self, n: int) -> int:
        while self.factorSum(n) < n:
            n = self.factorSum(n)
        return n
        
    def factorSum(self, n):
        sum = 0
        i = 2
        while n > 1:
            while n % i == 0:
                sum += i
                n //= i
            i += 1
        return sum