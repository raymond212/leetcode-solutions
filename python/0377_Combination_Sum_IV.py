# DP
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if num > i:
                    break
                dp[i] += dp[i - num] 

        return dp[-1]

# Memoization
class Solution2:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = {}

        def dfs(target):
            if target == 0:
                return 1
            if target in memo:
                return memo[target]

            ans = 0
            for num in nums:
                if num > target:
                    break
                ans += dfs(target - num)
            
            memo[target] = ans
            return ans
        
        return dfs(target)
