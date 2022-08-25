class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # similar to LIS. Consider a sorted nums, we need to find the LIS such that the previous number in the sequence is divisible by the next one in the sequence
        nums.sort()
        n = len(nums)
        dp, prev = {}, {}
        for num in nums:
            dp[num] = 1
            prev[num] = -1
        
        last_num = nums[0]
        for num in nums:
            for factor in self.get_factors(num):
                if factor not in dp:
                    continue
                if dp[num] < dp[factor] + 1:
                    dp[num] = dp[factor] + 1
                    prev[num] = factor
            if dp[num] > dp[last_num]:
                last_num = num
        
        return self.get_path(prev, last_num)
    
    def get_path(self, prev, last_num):
        path = []
        while last_num != -1:
            path.append(last_num)
            last_num = prev[last_num]
        return path[::-1]
    
    def get_factors(self, num):
        if num == 1:
            return []
        factor = 1
        factors = []
        while factor * factor <= num:
            if num % factor == 0:
                factors.append(factor)
                if factor * factor != num and factor != 1:
                    factors.append(num // factor)
            factor += 1
        return factors