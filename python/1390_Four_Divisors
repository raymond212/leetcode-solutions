class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            y = 1
            divisors = set()
            while y ** 2 <= x: 
                if x % y == 0:
                    divisors.add(y)
                    divisors.add(x // y)
                if len(divisors) > 4:
                    break
                y += 1
            if len(divisors) == 4:
                res += sum(divisors)
        return res