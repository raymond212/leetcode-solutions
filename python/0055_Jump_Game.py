# Greedy
class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        most_right = 0
        for i in range(n):
            if i <= most_right:
                most_right = max(most_right, i + nums[i])
                if most_right >= n - 1:
                    return True
        return False

# DP TLE
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n # dp[i]: if it is possible to get to nums[i]
        dp[0] = True
        
        for i in range(len(nums)):
            if dp[i] == False:
                continue
            
            for j in range(min(i + nums[i] + 1, n)):
                dp[j] = True
        
        return dp[n - 1]