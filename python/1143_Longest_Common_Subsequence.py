class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        if a is None or b is None:
            return 0
        
        n, m = len(a), len(b)
        dp = [[0] * (m + 1) for _ in range(2)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1], dp[(i - 1) % 2][j - 1] + 1)
                else:
                    dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1])
        
        return dp[n % 2][m]