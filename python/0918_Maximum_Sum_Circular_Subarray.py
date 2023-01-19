class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        arr_sum = sum(nums)
        n = len(nums)
        max_dp = [nums[0], 0]
        min_dp = [nums[0], 0]
        res = nums[0]
        for i in range(1, n):
            max_dp[i % 2] = max(nums[i], max_dp[(i - 1) % 2] + nums[i])
            res = max(res, max_dp[i % 2])
            if i != n - 1:
                min_dp[i % 2] = min(nums[i], min_dp[(i - 1) % 2] + nums[i])
                res = max(res, arr_sum - min_dp[i % 2])

        return res