# DP
class Solution1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return -1
        
        n = len(triangle)
        dp = [[0] * n, [0] * n]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            dp[i % 2][0] = dp[(i - 1) % 2][0] + triangle[i][0]
            dp[i % 2][i] = dp[(i - 1) % 2][i - 1] + triangle[i][i]
            for j in range(1, i):
                dp[i % 2][j] = min(dp[(i - 1) % 2][j], dp[(i - 1) % 2][j - 1]) + triangle[i][j]

        return min(dp[(n - 1) % 2])

# Memoization
class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        return self.dfs(triangle, 0, 0, memo)

    def dfs(self, triangle, row, col, memo):
        if (row, col) in memo:
            return memo[(row, col)]

        if row == len(triangle):
            return 0
        
        res = min(self.dfs(triangle, row + 1, col, memo), self.dfs(triangle, row + 1, col + 1, memo)) + triangle[row][col]
        memo[(row, col)] = res
        return res