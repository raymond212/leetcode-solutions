class Solution1:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for x in nums:
            for t in range(target, x - 1, -1):  # loop backwards to avoid using x multiple times
                dp[t] = dp[t] or dp[t - x]

        return dp[target]


class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        nums.sort()
        memo = {}

        def dfs(index, target):
            if target == 0:
                return True
            if index == len(nums):
                return False

            key = (index, target)
            if key in memo:
                return memo[key]
            
            memo[key] = dfs(index + 1, target) or dfs(index + 1, target - nums[index])
            return memo[key]
        
        return dfs(0, total // 2)
