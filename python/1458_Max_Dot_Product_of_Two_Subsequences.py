class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[nums1[i] * nums2[j] for j in range(n)] for i in range(m)]
        max_dp = [[float('-inf')] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    dp[i][j] = max(dp[i][j], max_dp[i - 1][j - 1] + nums1[i] * nums2[j])
                max_dp[i][j] = dp[i][j]
                if i > 0:
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i - 1][j])
                if j > 0:
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][j - 1])
        return max(max(row) for row in dp)
