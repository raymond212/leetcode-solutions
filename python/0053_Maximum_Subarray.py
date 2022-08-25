class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [0] * 2
        
        res = nums[0]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i % 2] = nums[i]
            dp[i % 2] = max(dp[i % 2], dp[(i - 1) % 2] + nums[i])
            res = max(res, dp[i % 2])
        
        return res