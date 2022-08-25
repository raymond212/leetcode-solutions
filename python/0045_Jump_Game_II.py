# Greedy
class Solution1:
    def jump(self, nums: List[int]) -> int:
        end, most_right, step = 0, 0, 0
        for i in range(len(nums) - 1):
            most_right = max(most_right, i + nums[i])
            if i == end:
                end = most_right
                step += 1
        return step

# DP
class Solution2:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n # dp[i] represents the minimum number of jumps to get to index i
        dp[0] = 0
        
        for i in range(n):
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                dp[j] = min(dp[i] + 1, dp[j])
        
        return dp[n - 1]