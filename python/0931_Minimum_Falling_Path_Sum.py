class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[matrix[i][j] for j in range(n)] for i in range(n)]
        
        for i in range(1, n):
            dp[i][0] += min(dp[i - 1][0], dp[i - 1][1])
            dp[i][m - 1] += min(dp[i - 1][m - 1], dp[i - 1][m - 2])
            for j in range(1, m - 1):
                dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])

        return min(dp[n - 1])