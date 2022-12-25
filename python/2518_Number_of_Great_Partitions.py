class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums) < 2 * k:
            return 0

        # Reverse problem: find number of partitions where the sum of one group is less than k
        # Equivalently: number of subsets where the sum of the subset is less than k

        nums.sort()
        n = len(nums)

        dp = [0] * k # dp[i]: number of subsets with sum equal to i
        dp[0] = 1 

        # after each iteration, determines dp if we use up to element i to make a subset
        for i in range(n):
            # Each sum from nums[i] to k - 1 can be achieved by adding nums[i]
            # Loop backwards because nums[i] could be used more than once if loop forwards
            for j in range(k - 1, nums[i] - 1, -1): 
                dp[j] += dp[j - nums[i]]
        
        return int(2 ** n - 2 * sum(dp)) % 1000000007